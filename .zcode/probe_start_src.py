"""
v3: 抓 startPractice 调用的 API + 抓所有 API 的响应内容
关键：用 Runtime.evaluate 直接读 startPractice 的源码
"""
import os, sys, json, time, subprocess, socket, shutil, urllib.request, websocket

os.environ['NO_PROXY'] = '127.0.0.1,localhost'
os.environ['no_proxy'] = '127.0.0.1,localhost'

LOCAL = os.environ.get('LOCALAPPDATA')
CHROME = r'C:\Program Files\Google\Chrome\Application\chrome.exe'
TMP_USER_DATA = os.path.join(LOCAL, 'Temp', 'chrome_api_probe3')
DEBUG_PORT = 9228

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
        if not wait_port(DEBUG_PORT, 40):
            print('❌'); return

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
        page_ws_url = pages[0]['webSocketDebuggerUrl']

        ws = websocket.create_connection(page_ws_url, timeout=15, suppress_origin=False)
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
        # 清空之前的请求
        ws.settimeout(1)
        try:
            while True: ws.recv()
        except: pass

        # 读 startPractice 源码 + appStore userInfo
        src_js = """(function() {
            const card = document.querySelector('.exercise-card');
            if (!card || !card.__vue__) return 'no vue';
            const indexComp = card.__vue__.$parent.$parent.$parent;
            // startPractice 真实源码
            const sp = indexComp.$options.methods.startPractice;
            const spSrc = sp.toString();
            // 检查 appStore 的 userInfo
            const appStore = indexComp.appStore;
            const userInfo = appStore ? appStore.userInfo : null;
            // 检查 examStore
            const examStore = indexComp.examStore;
            return JSON.stringify({
                startPracticeSrc: spSrc.slice(0, 1500),
                userInfo: userInfo,
                isLogin: appStore ? appStore.isLogin : null,
                currentSwitch: examStore ? examStore.currentSwitch : null
            });
        })()"""
        ws.settimeout(15)
        ws.send(json.dumps({'id': 10, 'method': 'Runtime.evaluate',
                            'params': {'expression': src_js, 'returnByValue': True}}))

        result = None
        end = time.time() + 15
        while time.time() < end:
            try:
                data = ws.recv()
                msg = json.loads(data)
                if msg.get('id') == 10:
                    result = msg.get('result', {}).get('result', {}).get('value')
                    break
            except websocket.WebSocketTimeoutException:
                break

        if result:
            d = json.loads(result)
            print('=== startPractice 源码 ===')
            print(d.get('startPracticeSrc', '')[:1200])
            print(f'\n=== userInfo ===')
            print(json.dumps(d.get('userInfo'), ensure_ascii=False, indent=2)[:300])
            print(f'isLogin: {d.get("isLogin")}')
            print(f'currentSwitch: {d.get("currentSwitch")}')

        ws.close()
    finally:
        try:
            proc.terminate(); proc.wait(timeout=5)
        except: proc.kill()


if __name__ == '__main__':
    main()
