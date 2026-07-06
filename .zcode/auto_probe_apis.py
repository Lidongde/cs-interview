"""
自动抓取题目内容 API：
1. 注入 cookie
2. 在浏览器内调用 request-make-paper-pc 创建试卷
3. 拿到 testId 后跳转答题页
4. 监听所有 Network 响应，找出包含题目内容的 API
"""
import os, json, time, subprocess, socket, shutil, urllib.request, websocket

os.environ['NO_PROXY'] = '127.0.0.1,localhost'
os.environ['no_proxy'] = '127.0.0.1,localhost'

LOCAL = os.environ.get('LOCALAPPDATA')
CHROME = r'C:\Program Files\Google\Chrome\Application\chrome.exe'
TMP_USER_DATA = os.path.join(LOCAL, 'Temp', 'chrome_auto_probe')
DEBUG_PORT = 9232

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
        if not wait_port(DEBUG_PORT, 40):
            print('❌ 端口未就绪'); return
        print('✓ 端口就绪')

        with urllib.request.urlopen(f'http://127.0.0.1:{DEBUG_PORT}/json/version', timeout=5) as r:
            ver = json.load(r)
        browser_ws = ver['webSocketDebuggerUrl']

        # 创建 target 导航到答题页（直接用 testId）
        ws = websocket.create_connection(browser_ws, timeout=15, suppress_origin=False)
        ws.send(json.dumps({'id': 1, 'method': 'Target.createTarget',
                            'params': {'url': 'https://www.nowcoder.com/exam/test?testId=97742075'}}))
        resp = json.loads(ws.recv())
        target_id = resp.get('result', {}).get('targetId', '')
        ws.close()
        time.sleep(6)

        with urllib.request.urlopen(f'http://127.0.0.1:{DEBUG_PORT}/json', timeout=5) as r:
            targets = json.load(r)
        pages = [t for t in targets if t.get('type') == 'page' and 'nowcoder' in t.get('url', '')]
        if not pages:
            print('❌ 无 page'); return
        page_ws = pages[0]['webSocketDebuggerUrl']

        ws = websocket.create_connection(page_ws, timeout=15, suppress_origin=False)
        # 启用 Network（含 response body）
        ws.send(json.dumps({'id': 1, 'method': 'Network.enable', 'params': {'maxTotalBufferSize': 10000000, 'maxResourceBufferSize': 5000000}}))
        ws.recv()

        # 注入 cookie
        for pair in COOKIE_STR.split('; '):
            if '=' in pair:
                name, _, val = pair.partition('=')
                ws.send(json.dumps({'id': f'c{name}', 'method': 'Network.setCookie',
                                    'params': {'name': name, 'value': val, 'domain': '.nowcoder.com', 'path': '/'}}))
                ws.recv()
        print('  cookie 注入完成')

        # 刷新页面
        ws.send(json.dumps({'id': 2, 'method': 'Page.reload'}))
        print('  刷新页面，监听所有请求和响应...')

        # 收集请求和响应（15 秒）
        requests_map = {}  # requestId -> {url, method, response body}
        ws.settimeout(1)
        end_time = time.time() + 15
        while time.time() < end_time:
            try:
                data = ws.recv()
                msg = json.loads(data)
                method = msg.get('method')
                if method == 'Network.requestWillBeSent':
                    params = msg['params']
                    req = params['request']
                    requests_map[params['requestId']] = {
                        'url': req['url'],
                        'method': req['method'],
                        'body': req.get('postData', '')
                    }
                elif method == 'Network.responseReceived':
                    params = msg['params']
                    rid = params['requestId']
                    if rid in requests_map:
                        requests_map[rid]['status'] = params['response']['status']
                        requests_map[rid]['mime'] = params['response']['mimeType']
                elif method == 'Network.loadingFinished':
                    rid = msg['params']['requestId']
                    if rid in requests_map and requests_map[rid].get('mime', '').startswith(('application/json', 'text/')):
                        # 获取 response body
                        try:
                            ws2 = websocket.create_connection(page_ws, timeout=5, suppress_origin=False)
                            ws2.send(json.dumps({'id': 'getbody', 'method': 'Network.getResponseBody',
                                                 'params': {'requestId': rid}}))
                            ws2.settimeout(3)
                            try:
                                bmsg = json.loads(ws2.recv())
                                body = bmsg.get('result', {}).get('body', '')
                                requests_map[rid]['response'] = body[:2000]
                            except: pass
                            ws2.close()
                        except: pass
            except websocket.WebSocketTimeoutException:
                continue
            except:
                break

        ws.close()

        # 过滤出 nowcoder API 请求
        api_reqs = {k: v for k, v in requests_map.items()
                    if 'nowcoder' in v['url'] and '/api/' in v['url']
                    and 'aliyuncs' not in v['url'] and 'baidu' not in v['url']}
        print(f'\n=== 捕获 {len(api_reqs)} 个 API 请求（含响应）===')
        for rid, req in api_reqs.items():
            url_short = req['url'].split('api/')[-1][:70] if 'api/' in req['url'] else req['url'][:70]
            status = req.get('status', '?')
            print(f'\n  {req["method"]:4} {status} {url_short}')
            if req.get('response'):
                resp_preview = req['response'][:300].replace('\n', ' ')
                print(f'        resp: {resp_preview}')

        # 保存完整数据
        out = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'test_page_full_apis.json')
        with open(out, 'w', encoding='utf-8') as f:
            json.dump(list(api_reqs.values()), f, ensure_ascii=False, indent=2)
        print(f'\n保存到 {out}')

    finally:
        try: proc.terminate(); proc.wait(timeout=5)
        except: proc.kill()


if __name__ == '__main__':
    main()
