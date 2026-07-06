"""
v2: 用 CDP Network.requestWillBeSent 事件监听所有网络请求（最可靠）
注入 cookie 后刷新页面，点击 Java 卡片，捕获所有 sparta API
"""
import os, sys, json, time, subprocess, socket, shutil, urllib.request, websocket
import threading

os.environ['NO_PROXY'] = '127.0.0.1,localhost'
os.environ['no_proxy'] = '127.0.0.1,localhost'

LOCAL = os.environ.get('LOCALAPPDATA')
CHROME = r'C:\Program Files\Google\Chrome\Application\chrome.exe'
TMP_USER_DATA = os.path.join(LOCAL, 'Temp', 'chrome_api_probe2')
DEBUG_PORT = 9227
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


def main():
    if os.path.exists(TMP_USER_DATA):
        shutil.rmtree(TMP_USER_DATA, ignore_errors=True)

    print('启动 Chrome...')
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

        # 创建 target
        ws = websocket.create_connection(browser_ws, timeout=15, suppress_origin=False)
        ws.send(json.dumps({'id': 1, 'method': 'Target.createTarget',
                            'params': {'url': 'https://www.nowcoder.com/exam/intelligent?questionJobId=10&subTabName=intelligent_page&tagId=21003'}}))
        resp = json.loads(ws.recv())
        target_id = resp.get('result', {}).get('targetId', '')
        ws.close()
        time.sleep(6)

        # 找 page target
        with urllib.request.urlopen(f'http://127.0.0.1:{DEBUG_PORT}/json', timeout=5) as r:
            targets = json.load(r)
        pages = [t for t in targets if t.get('type') == 'page' and 'nowcoder' in t.get('url', '')]
        if not pages:
            print('❌ 无 page'); return
        page_ws_url = pages[0]['webSocketDebuggerUrl']
        print(f'  page ws 就绪')

        # 注入 cookie
        ws = websocket.create_connection(page_ws_url, timeout=15, suppress_origin=False)
        ws.send(json.dumps({'id': 1, 'method': 'Network.enable'}))
        ws.recv()
        for pair in COOKIE_STR.split('; '):
            if '=' in pair:
                name, _, val = pair.partition('=')
                ws.send(json.dumps({'id': f'c{name}', 'method': 'Network.setCookie',
                                    'params': {'name': name, 'value': val, 'domain': '.nowcoder.com', 'path': '/'}}))
                ws.recv()
        print('  cookie 注入完成')

        # 用后台线程收集所有 Network.requestWillBeSent 事件
        captured = []
        ws.settimeout(1)

        # 先刷新页面（带 cookie）
        ws.send(json.dumps({'id': 2, 'method': 'Page.reload'}))
        print('  刷新页面...')
        time.sleep(12)

        # 收集刷新期间的请求
        try:
            while True:
                data = ws.recv()
                msg = json.loads(data)
                if msg.get('method') == 'Network.requestWillBeSent':
                    req = msg['params']['request']
                    captured.append({'url': req['url'][:400], 'method': req['method'], 'body': req.get('postData', '')[:300]})
        except websocket.WebSocketTimeoutException:
            pass
        except:
            pass

        print(f'  刷新期间捕获 {len(captured)} 个请求')

        # 点击 Java 卡片
        click_js = """(function() {
            const cards = document.querySelectorAll('.exercise-card');
            let target = null;
            for (const c of cards) {
                const v = c.__vue__;
                if (v && v.cardInfo && v.cardInfo.title === 'Java') { target = c; break; }
            }
            if (!target) return 'Java card not found, count=' + cards.length;
            const indexComp = target.__vue__.$parent.$parent.$parent;
            try {
                const r = indexComp.startPractice(570);
                return 'called startPractice(570)';
            } catch(e) { return 'error: ' + e.message; }
        })()"""
        ws.send(json.dumps({'id': 3, 'method': 'Runtime.evaluate',
                            'params': {'expression': click_js, 'returnByValue': True}}))

        # 收集点击后的请求（等 10 秒）
        time.sleep(10)
        try:
            while True:
                data = ws.recv()
                msg = json.loads(data)
                if msg.get('method') == 'Network.requestWillBeSent':
                    req = msg['params']['request']
                    captured.append({'url': req['url'][:400], 'method': req['method'], 'body': req.get('postData', '')[:300]})
                elif msg.get('id') == 3:
                    print(f'  click 结果: {msg.get("result", {}).get("result", {}).get("value")}')
        except websocket.WebSocketTimeoutException:
            pass
        except:
            pass

        ws.close()

        # 过滤相关请求
        relevant = [c for c in captured
                    if 'nowcoder' in c['url']
                    and 'aliyuncs' not in c['url']
                    and 'baidu' not in c['url']
                    and 'hm.baidu' not in c['url']
                    and 'qr-code' not in c['url']
                    and '/api/' in c['url']]
        print(f'\n=== 捕获 {len(relevant)} 个 nowcoder API 请求 ===')
        for c in relevant:
            print(f'  {c["method"]:4} {c["url"][:150]}')
            if c['body']:
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
