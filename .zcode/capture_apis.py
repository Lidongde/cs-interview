"""
用 junction Chrome（带 cookie）导航到答题页，捕获真实的题目 API
"""
import os, sys, json, time, subprocess, socket, urllib.request, websocket

os.environ['NO_PROXY'] = '127.0.0.1,localhost'
os.environ['no_proxy'] = '127.0.0.1,localhost'

LOCAL = os.environ.get('LOCALAPPDATA')
CHROME = r'C:\Program Files\Google\Chrome\Application\chrome.exe'
SRC_USER_DATA = os.path.join(LOCAL, 'Google', 'Chrome', 'User Data')
JUNCTION_USER_DATA = os.path.join(LOCAL, 'Temp', 'chrome_junction_userdata')
PROFILE = 'Default'
DEBUG_PORT = 9223
OUTPUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'nowcoder_apis.json')


def kill_chrome():
    subprocess.run(['powershell', '-Command',
                    'Stop-Process -Name chrome -Force -ErrorAction SilentlyContinue; Start-Sleep 2'],
                   capture_output=True)
    for lockname in ['SingletonLock', 'SingletonCookie', 'SingletonSocket']:
        for d in [os.path.join(SRC_USER_DATA, PROFILE), SRC_USER_DATA]:
            try: os.remove(os.path.join(d, lockname))
            except OSError: pass


