"""
junction 方案：Chrome 正在运行且已登录，junction 指向原 User Data
Chrome 启动后读取的 cookie 文件就是当前运行中 Chrome 的文件（含 session cookie）
v20 key 能解密（因为是原路径）
注意：不用 headless（headless 不加载 cookie），用 --headless=new 但导航到 nowcoder 触发加载
"""
import os, sys, json, time, subprocess, socket, urllib.request, websocket

os.environ['NO_PROXY'] = '127.0.0.1,localhost'
os.environ['no_proxy'] = '127.0.0.1,localhost'

LOCAL = os.environ.get('LOCALAPPDATA')
CHROME = r'C:\Program Files\Google\Chrome\Application\chrome.exe'
SRC_USER_DATA = os.path.join(LOCAL, 'Google', 'Chrome', 'User Data')
JUNCTION_USER_DATA = os.path.join(LOCAL, 'Temp', 'chrome_junction_live')
PROFILE = 'Default'
DEBUG_PORT = 9224  # 换个端口避免冲突
OUTPUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'nowcoder_cookies.json')


def kill_debug_chrome():
    subprocess.run(['powershell', '-Command',
                    "Get-Process chrome -ErrorAction SilentlyContinue | "
                    "Where-Object {(Get-CimInstance Win32_Process -Filter \"ProcessId=$($_.Id)\").CommandLine -like '*remote-debugging-port*'} | "
                    "Stop-Process -Force; Start-Sleep 1"],
                   capture_output=True)


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
    print('清理调试 Chrome...')
    kill_debug_chrome()

    # 创建/重建 junction
    if os.path.exists(JUNCTION_USER_DATA):
        try: os.rmdir(JUNCTION_USER_DATA)
        except: subprocess.run(['cmd', '/c', 'rmdir', JUNCTION_USER_DATA], capture_output=True)
    r = subprocess.run(['cmd', '/c', 'mklink', '/J', JUNCTION_USER_DATA, SRC_USER_DATA],
                       capture_output=True, text=True)
    if r.returncode != 0:
        print('junction 失败:', r.stderr); return
    print('  junction ✓ (指向原 User Data，含实时 session cookie)')

    print(f'启动 Chrome（端口 {DEBUG_PORT}，junction profile）...')
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
        stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

    try:
        if not wait_port(DEBUG_PORT, 40):
            print('❌ 端口未就绪'); return
        print('✓ 端口就绪')

        with urllib.request.urlopen(f'http://127.0.0.1:{DEBUG_PORT}/json/version', timeout=5) as r:
            ver = json.load(r)
        browser_ws = ver['webSocketDebuggerUrl']

        # 导航到 nowcoder（触发 cookie 加载）
        ws = websocket.create_connection(browser_ws, timeout=15, suppress_origin=False)
        ws.send(json.dumps({'id': 1, 'method': 'Target.createTarget',
                            'params': {'url': 'https://www.nowcoder.com/exam/intelligent'}}))
        ws.recv()
        ws.close()
        print('  导航到 nowcoder，等待加载...')
        time.sleep(10)

        # 读 cookie
        ws = websocket.create_connection(browser_ws, timeout=15, suppress_origin=False)
        ws.send(json.dumps({'id': 2, 'method': 'Network.getAllCookies'}))
        resp = json.loads(ws.recv())
        ws.close()
        cookies = resp.get('result', {}).get('cookies', [])

        nc = [c for c in cookies if 'nowcoder' in c.get('domain', '')]
        print(f'✓ 共 {len(nc)} 个 nowcoder cookie')

        if nc:
            result = {
                'cookies': nc,
                'cookie_string': '; '.join(f"{c['name']}={c['value']}" for c in nc),
            }
            with open(OUTPUT, 'w', encoding='utf-8') as f:
                json.dump(result, f, ensure_ascii=False, indent=2)
            names = sorted({c['name'] for c in nc})
            print(f'  cookie 名: {names}')
            has_uid = 'uid' in names
            print(f'  登录态: {"✓ 已登录（有 uid）" if has_uid else "✗ 无 uid session cookie"}')
            for key_name in ['uid', 'username', 'uid.sig', 'NOWCODERUID', 'csrfToken', 't']:
                for c in nc:
                    if c['name'] == key_name:
                        print(f'    {key_name:18} = {c["value"][:25]}{"..." if len(c["value"])>25 else ""}')
            print(f'\n✓ 已保存到 {OUTPUT}')
        else:
            print('  ❌ 0 cookie')
    finally:
        try:
            proc.terminate()
            proc.wait(timeout=5)
        except:
            proc.kill()


if __name__ == '__main__':
    main()
