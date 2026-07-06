"""
最终方案：用 VSS 复制的 cookie 文件（含 session cookie）替换 junction profile 的 cookie，
启动 junction Chrome 解密 v20，CDP 读取明文 cookie。
关键：junction 指向原 User Data，v20 key 能解密；但 cookie 文件用 VSS 版本（含 session cookie）
"""
import os, sys, json, time, subprocess, socket, shutil, urllib.request, websocket

os.environ['NO_PROXY'] = '127.0.0.1,localhost'
os.environ['no_proxy'] = '127.0.0.1,localhost'

LOCAL = os.environ.get('LOCALAPPDATA')
CHROME = r'C:\Program Files\Google\Chrome\Application\chrome.exe'
SRC_USER_DATA = os.path.join(LOCAL, 'Google', 'Chrome', 'User Data')
# 这次用复制方式（不用 junction，因为要替换 cookie 文件）
TMP_USER_DATA = os.path.join(LOCAL, 'Temp', 'chrome_cookie_profile')
PROFILE = 'Default'
VSS_COOKIE_DB = os.path.join(LOCAL, 'Temp', 'chrome_cookies_vss2.db')
DEBUG_PORT = 9223
OUTPUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'nowcoder_cookies.json')


def kill_chrome_debug_only():
    """只杀调试用的 Chrome（headless），不动用户的日常 Chrome
    headless Chrome 的命令行含 remote-debugging-port
    """
    # 找出占用 9223 的进程并杀掉
    subprocess.run(['powershell', '-Command',
                    "Get-Process chrome -ErrorAction SilentlyContinue | "
                    "Where-Object {(Get-CimInstance Win32_Process -Filter \"ProcessId=$($_.Id)\").CommandLine -like '*remote-debugging-port*'} | "
                    "Stop-Process -Force; Start-Sleep 1"],
                   capture_output=True)


def setup_profile():
    """设置临时 profile：复制 Local State（v20 key）+ VSS cookie 文件"""
    # 清理旧的
    if os.path.exists(TMP_USER_DATA):
        shutil.rmtree(TMP_USER_DATA, ignore_errors=True)
    os.makedirs(os.path.join(TMP_USER_DATA, PROFILE, 'Network'), exist_ok=True)

    # 复制 Local State（含 v20 加密 key，绑定 Chrome 安装 + Windows 用户）
    ls_src = os.path.join(SRC_USER_DATA, 'Local State')
    ls_dst = os.path.join(TMP_USER_DATA, 'Local State')
    shutil.copy2(ls_src, ls_dst)
    print('  复制 Local State ✓')

    # 复制 VSS cookie 文件（含 session cookie）
    cookie_dst = os.path.join(TMP_USER_DATA, PROFILE, 'Network', 'Cookies')
    shutil.copy2(VSS_COOKIE_DB, cookie_dst)
    print('  复制 VSS Cookies ✓')

    # 也复制 journal（如果有）
    journal_src = os.path.join(LOCAL, 'Temp', 'chrome_cookies_vss2.db-journal')
    if os.path.exists(journal_src):
        shutil.copy2(journal_src, cookie_dst + '-journal')

    # 复制 Preferences（让 Chrome 识别 profile）
    pref_src = os.path.join(SRC_USER_DATA, PROFILE, 'Preferences')
    if os.path.exists(pref_src):
        shutil.copy2(pref_src, os.path.join(TMP_USER_DATA, PROFILE, 'Preferences'))

    print(f'  临时 profile: {TMP_USER_DATA}')


def wait_port(port, timeout=40):
    end = time.time() + timeout
    while time.time() < end:
        try:
            with socket.create_connection(('127.0.0.1', port), timeout=1):
                return True
        except OSError:
            time.sleep(0.5)
    return False


def main():
    print('清理旧的调试 Chrome...')
    kill_chrome_debug_only()

    print('设置临时 profile（VSS cookie + Local State）...')
    setup_profile()

    print(f'启动 Chrome（调试端口 {DEBUG_PORT}）...')
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
        stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

    try:
        if not wait_port(DEBUG_PORT, 40):
            print('❌ 端口未就绪')
            proc.terminate()
            return

        print('✓ 端口就绪，读取 cookie...')

        # 获取 browser ws
        with urllib.request.urlopen(f'http://127.0.0.1:{DEBUG_PORT}/json/version', timeout=5) as r:
            ver = json.load(r)
        browser_ws = ver['webSocketDebuggerUrl']

        # 创建 target 导航到 nowcoder（触发 cookie 加载）
        ws = websocket.create_connection(browser_ws, timeout=15, suppress_origin=False)
        ws.send(json.dumps({'id': 1, 'method': 'Target.createTarget',
                            'params': {'url': 'https://www.nowcoder.com'}}))
        ws.recv()
        ws.close()
        time.sleep(8)

        # 读取所有 cookie
        ws = websocket.create_connection(browser_ws, timeout=15, suppress_origin=False)
        ws.send(json.dumps({'id': 2, 'method': 'Network.getAllCookies'}))
        resp = json.loads(ws.recv())
        ws.close()
        cookies = resp.get('result', {}).get('cookies', [])

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
        has_login = 'uid' in names or 'NOWCODERUID' in names
        print(f'\n=== 关键 cookie ===')
        for key_name in ['uid', 'username', 'NOWCODERUID', 'NOWCODERCLINETID', 'csrfToken', 'acw_tc', 't', 'uid.sig']:
            for c in nc:
                if c['name'] == key_name:
                    v = c['value']
                    print(f'  {key_name:20} = {v[:25]}{"..." if len(v)>25 else ""}')
        print(f'\n登录态: {"✓ 已登录" if "uid" in names else "△ 部分（无 uid session）"}')

    finally:
        try:
            proc.terminate()
            proc.wait(timeout=5)
        except:
            proc.kill()


if __name__ == '__main__':
    main()