def create_junction():
    if os.path.exists(JUNCTION_USER_DATA):
        try: os.rmdir(JUNCTION_USER_DATA)
        except: subprocess.run(['cmd', '/c', 'rmdir', JUNCTION_USER_DATA], capture_output=True)
    r = subprocess.run(['cmd', '/c', 'mklink', '/J', JUNCTION_USER_DATA, SRC_USER_DATA],
                       capture_output=True, text=True)
    return r.returncode == 0


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
    print('清理 Chrome...')
    kill_chrome()
    print('创建 junction...')
    if not create_junction():
        print('junction 失败'); return

    print('启动 Chrome...')
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

        # 获取 browser ws
        with urllib.request.urlopen(f'http://127.0.0.1:{DEBUG_PORT}/json/version', timeout=5) as r:
            ver = json.load(r)
        browser_ws = ver['webSocketDebuggerUrl']

        # 创建 target 导航到答题页
        ws = websocket.create_connection(browser_ws, timeout=15, suppress_origin=False)
        ws.send(json.dumps({'id': 1, 'method': 'Target.createTarget',
                            'params': {'url': 'https://www.nowcoder.com/exam/intelligent?questionJobId=10&subTabName=intelligent_page&tagId=21003'}}))
        resp = json.loads(ws.recv())
        target_id = resp.get('result', {}).get('targetId', '')
        print(f'  target: {target_id}')
        ws.close()

        # 等待页面加载
        print('等待页面加载...')
        time.sleep(10)

        # 找到 page target 的 ws
        with urllib.request.urlopen(f'http://127.0.0.1:{DEBUG_PORT}/json', timeout=5) as r:
            targets = json.load(r)
        pages = [t for t in targets if t.get('type') == 'page' and 'nowcoder' in t.get('url', '')]
        if not pages:
            print('❌ 没有 nowcoder page target')
            print('所有 targets:', [t.get('url') for t in targets])
            return

        page_ws_url = pages[0]['webSocketDebuggerUrl']
        print(f'  page ws: {page_ws_url[:60]}...')

        # 启用 Network
        ws = websocket.create_connection(page_ws_url, timeout=15, suppress_origin=False)
        ws.send(json.dumps({'id': 1, 'method': 'Network.enable'}))
        ws.recv()

        # 在页面里执行 JS：安装 fetch hook，然后点击 Java 卡片
        hook_js = """
        window.__apiCalls = [];
        const origFetch = window.fetch;
        window.fetch = function(...args) {
            const url = typeof args[0] === 'string' ? args[0] : (args[0] && args[0].url);
            const method = (args[1] && args[1].method) || 'GET';
            window.__apiCalls.push({url: url ? url.slice(0, 300) : '', method});
            return origFetch.apply(this, args);
        };
        const origOpen = XMLHttpRequest.prototype.open;
        XMLHttpRequest.prototype.open = function(method, url) {
            window.__apiCalls.push({url: (url||'').slice(0, 300), method, type: 'xhr'});
            return origOpen.apply(this, arguments);
        };
        'hooks installed'
        """
        ws.send(json.dumps({'id': 2, 'method': 'Runtime.evaluate',
                            'params': {'expression': hook_js, 'returnByValue': True}}))
        resp = json.loads(ws.recv())
        print(f'  hook: {resp.get("result", {}).get("result", {}).get("value")}')

        # 点击 Java 卡片（通过 Vue 调用 startPractice）
        click_js = """
        (function() {
            const card = document.querySelector('.exercise-card');
            if (!card || !card.__vue__) return 'no vue card';
            const indexComp = card.__vue__.$parent.$parent.$parent;
            try {
                const r = indexComp.startPractice(570);
                return 'called startPractice, isPromise=' + (r && typeof r.then === 'function');
            } catch(e) { return 'error: ' + e.message; }
        })()
        """
        ws.send(json.dumps({'id': 3, 'method': 'Runtime.evaluate',
                            'params': {'expression': click_js, 'returnByValue': True, 'awaitPromise': True}}))
        # 可能需要等 promise
        deadline = time.time() + 15
        resp = None
        while time.time() < deadline:
            try:
                data = ws.recv()
                msg = json.loads(data)
                if msg.get('id') == 3:
                    resp = msg
                    break
            except Exception:
                break
        print(f'  startPractice: {resp.get("result", {}).get("result", {}).get("value") if resp else "timeout"}')

        # 等待 API 调用
        time.sleep(5)

        # 读取捕获的 API 调用
        ws.send(json.dumps({'id': 4, 'method': 'Runtime.evaluate',
                            'params': {'expression': 'JSON.stringify(window.__apiCalls || [])', 'returnByValue': True}}))
        deadline = time.time() + 10
        resp = None
        while time.time() < deadline:
            data = ws.recv()
            msg = json.loads(data)
            if msg.get('id') == 4:
                resp = msg
                break
        if resp:
            calls_str = resp.get('result', {}).get('result', {}).get('value', '[]')
            calls = json.loads(calls_str)
            # 过滤无关请求
            relevant = [c for c in calls if 'nowcoder' in c.get('url', '') and 'aliyuncs' not in c.get('url', '') and 'baidu' not in c.get('url', '') and 'hm.baidu' not in c.get('url', '')]
            print(f'\n=== 捕获 {len(relevant)} 个相关 API 调用 ===')
            for c in relevant:
                print(f'  {c.get("method","?"):4} {c.get("url","")[:120]}')
            # 保存
            with open(OUTPUT, 'w', encoding='utf-8') as f:
                json.dump(relevant, f, ensure_ascii=False, indent=2)
            print(f'\n保存到 {OUTPUT}')

        # 也读当前 cookie（确认登录态）
        ws.send(json.dumps({'id': 5, 'method': 'Network.getAllCookies'}))
        deadline = time.time() + 10
        while time.time() < deadline:
            data = ws.recv()
            msg = json.loads(data)
            if msg.get('id') == 5:
                cookies = msg.get('result', {}).get('cookies', [])
                nc = [c for c in cookies if 'nowcoder' in c.get('domain', '')]
                names = [c['name'] for c in nc]
                print(f'\n当前 cookie ({len(nc)}): {names}')
                has_login = 'uid' in names
                print(f'登录态: {"✓" if has_login else "✗"}')
                # 保存完整 cookie
                with open(os.path.join(os.path.dirname(OUTPUT), 'nowcoder_cookies.json'), 'w', encoding='utf-8') as f:
                    json.dump({'cookies': nc,
                               'cookie_string': '; '.join(f"{c['name']}={c['value']}" for c in nc)},
                              f, ensure_ascii=False, indent=2)
                break
        ws.close()

    finally:
        try:
            proc.terminate()
            proc.wait(timeout=5)
        except:
            proc.kill()
        try: os.rmdir(JUNCTION_USER_DATA)
        except: subprocess.run(['cmd', '/c', 'rmdir', JUNCTION_USER_DATA], capture_output=True)


if __name__ == '__main__':
    main()
