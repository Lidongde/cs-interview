"""
复制 Chrome profile 的 cookie 相关文件到临时目录，用临时 profile 启动 CDP 读 cookie
Chrome 不允许默认 profile 开调试端口，所以复制一份
"""
import os, sys, json, time, subprocess, socket, shutil, urllib.request, websocket

# 禁用代理，确保 localhost 直连
os.environ['NO_PROXY'] = '127.0.0.1,localhost'
os.environ['no_proxy'] = '127.0.0.1,localhost'

LOCAL = os.environ.get('LOCALAPPDATA')
CHROME = r'C:\Program Files\Google\Chrome\Application\chrome.exe'
SRC_USER_DATA = os.path.join(LOCAL, 'Google', 'Chrome', 'User Data')
PROFILE = 'Default'
TMP_USER_DATA = os.path.join(LOCAL, 'Temp', 'chrome_cdp_profile')
DEBUG_PORT = 9223
OUTPUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'nowcoder_cookies.json')


def kill_chrome():
    subprocess.run(['powershell', '-Command',
                    'Stop-Process -Name chrome -Force -ErrorAction SilentlyContinue; Start-Sleep 2'],
                   capture_output=True)
    for lockname in ['SingletonLock', 'SingletonCookie', 'SingletonSocket']:
        for d in [os.path.join(SRC_USER_DATA, PROFILE), SRC_USER_DATA]:
            try: os.remove(os.path.join(d, lockname))
            except OSError: pass


def copy_profile_cookie_files():
    """复制 Default profile 的关键文件到临时目录（保留 v20 加密可解密性）
    v20 App-Bound Encryption 的 key 绑定 Chrome 安装 + Windows 用户，
    只要 Local State + Default/Network/Cookies 完整，Chrome 能自己解密。
    但需要 Default profile 的 Preferences 让 Chrome 识别这个 profile。
    """
    src_profile = os.path.join(SRC_USER_DATA, PROFILE)
    dst_profile = os.path.join(TMP_USER_DATA, PROFILE)
    os.makedirs(dst_profile, exist_ok=True)
    os.makedirs(os.path.join(dst_profile, 'Network'), exist_ok=True)

    # 关键文件列表
    files = [
        ('Network/Cookies', 'Network/Cookies'),
        ('Network/Cookies-journal', 'Network/Cookies-journal'),
        ('Preferences', 'Preferences'),
        ('Secure Preferences', 'Secure Preferences'),
        ('Login Data', 'Login Data'),
    ]
    for rel_src, rel_dst in files:
        s = os.path.join(src_profile, rel_src)
        d = os.path.join(dst_profile, rel_dst)
        if os.path.exists(s):
            try:
                shutil.copy2(s, d)
                print(f'  复制 {rel_src} ✓')
            except Exception as e:
                print(f'  复制 {rel_src} 失败: {e}')

    # Local State (含加密 key)
    ls_src = os.path.join(SRC_USER_DATA, 'Local State')
    ls_dst = os.path.join(TMP_USER_DATA, 'Local State')
    if os.path.exists(ls_src):
        shutil.copy2(ls_src, ls_dst)
        print('  复制 Local State ✓')

    print(f'  临时 profile: {TMP_USER_DATA}')


def wait_port(port, timeout=30):
    end = time.time() + timeout
    while time.time() < end:
        try:
            with socket.create_connection(('127.0.0.1', port), timeout=1):
                return True
        except OSError:
            time.sleep(0.5)
    return False


def cdp_get_all_cookies(port):
    with urllib.request.urlopen(f'http://127.0.0.1:{port}/json/version', timeout=5) as r:
        ver = json.load(r)
    ws_url = ver['webSocketDebuggerUrl']
    ws = websocket.create_connection(ws_url, timeout=15)
    ws.send(json.dumps({'id': 1, 'method': 'Storage.getCookies'}))
    resp = json.loads(ws.recv())
    ws.close()
    cookies = resp.get('result', {}).get('cookies', [])
    if not cookies:
        ws = websocket.create_connection(ws_url, timeout=15)
        ws.send(json.dumps({'id': 2, 'method': 'Network.getAllCookies'}))
        resp = json.loads(ws.recv())
        ws.close()
        cookies = resp.get('result', {}).get('cookies', [])
    return cookies


def main():
    print('清理 Chrome 进程和锁文件...')
    kill_chrome()

    print('复制 cookie 文件到临时 profile...')
    copy_profile_cookie_files()

    print(f'启动 Chrome（调试端口 {DEBUG_PORT}，临时 profile）...')
    proc = subprocess.Popen(
        [CHROME,
         f'--remote-debugging-port={DEBUG_PORT}',
         f'--user-data-dir={TMP_USER_DATA}',
         f'--profile-directory={PROFILE}',
         '--no-first-run', '--no-default-browser-check',
         '--headless=new', '--disable-gpu',
         '--no-proxy-server',
         '--remote-allow-origins=*',
         'about:blank'],
        stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    try:
        if not wait_port(DEBUG_PORT, 30):
            print('❌ 调试端口未就绪')
            proc.terminate()
            try:
                out, err = proc.communicate(timeout=5)
                print(f'stderr: {err.decode("utf-8", errors="replace")[:600]}')
            except:
                proc.kill()
            return

        print('✓ 调试端口就绪，读取 cookie...')
        cookies = cdp_get_all_cookies(DEBUG_PORT)
        nc = [c for c in cookies if 'nowcoder' in c.get('domain', '')]
        print(f'✓ 共 {len(cookies)} 个 cookie，其中 nowcoder {len(nc)} 个')

        result = {
            'cookies': nc,
            'cookie_string': '; '.join(f"{c['name']}={c['value']}" for c in nc),
        }
        with open(OUTPUT, 'w', encoding='utf-8') as f:
            json.dump(result, f, ensure_ascii=False, indent=2)
        print(f'✓ 已保存到 {OUTPUT}')

        names = {c['name'] for c in nc}
        has_login = 'uid' in names and 'username' in names
        print(f'登录态: {"✓ 已登录" if has_login else "✗ 未登录"}')
        for key_name in ['uid', 'username', 'NOWCODERUID', 'csrfToken', 'acw_tc']:
            for c in nc:
                if c['name'] == key_name:
                    v = c['value']
                    print(f'  {key_name:20} = {v[:18]}{"..." if len(v)>18 else ""}')
    finally:
        try:
            proc.terminate()
            proc.wait(timeout=5)
        except Exception:
            proc.kill()


if __name__ == '__main__':
    main()
