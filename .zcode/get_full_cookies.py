"""
在你的已登录 Chrome 里执行（通过 CDP），查看完整的登录态信息
包括 localStorage、所有 cookie（含 HttpOnly）、appStore.userInfo
"""
import os, json, time, subprocess, socket, shutil, urllib.request, websocket

os.environ['NO_PROXY'] = '127.0.0.1,localhost'
os.environ['no_proxy'] = '127.0.0.1,localhost'

LOCAL = os.environ.get('LOCALAPPDATA')
CHROME = r'C:\Program Files\Google\Chrome\Application\chrome.exe'
SRC_USER_DATA = os.path.join(LOCAL, 'Google', 'Chrome', 'User Data')
JUNCTION = os.path.join(LOCAL, 'Temp', 'chrome_junction_live2')
DEBUG_PORT = 9230


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
    # 杀掉调试用 chrome（保留你的日常 Chrome）
    subprocess.run(['powershell', '-Command',
        "Get-Process chrome -ErrorAction SilentlyContinue | "
        "Where-Object {(Get-CimInstance Win32_Process -Filter \"ProcessId=$($_.Id)\").CommandLine -like '*remote-debugging-port*'} | "
        "Stop-Process -Force; Start-Sleep 1"], capture_output=True)

    # 删除旧 junction
    if os.path.exists(JUNCTION):
        try: os.rmdir(JUNCTION)
        except: subprocess.run(['cmd', '/c', 'rmdir', JUNCTION], capture_output=True)
    # 创建 junction 指向原 User Data（你的 Chrome 正在运行，cookie 文件含 session）
    subprocess.run(['cmd', '/c', 'mklink', '/J', JUNCTION, SRC_USER_DATA], capture_output=True)
    print('junction ✓')

    # 关键：用 junction 启动，但你的 Chrome 占用了 profile（SingletonLock）
    # 解决：复制 SingletonLock 的方式——用 --no-first-run 并指定不同的 profile directory 名
    # 实际上 Chrome 允许第二个实例用同一 user-data-dir 但不同 profile
    # 或者：直接用 junction 但加 --profile-directory=Default，Chrome 会检测到锁
    # 试试看能否启动
    proc = subprocess.Popen(
        [CHROME, f'--remote-debugging-port={DEBUG_PORT}', f'--user-data-dir={JUNCTION}',
         '--profile-directory=Default', '--no-first-run', '--no-default-browser-check',
         '--headless=new', '--disable-gpu',
         '--proxy-server=http://proxyhk.zte.com.cn:80', '--proxy-bypass-list=127.0.0.1;localhost',
         '--remote-allow-origins=*', 'about:blank'],
        stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    ready = wait_port(DEBUG_PORT, 30)
    if not ready:
        print('❌ 端口未就绪（profile 被你的 Chrome 占用）')
        proc.terminate()
        try:
            out, err = proc.communicate(timeout=3)
            print(err.decode('utf-8', errors='replace')[:300])
        except: proc.kill()
        return
    print('✓ 端口就绪')

    try:
        with urllib.request.urlopen(f'http://127.0.0.1:{DEBUG_PORT}/json/version', timeout=5) as r:
            ver = json.load(r)
        browser_ws = ver['webSocketDebuggerUrl']

        # 导航到 nowcoder
        ws = websocket.create_connection(browser_ws, timeout=15, suppress_origin=False)
        ws.send(json.dumps({'id': 1, 'method': 'Target.createTarget',
                            'params': {'url': 'https://www.nowcoder.com/exam/intelligent'}}))
        ws.recv()
        ws.close()
        time.sleep(10)

        # 读所有 cookie（含 HttpOnly）
        ws = websocket.create_connection(browser_ws, timeout=15, suppress_origin=False)
        ws.send(json.dumps({'id': 2, 'method': 'Network.getAllCookies'}))
        resp = json.loads(ws.recv())
        ws.close()
        cookies = resp.get('result', {}).get('cookies', [])
        nc = [c for c in cookies if 'nowcoder' in c.get('domain', '')]
        print(f'\n=== {len(nc)} 个 nowcoder cookie（含 HttpOnly）===')
        for c in nc:
            v = c['value']
            httponly = c.get('httpOnly', False)
            print(f'  {"[H]" if httponly else "   "} {c["name"]:25} = {v[:30]}{"..." if len(v)>30 else ""}')

        # 保存完整 cookie
        out = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'nowcoder_cookies_full.json')
        with open(out, 'w', encoding='utf-8') as f:
            json.dump({'cookies': nc,
                       'cookie_string': '; '.join(f"{c['name']}={c['value']}" for c in nc)},
                      f, ensure_ascii=False, indent=2)
        print(f'\n保存到 {out}')
    finally:
        try: proc.terminate(); proc.wait(timeout=5)
        except: proc.kill()
        try: os.rmdir(JUNCTION)
        except: subprocess.run(['cmd', '/c', 'rmdir', JUNCTION], capture_output=True)


if __name__ == '__main__':
    main()
