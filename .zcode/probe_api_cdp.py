"""
用 CDP 启动独立 Chrome，注入 cookie，导航到答题页，点击 Java 卡片，抓真实 API
"""
import os, sys, json, time, subprocess, socket, urllib.request, websocket

os.environ['NO_PROXY'] = '127.0.0.1,localhost'
os.environ['no_proxy'] = '127.0.0.1,localhost'

LOCAL = os.environ.get('LOCALAPPDATA')
CHROME = r'C:\Program Files\Google\Chrome\Application\chrome.exe'
TMP_USER_DATA = os.path.join(LOCAL, 'Temp', 'chrome_api_probe')
DEBUG_PORT = 9226
OUTPUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'nowcoder_apis.json')

COOKIE_STR = '__snaker__id=utDTAd7ObV8JQt1f; csrfToken=DUZhF38yZz3Vs1nt5QM-HiNw; Hm_lvt_a808a1326b6c06c437de769d1b85b870=1783324773,1783326792,1783327040,1783332669; HMACCOUNT=5B50E5714BA2371A; NOWCODERCLINETID=5C624A404D820BAA561A9E407C597491; NOWCODERUID=99DB5E9FA741DBE9F474F73C04CD2DE0; gdxidpyhxdE=%2FMO7viLNXdURbVemEdWJJRubPsGhPhQ0g9j%2FDNSzck4%5CmcZYz52vsn1E%5CzTRH9q9%2Fl88wg9AkgbNCBvN90Xup%2B62NB%5CbC%2Bo94nsyiWgZ%5CJtquJXwfLret87GHns4Wd0CuYT%5C66q8AtrIvLRjnPqbciVHRPHu2tYmogl1G394y%2BijkCrB%3A1783333579090; isAgreementChecked=true; t=95DEC25319FA21258C369646734311BF; SERVERID=65f227749e96649c85a683aa7ef45343|1783332696|1783332666; SERVERCORSID=65f227749e96649c85a683aa7ef45343|1783332696|1783332666; gr_user_id=8efaa278-603a-4231-b6df-e5959903fcdd; c196c3667d214851b11233f5c17f99d5_gr_session_id=697b7bd4-3ec7-4108-b9c0-d49935fc4cdb; c196c3667d214851b11233f5c17f99d5_gr_session_id_697b7bd4-3ec7-4108-b9c0-d49935fc4cdb=true; c196c3667d214851b11233f5c17f99d5_gr_last_sent_sid_with_cs1=697b7bd4-3ec7-4108-b9c0-d49935fc4cdb; c196c3667d214851b11233f5c17f99d5_gr_last_sent_cs1=77826278; c196c3667d214851b11233f5c17f99d5_gr_cs1=77826278; Hm_lpvt_a808a1326b6c06c437de769d1b85b870=1783332697'


def wait_port(port, timeout=40):
    end = time.time() + timeout
    while time.time() < end:
        try:
            with socket.create_connection(('127.0.0.1', port), timeout=1):
                return True
        except OSError:
            time.sleep(0.5)
    return False


def parse_cookies(cookie_str, domain='.nowcoder.com'):
    cookies = []
    for pair in cookie_str.split('; '):
        if '=' in pair:
            name, _, val = pair.partition('=')
            cookies.append({
                'name': name, 'value': val,
                'domain': domain, 'path': '/',
            })
    return cookies


