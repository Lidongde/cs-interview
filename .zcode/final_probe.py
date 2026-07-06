"""
最终方案：用 CDP 在浏览器里：
1. 注入 cookie
2. 用浏览器 fetch 调用 request-make-paper-pc 创建试卷（带完整 cookie）
3. 用 location.href 跳转到答题页
4. 监听答题页所有 API 请求和响应
关键：用浏览器的 fetch（自动带所有 cookie，含 HttpOnly）
"""
import os, json, time, subprocess, socket, shutil, urllib.request, websocket

os.environ['NO_PROXY'] = '127.0.0.1,localhost'
os.environ['no_proxy'] = '127.0.0.1,localhost'

LOCAL = os.environ.get('LOCALAPPDATA')
CHROME = r'C:\Program Files\Google\Chrome\Application\chrome.exe'
TMP_USER_DATA = os.path.join(LOCAL, 'Temp', 'chrome_final_probe')
DEBUG_PORT = 9233
OUTPUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'question_api_found.json')

COOKIE_STR = 'Hm_lvt_a808a1326b6c06c437de769d1b85b870=1783324773,1783326792,1783327040,1783332669; HMACCOUNT=5B50E5714BA2371A; NOWCODERCLINETID=5C624A404D820BAA561A9E407C597491; NOWCODERUID=99DB5E9FA741DBE9F474F73C04CD2DE0; acw_tc=0a18ab6c17833326692832986e66ad88590a1857ddae18de8424446dd7c7f2; isAgreementChecked=true; t=95DEC25319FA21258C369646734311BF; gr_user_id=8efaa278-603a-4231-b6df-e5959903fcdd; c196c3667d214851b11233f5c17f99d5_gr_session_id=697b7bd4-3ec7-4108-b9c0-d49935fc4cdb; c196c3667d214851b11233f5c17f99d5_gr_session_id_697b7bd4-3ec7-4108-b9c0-d49935fc4cdb=true; c196c3667d214851b11233f5c17f99d5_gr_last_sent_sid_with_cs1=697b7bd4-3ec7-4108-b9c0-d49935fc4cdb; c196c3667d214851b11233f5c17f99d5_gr_last_sent_cs1=77826278; Hm_lpvt_a808a1326b6c06c437de769d1b85b870=1783333797; c196c3667d214851b11233f5c17f99d5_gr_cs1=77826278'


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
    proc = subprocess.Popen(
        [CHROME, f'--remote-debugging-port={DEBUG_PORT}', f'--user-data-dir={TMP_USER_DATA}',
         '--no-first-run', '--no-default-browser-check', '--headless=new', '--disable-gpu',
         '--proxy-server=http://proxyhk.zte.com.cn:80', '--proxy-bypass-list=127.0.0.1;localhost',
         '--remote-allow-origins=*', 'about:blank'],
        stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    try:
        if not wait_port(DEBUG_PORT, 40): return
        print('✓ 端口就绪')

        with urllib.request.urlopen(f'http://127.0.0.1:{DEBUG_PORT}/json/version', timeout=5) as r:
            ver = json.load(r)
        browser_ws = ver['webSocketDebuggerUrl']

        # 创建 target 导航到 nowcoder 首页
        ws = websocket.create_connection(browser_ws, timeout=15, suppress_origin=False)
        ws.send(json.dumps({'id': 1, 'method': 'Target.createTarget',
                            'params': {'url': 'https://www.nowcoder.com/exam/intelligent?questionJobId=10&subTabName=intelligent_page&tagId=21003'}}))
        ws.recv()
        ws.close()
        time.sleep(8)

        with urllib.request.urlopen(f'http://127.0.0.1:{DEBUG_PORT}/json', timeout=5) as r:
            targets = json.load(r)
        pages = [t for t in targets if t.get('type') == 'page' and 'nowcoder' in t.get('url', '')]
        page_ws = pages[0]['webSocketDebuggerUrl']

        ws = websocket.create_connection(page_ws, timeout=15, suppress_origin=False)
        ws.send(json.dumps({'id': 1, 'method': 'Network.enable', 'params': {'maxTotalBufferSize': 10000000, 'maxResourceBufferSize': 5000000}}))
        ws.recv()

        # 注入 cookie（含 acw_tc，HttpOnly）
        for pair in COOKIE_STR.split('; '):
            if '=' in pair:
                name, _, val = pair.partition('=')
                ws.send(json.dumps({'id': f'c{name}', 'method': 'Network.setCookie',
                                    'params': {'name': name, 'value': val, 'domain': '.nowcoder.com', 'path': '/', 'httpOnly': name in ('acw_tc', 't')}}))
                ws.recv()
        print('  cookie 注入完成')

        # 用浏览器 fetch 创建试卷（这样自动带所有 cookie）
        create_js = """(async function() {
            const r = await fetch('https://gw-c.nowcoder.com/api/sparta/common-practice/request-make-paper-pc', {
                method: 'POST',
                credentials: 'include',
                headers: {'Content-Type': 'application/json', 'Accept': 'application/json'},
                body: JSON.stringify({"tagIdSets":["570"],"classifyName":"    ","pageType":"intelligent_page","questionJobId":10})
            });
            const data = await r.json();
            return JSON.stringify(data);
        })()"""
        ws.send(json.dumps({'id': 10, 'method': 'Runtime.evaluate',
                            'params': {'expression': create_js, 'returnByValue': True, 'awaitPromise': True, 'userGesture': True}}))
        ws.settimeout(20)
        create_result = None
        end = time.time() + 20
        while time.time() < end:
            try:
                data = ws.recv()
                msg = json.loads(data)
                if msg.get('id') == 10:
                    create_result = msg.get('result', {}).get('result', {}).get('value')
                    break
            except websocket.WebSocketTimeoutException:
                break
        if not create_result:
            print('❌ 创建试卷失败'); return

        create_data = json.loads(create_result)
        print(f'  试卷: {create_data}')
        test_id = create_data.get('data', {}).get('testId')
        paper_id = create_data.get('data', {}).get('paperId')
        question_uuid = create_data.get('data', {}).get('questionUUID')
        print(f'  testId={test_id}, paperId={paper_id}, uuid={question_uuid}')

        # 跳转到答题页
        print(f'\n跳转答题页: /exam/test?testId={test_id}')
        ws.send(json.dumps({'id': 11, 'method': 'Page.navigate',
                            'params': {'url': f'https://www.nowcoder.com/exam/test?testId={test_id}'}}))

        # 监听所有请求和响应（20 秒）
        requests_map = {}
        ws.settimeout(1)
        end_time = time.time() + 20
        while time.time() < end_time:
            try:
                data = ws.recv()
                msg = json.loads(data)
                method = msg.get('method')
                if method == 'Network.requestWillBeSent':
                    params = msg['params']
                    req = params['request']
                    requests_map[params['requestId']] = {
                        'url': req['url'], 'method': req['method'],
                        'body': req.get('postData', '')[:500]
                    }
                elif method == 'Network.responseReceived':
                    rid = msg['params']['requestId']
                    if rid in requests_map:
                        requests_map[rid]['status'] = msg['params']['response']['status']
                        requests_map[rid]['mime'] = msg['params']['response']['mimeType']
                elif method == 'Network.loadingFinished':
                    rid = msg['params']['requestId']
                    if rid in requests_map:
                        mime = requests_map[rid].get('mime', '')
                        if 'json' in mime:
                            try:
                                ws.send(json.dumps({'id': f'body_{rid}', 'method': 'Network.getResponseBody',
                                                    'params': {'requestId': rid}}))
                            except: pass
                elif method and method.startswith('Runtime'):
                    pass
                else:
                    # 可能是 getResponseBody 的响应
                    rid = None
                    if msg.get('id') and isinstance(msg['id'], str) and msg['id'].startswith('body_'):
                        rid = msg['id'][5:]
                    if rid and rid in requests_map:
                        body = msg.get('result', {}).get('body', '')
                        requests_map[rid]['response'] = body[:3000]
            except websocket.WebSocketTimeoutException:
                continue
            except:
                pass

        ws.close()

        # 过滤 API 请求
        api_reqs = [v for v in requests_map.values()
                    if 'nowcoder' in v['url'] and '/api/' in v['url']
                    and 'aliyuncs' not in v['url'] and 'baidu' not in v['url'] and 'hm.baidu' not in v['url']
                    and v.get('method') != 'OPTIONS']
        print(f'\n=== 捕获 {len(api_reqs)} 个 API 请求 ===')
        for req in api_reqs:
            url_short = req['url'].split('api/')[-1][:70] if 'api/' in req['url'] else req['url'][:70]
            status = req.get('status', '?')
            resp = req.get('response', '')[:200].replace('\n', ' ')
            print(f'\n  {req["method"]:4} {status} {url_short}')
            if resp:
                print(f'        resp: {resp}')

        # 找包含题目内容的 API
        question_apis = [r for r in api_reqs if r.get('response') and
                         any(k in r['response'].lower() for k in ['question', 'answer', 'option', 'content', '解析', '题目'])]
        if question_apis:
            print(f'\n=== ★ 找到 {len(question_apis)} 个题目相关 API ===')
            for r in question_apis:
                print(f'  {r["method"]} {r["url"][:120]}')

        with open(OUTPUT, 'w', encoding='utf-8') as f:
            json.dump(api_reqs, f, ensure_ascii=False, indent=2)
        print(f'\n保存到 {OUTPUT}')
    finally:
        try: proc.terminate(); proc.wait(timeout=5)
        except: proc.kill()


if __name__ == '__main__':
    main()
