"""
用 CDP 导航到答题页（testId=97742075），抓取所有题目内容 API
"""
import os, json, time, subprocess, socket, shutil, urllib.request, websocket

os.environ['NO_PROXY'] = '127.0.0.1,localhost'
os.environ['no_proxy'] = '127.0.0.1,localhost'

LOCAL = os.environ.get('LOCALAPPDATA')
CHROME = r'C:\Program Files\Google\Chrome\Application\chrome.exe'
TMP_USER_DATA = os.path.join(LOCAL, 'Temp', 'chrome_test_probe')
DEBUG_PORT = 9231

COOKIE_STR = 'Hm_lvt_a808a1326b6c06c437de769d1b85b870=1783324773,1783326792,1783327040,1783332669; HMACCOUNT=5B50E5714BA2371A; NOWCODERCLINETID=5C624A404D820BAA561A9E407C597491; NOWCODERUID=99DB5E9FA741DBE9F474F73C04CD2DE0; acw_tc=0a18ab6c17833326692832986e66ad88590a1857ddae18de8424446dd7c7f2; isAgreementChecked=true; t=95DEC25319FA21258C369646734311BF; gr_user_id=8efaa278-603a-4231-b6df-e5959903fcdd; c196c3667d214851b11233f5c17f99d5_gr_session_id=697b7bd4-3ec7-4108-b9c0-d49935fc4cdb; c196c3667d214851b11233f5c17f99d5_gr_session_id_697b7bd4-3ec7-4108-b9c0-d49935fc4cdb=true; c196c3667d214851b11233f5c17f99d5_gr_last_sent_sid_with_cs1=697b7bd4-3ec7-4108-b9c0-d49935fc4cdb; c196c3667d214851b11233f5c17f99d5_gr_last_sent_cs1=77826278; Hm_lpvt_a808a1326b6c06c437de769d1b85b870=1783333797; c196c3667d214851b11233f5c17f99d5_gr_cs1=77826278'

TEST_ID = 97742075


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
        with urllib.request.urlopen(f'http://127.0.0.1:{DEBUG_PORT}/json/version', timeout=5) as r:
            ver = json.load(r)
        browser_ws = ver['webSocketDebuggerUrl']

        # 尝试多个答题页 URL
        test_urls = [
            f'https://www.nowcoder.com/exam/test?testId={TEST_ID}',
            f'https://www.nowcoder.com/exam/test?id={TEST_ID}',
            f'https://www.nowcoder.com/test/{TEST_ID}',
            f'https://www.nowcoder.com/exam/intelligent/test?testId={TEST_ID}',
        ]

        for test_url in test_urls:
            print(f'\n尝试: {test_url}')
            ws = websocket.create_connection(browser_ws, timeout=15, suppress_origin=False)
            ws.send(json.dumps({'id': 1, 'method': 'Target.createTarget', 'params': {'url': test_url}}))
            ws.recv()
            ws.close()
            time.sleep(2)

            # 检查是否 404
            with urllib.request.urlopen(f'http://127.0.0.1:{DEBUG_PORT}/json', timeout=5) as r:
                targets = json.load(r)
            pages = [t for t in targets if t.get('type') == 'page' and 'nowcoder' in t.get('url', '')]
            if pages:
                page_ws = pages[-1]['webSocketDebuggerUrl']
                ws = websocket.create_connection(page_ws, timeout=10, suppress_origin=False)
                ws.send(json.dumps({'id': 1, 'method': 'Runtime.evaluate',
                                    'params': {'expression': 'JSON.stringify({url: location.href, title: document.title, is404: document.title.includes("找不到") || document.title.includes("404")})', 'returnByValue': True}}))
                ws.settimeout(5)
                try:
                    msg = json.loads(ws.recv())
                    val = msg.get('result', {}).get('result', {}).get('value', '{}')
                    info = json.loads(val)
                    print(f'  -> {info.get("title","")} | 404={info.get("is404")}')
                except: pass
                ws.close()

        # 用最可能的 URL，注入 cookie 后抓所有请求
        print('\n=== 注入 cookie 后导航答题页，抓所有 API ===')
        # 先关闭其他 page
        ws = websocket.create_connection(browser_ws, timeout=10, suppress_origin=False)
        ws.send(json.dumps({'id': 1, 'method': 'Target.createTarget', 'params': {'url': f'https://www.nowcoder.com/exam/test?testId={TEST_ID}'}}))
        ws.recv()
        ws.close()
        time.sleep(3)

        with urllib.request.urlopen(f'http://127.0.0.1:{DEBUG_PORT}/json', timeout=5) as r:
            targets = json.load(r)
        pages = [t for t in targets if t.get('type') == 'page' and 'nowcoder' in t.get('url', '')]
        if not pages:
            print('无 page'); return
        page_ws = pages[-1]['webSocketDebuggerUrl']

        ws = websocket.create_connection(page_ws, timeout=15, suppress_origin=False)
        ws.send(json.dumps({'id': 1, 'method': 'Network.enable'}))
        ws.recv()

        # 注入 cookie
        for pair in COOKIE_STR.split('; '):
            if '=' in pair:
                name, _, val = pair.partition('=')
                ws.send(json.dumps({'id': f'c{name}', 'method': 'Network.setCookie',
                                    'params': {'name': name, 'value': val, 'domain': '.nowcoder.com', 'path': '/'}}))
                ws.recv()

        # 刷新
        ws.send(json.dumps({'id': 2, 'method': 'Page.reload'}))
        time.sleep(12)

        # 收集请求
        captured = []
        ws.settimeout(1)
        try:
            while True:
                data = ws.recv()
                msg = json.loads(data)
                if msg.get('method') == 'Network.requestWillBeSent':
                    req = msg['params']['request']
                    captured.append({'url': req['url'][:300], 'method': req['method']})
        except: pass

        ws.close()

        relevant = [c for c in captured if 'nowcoder' in c['url'] and '/api/' in c['url']
                    and 'aliyuncs' not in c['url'] and 'baidu' not in c['url'] and 'hm.baidu' not in c['url']]
        print(f'\n=== 捕获 {len(relevant)} 个 API ===')
        for c in relevant:
            print(f'  {c["method"]:4} {c["url"][:150]}')

        out = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'test_page_apis.json')
        with open(out, 'w', encoding='utf-8') as f:
            json.dump(relevant, f, ensure_ascii=False, indent=2)
        print(f'\n保存到 {out}')
    finally:
        try: proc.terminate(); proc.wait(timeout=5)
        except: proc.kill()


if __name__ == '__main__':
    main()
