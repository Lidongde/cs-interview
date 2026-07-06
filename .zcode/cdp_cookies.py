"""
通过 CDP 从运行中的 Chrome 读取 nowcoder 明文 cookie
用法：先关闭所有 Chrome，然后运行此脚本（会用你的 profile 启动带调试端口的 Chrome）
"""
import os, sys, json, time, subprocess, socket, urllib.request, websocket

LOCAL = os.environ.get('LOCALAPPDATA')
CHROME = r'C:\Program Files\Google\Chrome\Application\chrome.exe'
USER_DATA = os.path.join(LOCAL, 'Google', 'Chrome', 'User Data')
PROFILE = 'Default'
DEBUG_PORT = 9223
OUTPUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'nowcoder_cookies.json')


def wait_port(port, timeout=20):
    end = time.time() + timeout
    while time.time() < end:
        try:
            with socket.create_connection(('127.0.0.1', port), timeout=1):
                return True
        except OSError:
            time.sleep(0.3)
    return False


def cdp_get_all_cookies(port):
    # 找一个 page target
    for _ in range(10):
        try:
            with urllib.request.urlopen(f'http://127.0.0.1:{port}/json', timeout=3) as r:
                targets = json.load(r)
            pages = [t for t in targets if t.get('type') == 'page']
            if pages:
                break
        except Exception:
            pass
        time.sleep(0.5)
    else:
        # 新开一个 about:blank
        try:
            urllib.request.urlopen(f'http://127.0.0.1:{port}/json/new?about:blank', timeout=3).read()
        except Exception:
            pass
        with urllib.request.urlopen(f'http://127.0.0.1:{port}/json', timeout=3) as r:
            targets = json.load(r)
        pages = [t for t in targets if t.get('type') == 'page']

    if not pages:
        raise RuntimeError('没有可用的 page target')

    ws_url = pages[0]['webSocketDebuggerUrl']
    ws = websocket.create_connection(ws_url, timeout=15)
    ws.send(json.dumps({'id': 1, 'method': 'Network.getAllCookies'}))
    resp = json.loads(ws.recv())
    ws.close()
    return resp.get('result', {}).get('cookies', [])


def main():
    # 检查 Chrome 是否在运行
    try:
        out = subprocess.check_output(
            ['powershell', '-Command',
             "(Get-Process chrome -ErrorAction SilentlyContinue | Measure-Object).Count"],
            stderr=subprocess.DEVNULL).decode().strip()
        chrome_running = int(out or '0') > 0
    except Exception:
        chrome_running = False

    if chrome_running:
        print('⚠️  检测到 Chrome 正在运行。请先关闭所有 Chrome 窗口再运行本脚本。')
        print('   （cookie 文件被锁，且需要用你的 profile 启动调试实例）')
        sys.exit(1)

    print(f'启动 Chrome（调试端口 {DEBUG_PORT}，profile={PROFILE}）...')
    proc = subprocess.Popen(
        [CHROME,
         f'--remote-debugging-port={DEBUG_PORT}',
         f'--user-data-dir={USER_DATA}',
         f'--profile-directory={PROFILE}',
         '--no-first-run', '--no-default-browser-check',
         '--headless=new', '--disable-gpu',
         '--no-proxy-server',
         'about:blank'],
        stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

    try:
        if not wait_port(DEBUG_PORT, 25):
            print('❌ Chrome 调试端口未就绪')
            return
        print('✓ Chrome 调试端口就绪，读取 cookie...')
        cookies = cdp_get_all_cookies(DEBUG_PORT)
        nc = [c for c in cookies if 'nowcoder' in c.get('domain', '')]
        print(f'✓ 共 {len(cookies)} 个 cookie，其中 nowcoder {len(nc)} 个')

        # 构造 cookie 字符串（按 domain 分组，主要用于 .nowcoder.com 和 www.nowcoder.com）
        by_domain = {}
        for c in nc:
            by_domain.setdefault(c['domain'], []).append(c)

        result = {
            'cookies': nc,
            'cookie_string_for_nowcoder': '; '.join(
                f"{c['name']}={c['value']}" for c in nc
                if c['domain'] in ('.nowcoder.com', 'www.nowcoder.com')
            ),
            'cookie_string_all': '; '.join(f"{c['name']}={c['value']}" for c in nc),
        }
        with open(OUTPUT, 'w', encoding='utf-8') as f:
            json.dump(result, f, ensure_ascii=False, indent=2)
        print(f'✓ 已保存到 {OUTPUT}')

        # 判断登录态
        names = {c['name'] for c in nc}
        has_login = 'uid' in names and 'username' in names
        print(f'登录态: {"✓ 已登录" if has_login else "✗ 未登录"}')
        # 脱敏显示关键 cookie
        for key_name in ['uid', 'username', 'NOWCODERUID', 'csrfToken', 'NOWCODERCLINETID']:
            for c in nc:
                if c['name'] == key_name:
                    v = c['value']
                    print(f'  {key_name:20} = {v[:15]}{"..." if len(v)>15 else ""}')
    finally:
        proc.terminate()
        try:
            proc.wait(timeout=5)
        except Exception:
            proc.kill()


if __name__ == '__main__':
    main()
