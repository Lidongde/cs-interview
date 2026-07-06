"""
最终方案：用 junction（目录联接）创建一个指向原 User Data 的链接，
路径不同（绕过 Chrome 的默认 profile 检测），但内容相同（v20 cookie 能解密）
"""
import os, sys, json, time, subprocess, socket, urllib.request, websocket

os.environ['NO_PROXY'] = '127.0.0.1,localhost'
os.environ['no_proxy'] = '127.0.0.1,localhost'

LOCAL = os.environ.get('LOCALAPPDATA')
CHROME = r'C:\Program Files\Google\Chrome\Application\chrome.exe'
SRC_USER_DATA = os.path.join(LOCAL, 'Google', 'Chrome', 'User Data')
# junction 路径（与原路径不同，绕过检测）
JUNCTION_USER_DATA = os.path.join(LOCAL, 'Temp', 'chrome_junction_userdata')
PROFILE = 'Default'
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


def create_junction():
    """创建目录联接指向原 User Data"""
    # 先删除旧的 junction
    if os.path.exists(JUNCTION_USER_DATA):
        try:
            os.rmdir(JUNCTION_USER_DATA)  # junction 用 rmdir 删除（不会删原目录内容）
        except Exception:
            subprocess.run(['cmd', '/c', 'rmdir', JUNCTION_USER_DATA], capture_output=True)
    # 创建 junction
    r = subprocess.run(['cmd', '/c', 'mklink', '/J', JUNCTION_USER_DATA, SRC_USER_DATA],
                       capture_output=True, text=True)
    if r.returncode == 0:
        print(f'  创建 junction ✓: {JUNCTION_USER_DATA} -> {SRC_USER_DATA}')
    else:
        print(f'  创建 junction 失败: {r.stderr}')
        return False
    return True


def wait_port(port, timeout=40):
    end = time.time() + timeout
    while time.time() < end:
        try:
            with socket.create_connection(('127.0.0.1', port), timeout=1):
                return True
        except OSError:
            time.sleep(0.5)
    return False


def cdp_get_all_cookies(port):
    # 获取 browser websocket
    with urllib.request.urlopen(f'http://127.0.0.1:{port}/json/version', timeout=5) as r:
        ver = json.load(r)
    browser_ws = ver['webSocketDebuggerUrl']

    # 创建 target 导航到 nowcoder
    ws = websocket.create_connection(browser_ws, timeout=15, suppress_origin=False)
    ws.send(json.dumps({'id': 1, 'method': 'Target.createTarget', 'params': {'url': 'https://www.nowcoder.com/exam/intelligent'}}))
    resp = json.loads(ws.recv())
    target_id = resp.get('result', {}).get('targetId', '')
    print(f'  创建 target: {target_id}')
    ws.close()

    # 等待页面加载（含网络请求）
    time.sleep(12)

    # 用 browser 级别 getAllCookies（获取所有 target 的 cookie）
    ws = websocket.create_connection(browser_ws, timeout=15, suppress_origin=False)
    ws.send(json.dumps({'id': 2, 'method': 'Storage.getCookies'}))
    resp = json.loads(ws.recv())
    ws.close()
    cookies = resp.get('result', {}).get('cookies', [])

    # 也试 Network.getAllCookies
    if not cookies:
        ws = websocket.create_connection(browser_ws, timeout=15, suppress_origin=False)
        ws.send(json.dumps({'id': 3, 'method': 'Network.getAllCookies'}))
        resp = json.loads(ws.recv())
        ws.close()
        cookies = resp.get('result', {}).get('cookies', [])

    # 也通过 page target 获取
    if not cookies and target_id:
        with urllib.request.urlopen(f'http://127.0.0.1:{port}/json', timeout=5) as r:
            targets = json.load(r)
        pages = [t for t in targets if t.get('type') == 'page']
        for p in pages:
            try:
                ws = websocket.create_connection(p['webSocketDebuggerUrl'], timeout=10, suppress_origin=False)
                ws.send(json.dumps({'id': 4, 'method': 'Network.getCookies', 'params': {'urls': ['https://www.nowcoder.com', 'https://gw-c.nowcoder.com']}}))
                resp = json.loads(ws.recv())
                ws.close()
                pc = resp.get('result', {}).get('cookies', [])
                if pc:
                    cookies = pc
                    break
            except Exception as e:
                print(f'  page target 获取失败: {e}')

    return cookies


def main():
    print('清理 Chrome 进程和锁文件...')
    kill_chrome()

    print('创建 User Data 的目录联接...')
    if not create_junction():
        return

    print(f'启动 Chrome（调试端口 {DEBUG_PORT}，junction profile）...')
    proc = subprocess.Popen(
        [CHROME,
         f'--remote-debugging-port={DEBUG_PORT}',
         f'--user-data-dir={JUNCTION_USER_DATA}',
         f'--profile-directory={PROFILE}',
         '--no-first-run', '--no-default-browser-check',
         '--headless=new', '--disable-gpu',
         '--proxy-server=http://proxyhk.zte.com.cn:80',
         '--proxy-bypass-list=127.0.0.1;localhost',
         '--remote-allow-origins=*',
         'about:blank'],
        stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    try:
        if not wait_port(DEBUG_PORT, 40):
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
        # 清理 junction
        try:
            os.rmdir(JUNCTION_USER_DATA)
        except Exception:
            subprocess.run(['cmd', '/c', 'rmdir', JUNCTION_USER_DATA], capture_output=True)


if __name__ == '__main__':
    main()
