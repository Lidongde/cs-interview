"""
找 appStore.setUserInfo 是从哪个 API 获取的
并直接调用可能的 user-info API
"""
import os, json, time, subprocess, socket, shutil, urllib.request, websocket

os.environ['NO_PROXY'] = '127.0.0.1,localhost'
os.environ['no_proxy'] = '127.0.0.1,localhost'

LOCAL = os.environ.get('LOCALAPPDATA')
CHROME = r'C:\Program Files\Google\Chrome\Application\chrome.exe'
TMP_USER_DATA = os.path.join(LOCAL, 'Temp', 'chrome_api_probe4')
DEBUG_PORT = 9229

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
        ws = websocket.create_connection(browser_ws, timeout=15, suppress_origin=False)
        ws.send(json.dumps({'id': 1, 'method': 'Target.createTarget',
                            'params': {'url': 'https://www.nowcoder.com/exam/intelligent?questionJobId=10&subTabName=intelligent_page&tagId=21003'}}))
        ws.recv()
        ws.close()
        time.sleep(8)
        with urllib.request.urlopen(f'http://127.0.0.1:{DEBUG_PORT}/json', timeout=5) as r:
            targets = json.load(r)
        pages = [t for t in targets if t.get('type') == 'page' and 'nowcoder' in t.get('url', '')]
        ws = websocket.create_connection(pages[0]['webSocketDebuggerUrl'], timeout=15, suppress_origin=False)
        ws.send(json.dumps({'id': 1, 'method': 'Network.enable'}))
        ws.recv()
        for pair in COOKIE_STR.split('; '):
            if '=' in pair:
                name, _, val = pair.partition('=')
                ws.send(json.dumps({'id': f'c{name}', 'method': 'Network.setCookie',
                                    'params': {'name': name, 'value': val, 'domain': '.nowcoder.com', 'path': '/'}}))
                ws.recv()

        # 注入 cookie 后，直接在浏览器里用 fetch 调用各种 user-info API
        # 牛客的登录态 API 通常返回用户信息
        test_js = """(async function() {
            const apis = [
                'https://gw-c.nowcoder.com/api/sparta/account/user-info',
                'https://gw-c.nowcoder.com/api/sparta/user/info',
                'https://gw-c.nowcoder.com/api/sparta/user-info',
                'https://gw-c.nowcoder.com/api/sparta/account/info',
                'https://gw-c.nowcoder.com/api/sparta/exam/exam-paper/create',
                'https://www.nowcoder.com/api/questiontraining/intelligent/practiceHistory?subTabName=intelligent_page&questionJobId=10',
                'https://gw-c.nowcoder.com/api/sparta/question-tab/query-all-tab-list',
            ];
            const results = [];
            for (const url of apis) {
                try {
                    const r = await fetch(url, {credentials: 'include', headers: {'Accept':'application/json'}});
                    const text = await r.text();
                    results.push({url: url.split('api/')[1] || url, status: r.status, body: text.slice(0, 250)});
                } catch(e) {
                    results.push({url: url.split('api/')[1] || url, error: e.message});
                }
            }
            return JSON.stringify(results);
        })()"""
        ws.send(json.dumps({'id': 10, 'method': 'Runtime.evaluate',
                            'params': {'expression': test_js, 'returnByValue': True, 'awaitPromise': True, 'userGesture': True}}))
        ws.settimeout(30)
        result = None
        end = time.time() + 30
        while time.time() < end:
            try:
                data = ws.recv()
                msg = json.loads(data)
                if msg.get('id') == 10:
                    result = msg.get('result', {}).get('result', {}).get('value')
                    break
            except websocket.WebSocketTimeoutException:
                break
        ws.close()

        if result:
            results = json.loads(result)
            print('=== API 测试结果 ===')
            for r in results:
                print(f'\n{r.get("url","")}')
                if r.get('status'):
                    print(f'  status: {r["status"]}')
                    print(f'  body: {r.get("body","")[:200]}')
                else:
                    print(f'  error: {r.get("error")}')
        else:
            print('无结果（超时）')
    finally:
        try: proc.terminate(); proc.wait(timeout=5)
        except: proc.kill()


if __name__ == '__main__':
    main()