def main():
    # 清理
    import shutil
    if os.path.exists(TMP_USER_DATA):
        shutil.rmtree(TMP_USER_DATA, ignore_errors=True)

    print('启动独立 Chrome...')
    proc = subprocess.Popen(
        [CHROME,
         f'--remote-debugging-port={DEBUG_PORT}',
         f'--user-data-dir={TMP_USER_DATA}',
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

        # 创建 target 导航到 nowcoder
        ws = websocket.create_connection(browser_ws, timeout=15, suppress_origin=False)
        ws.send(json.dumps({'id': 1, 'method': 'Target.createTarget',
                            'params': {'url': 'https://www.nowcoder.com/exam/intelligent?questionJobId=10&subTabName=intelligent_page&tagId=21003'}}))
        resp = json.loads(ws.recv())
        target_id = resp.get('result', {}).get('targetId', '')
        print(f'  target: {target_id}')
        ws.close()

        time.sleep(8)

        # 找 page target
        with urllib.request.urlopen(f'http://127.0.0.1:{DEBUG_PORT}/json', timeout=5) as r:
            targets = json.load(r)
        pages = [t for t in targets if t.get('type') == 'page' and 'nowcoder' in t.get('url', '')]
        if not pages:
            print('❌ 无 page target'); return

        page_ws_url = pages[0]['webSocketDebuggerUrl']

        # 注入 cookie
        ws = websocket.create_connection(page_ws_url, timeout=15, suppress_origin=False)
        ws.send(json.dumps({'id': 1, 'method': 'Network.enable'}))
        ws.recv()

        cookies = parse_cookies(COOKIE_STR)
        for c in cookies:
            ws.send(json.dumps({'id': 'set', 'method': 'Network.setCookie',
                                'params': {
                                    'name': c['name'], 'value': c['value'],
                                    'domain': '.nowcoder.com', 'path': '/',
                                }}))
            ws.recv()
        print(f'  注入 {len(cookies)} 个 cookie')

        # 安装 fetch hook
        hook_js = """
        window.__apiCalls = [];
        const origFetch = window.fetch;
        window.fetch = function(...args) {
            const url = typeof args[0] === 'string' ? args[0] : (args[0] && args[0].url);
            const method = (args[1] && args[1].method) || 'GET';
            const body = (args[1] && args[1].body) || '';
            window.__apiCalls.push({url: url ? url.slice(0, 400) : '', method, body: typeof body === 'string' ? body.slice(0, 300) : ''});
            return origFetch.apply(this, args);
        };
        const origOpen = XMLHttpRequest.prototype.open;
        const origSend = XMLHttpRequest.prototype.send;
        XMLHttpRequest.prototype.open = function(method, url) {
            this.__nc_m = method; this.__nc_u = url;
            return origOpen.apply(this, arguments);
        };
        XMLHttpRequest.prototype.send = function(body) {
            window.__apiCalls.push({url: (this.__nc_u||'').slice(0,400), method: this.__nc_m||'GET', body: typeof body === 'string' ? body.slice(0,300) : '', type: 'xhr'});
            return origSend.apply(this, arguments);
        };
        'hooks installed'
        """
        ws.send(json.dumps({'id': 2, 'method': 'Runtime.evaluate',
                            'params': {'expression': hook_js, 'returnByValue': True}}))
        resp = json.loads(ws.recv())
        print(f'  hook: {resp.get("result", {}).get("result", {}).get("value")}')

        # 刷新页面让 cookie 生效
        ws.send(json.dumps({'id': 3, 'method': 'Page.reload'}))
        time.sleep(8)

        # 重新安装 hook（刷新后丢失）
        ws.send(json.dumps({'id': 4, 'method': 'Runtime.evaluate',
                            'params': {'expression': hook_js, 'returnByValue': True}}))
        ws.recv()

        # 检查登录态
        ws.send(json.dumps({'id': 5, 'method': 'Runtime.evaluate',
                            'params': {'expression': "document.querySelector('.exercise-card') ? 'has cards' : 'no cards'", 'returnByValue': True}}))
        resp = json.loads(ws.recv())
        print(f'  页面状态: {resp.get("result", {}).get("result", {}).get("value")}')

        # 点击 Java 卡片（调用 startPractice）
        click_js = """
        (function() {
            const card = document.querySelector('.exercise-card');
            if (!card || !card.__vue__) return 'no vue card';
            const indexComp = card.__vue__.$parent.$parent.$parent;
            try {
                const r = indexComp.startPractice(570);
                return 'called startPractice(570), isPromise=' + (r && typeof r.then === 'function');
            } catch(e) { return 'error: ' + e.message; }
        })()
        """
        ws.send(json.dumps({'id': 6, 'method': 'Runtime.evaluate',
                            'params': {'expression': click_js, 'returnByValue': True, 'awaitPromise': False}}))
        resp = json.loads(ws.recv())
        print(f'  startPractice: {resp.get("result", {}).get("result", {}).get("value")}')

        # 等待 API 调用
        time.sleep(8)

        # 读取捕获的 API
        ws.send(json.dumps({'id': 7, 'method': 'Runtime.evaluate',
                            'params': {'expression': 'JSON.stringify(window.__apiCalls || [])', 'returnByValue': True}}))
        # 收集响应
        calls_str = '[]'
        end = time.time() + 10
        while time.time() < end:
            try:
                data = ws.recv()
                msg = json.loads(data)
                if msg.get('id') == 7:
                    calls_str = msg.get('result', {}).get('result', {}).get('value', '[]')
                    break
            except websocket.WebSocketTimeoutException:
                break
            except:
                pass

        ws.close()

        calls = json.loads(calls_str)
        relevant = [c for c in calls if 'nowcoder' in c.get('url', '')
                    and 'aliyuncs' not in c.get('url', '')
                    and 'baidu' not in c.get('url', '')
                    and 'hm.baidu' not in c.get('url', '')
                    and 'qr-code' not in c.get('url', '')]
        print(f'\n=== 捕获 {len(relevant)} 个相关 API ===')
        for c in relevant:
            print(f'  {c.get("method","?"):4} {c.get("url","")[:150]}')
            if c.get('body'):
                print(f'        body: {c["body"][:150]}')

        with open(OUTPUT, 'w', encoding='utf-8') as f:
            json.dump(relevant, f, ensure_ascii=False, indent=2)
        print(f'\n保存到 {OUTPUT}')

    finally:
        try:
            proc.terminate()
            proc.wait(timeout=5)
        except:
            proc.kill()


if __name__ == '__main__':
    main()
