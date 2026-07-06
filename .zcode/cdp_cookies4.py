"""
方案：用原 profile 启动非 headless Chrome 开调试端口
Chrome 的 'requires non-default data directory' 限制只针对 headless 模式
非 headless + 原 profile 可以正常开调试端口
"""
import os, sys, json, time, subprocess, socket, urllib.request, websocket

os.environ['NO_PROXY'] = '127.0.0.1,localhost'
os.environ['no_proxy'] = '127.0.0.1,localhost'

LOCAL = os.environ.get('LOCALAPPDATA')
CHROME = r'C:\Program Files\Google\Chrome\Application\chrome.exe'
USER_DATA = os.path.join(LOCAL, 'Google', 'Chrome', 'User Data')
PROFILE = 'Default'
DEBUG_PORT = 9223
OUTPUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'nowcoder_cookies.json')


def kill_chrome():
    subprocess.run(['powershell', '-Command',
                    'Stop-Process -Name chrome -Force -ErrorAction SilentlyContinue; Start-Sleep 2'],
                   capture_output=True)
    for lockname in ['SingletonLock', 'SingletonCookie', 'SingletonSocket']:
        for d in [os.path.join(USER_DATA, PROFILE), USER_DATA]:
            try: os.remove(os.path.join(d, lockname))
            except OSError: pass


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
    with urllib.request.urlopen(f'http://127.0.0.1:{port}/json/version', timeout=5) as r:
        ver = json.load(r)
    ws_url = ver['webSocketDebuggerUrl']
    ws = websocket.create_connection(ws_url, timeout=15, suppress_origin=False)
    ws.send(json.dumps({'id': 1, 'method': 'Storage.getCookies'}))
    resp = json.loads(ws.recv())
    ws.close()
    cookies = resp.get('result', {}).get('cookies', [])
    if not cookies:
        ws = websocket.create_connection(ws_url, timeout=15, suppress_origin=False)
        ws.send(json.dumps({'id': 2, 'method': 'Network.getAllCookies'}))
        resp = json.loads(ws.recv())
        ws.close()
        cookies = resp.get('result', {}).get('cookies', [])
    return cookies


def main():
    print('清理 Chrome 进程和锁文件...')
    kill_chrome()

    print(f'启动 Chrome（调试端口 {DEBUG_PORT}，原 profile，非 headless）...')
    # 关键：不加 --headless，用原 profile
    proc = subprocess.Popen(
        [CHROME,
         f'--remote-debugging-port={DEBUG_PORT}',
         f'--user-data-dir={USER_DATA}',
         f'--profile-directory={PROFILE}',
         '--no-first-run', '--no-default-browser-check',
         '--no-proxy-server',
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


if __name__ == '__main__':
    main()
