"""
最终方案 v2：junction 指向原 User Data（v20 key 可解密），
然后用 VSS cookie 文件覆盖 junction 里的 cookie（注入 session cookie）
关键：junction 是链接，直接覆盖会改原文件——所以先断开 junction，复制完整 User Data 到临时目录
但 User Data 太大……
变通：junction + 用 VSS cookie 覆盖（覆盖到 junction 路径=覆盖原文件，但原文件已被 Chrome 锁）
所以：先复制原 User Data 中必需的小文件到新临时目录，配合 VSS cookie
但 v20 key 绑定路径……

实际验证：v20 ABE key 是否真的绑定路径？让我测试用 junction 但覆盖 cookie
"""
import os, sys, json, time, subprocess, socket, shutil, urllib.request, websocket

os.environ['NO_PROXY'] = '127.0.0.1,localhost'
os.environ['no_proxy'] = '127.0.0.1,localhost'

LOCAL = os.environ.get('LOCALAPPDATA')
CHROME = r'C:\Program Files\Google\Chrome\Application\chrome.exe'
SRC_USER_DATA = os.path.join(LOCAL, 'Google', 'Chrome', 'User Data')
JUNCTION_USER_DATA = os.path.join(LOCAL, 'Temp', 'chrome_junction_userdata')
PROFILE = 'Default'
VSS_COOKIE_DB = os.path.join(LOCAL, 'Temp', 'chrome_cookies_vss2.db')
DEBUG_PORT = 9223
OUTPUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'nowcoder_cookies.json')


def kill_chrome_debug_only():
    subprocess.run(['powershell', '-Command',
                    "Get-Process chrome -ErrorAction SilentlyContinue | "
                    "Where-Object {(Get-CimInstance Win32_Process -Filter \"ProcessId=$($_.Id)\").CommandLine -like '*remote-debugging-port*'} | "
                    "Stop-Process -Force; Start-Sleep 1"],
                   capture_output=True)


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
    print('清理调试 Chrome...')
    kill_chrome_debug_only()

    # 删除旧 junction
    if os.path.exists(JUNCTION_USER_DATA):
        try: os.rmdir(JUNCTION_USER_DATA)
        except: subprocess.run(['cmd', '/c', 'rmdir', JUNCTION_USER_DATA], capture_output=True)

    # 创建新 junction
    r = subprocess.run(['cmd', '/c', 'mklink', '/J', JUNCTION_USER_DATA, SRC_USER_DATA],
                       capture_output=True, text=True)
    if r.returncode != 0:
        print('junction 失败:', r.stderr); return
    print('  junction ✓')

    # 覆盖 junction 里的 cookie 文件为 VSS 版本
    # 注意：junction 指向原目录，覆盖会改原文件！所以不能直接覆盖。
    # 解决：断开 junction，改为复制完整 User Data？太大。
    # 另一思路：Chrome 启动时读 cookie 文件，我们启动前用 VSS 文件覆盖 junction 的 cookie
    # 但 junction 是链接，覆盖=改原文件。原文件被运行中的 Chrome 锁定。
    # 所以：先断开 junction，创建真实目录，复制必需文件 + VSS cookie
    print('断开 junction，创建独立 profile...')
    try: os.rmdir(JUNCTION_USER_DATA)
    except: subprocess.run(['cmd', '/c', 'rmdir', JUNCTION_USER_DATA], capture_output=True)

    os.makedirs(os.path.join(JUNCTION_USER_DATA, PROFILE, 'Network'), exist_ok=True)

    # 复制 Local State（v20 key）
    shutil.copy2(os.path.join(SRC_USER_DATA, 'Local State'),
                 os.path.join(JUNCTION_USER_DATA, 'Local State'))
    # 复制 Preferences
    shutil.copy2(os.path.join(SRC_USER_DATA, PROFILE, 'Preferences'),
                 os.path.join(JUNCTION_USER_DATA, PROFILE, 'Preferences'))
    # 复制 VSS cookie（含 session cookie）
    shutil.copy2(VSS_COOKIE_DB,
                 os.path.join(JUNCTION_USER_DATA, PROFILE, 'Network', 'Cookies'))
    # 创建空的 Login Data（避免 Chrome 报错）
    open(os.path.join(JUNCTION_USER_DATA, PROFILE, 'Login Data'), 'a').close()
    print('  profile 就绪（独立目录 + VSS cookie + Local State）')

    print(f'启动 Chrome...')
    proc = subprocess.Popen(
        [CHROME,
         f'--remote-debugging-port={DEBUG_PORT}',
         f'--user-data-dir={JUNCTION_USER_DATA}',
         f'--profile-directory={PROFILE}',
         '--no-first-run', '--no-default-browser-check',
         '--headless=new', '--disable-gpu',
         '--no-proxy-server',
         '--remote-allow-origins=*',
         '--password-store=basic',
         'about:blank'],
        stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

    try:
        if not wait_port(DEBUG_PORT, 40):
            print('❌ 端口未就绪')
            proc.terminate()
            return

        print('✓ 端口就绪')

        with urllib.request.urlopen(f'http://127.0.0.1:{DEBUG_PORT}/json/version', timeout=5) as r:
            ver = json.load(r)
        browser_ws = ver['webSocketDebuggerUrl']

        # 导航到 nowcoder 触发 cookie 加载
        ws = websocket.create_connection(browser_ws, timeout=15, suppress_origin=False)
        ws.send(json.dumps({'id': 1, 'method': 'Target.createTarget',
                            'params': {'url': 'https://www.nowcoder.com'}}))
        ws.recv()
        ws.close()
        time.sleep(8)

        # 读 cookie
        ws = websocket.create_connection(browser_ws, timeout=15, suppress_origin=False)
        ws.send(json.dumps({'id': 2, 'method': 'Network.getAllCookies'}))
        resp = json.loads(ws.recv())
        ws.close()
        cookies = resp.get('result', {}).get('cookies', [])

        nc = [c for c in cookies if 'nowcoder' in c.get('domain', '')]
        print(f'✓ 共 {len(nc)} 个 nowcoder cookie')

        if nc:
            result = {
                'cookies': nc,
                'cookie_string': '; '.join(f"{c['name']}={c['value']}" for c in nc),
            }
            with open(OUTPUT, 'w', encoding='utf-8') as f:
                json.dump(result, f, ensure_ascii=False, indent=2)
            names = {c['name'] for c in nc}
            print(f'  cookie 名: {sorted(names)}')
            print(f'  登录态: {"✓ 已登录" if "uid" in names else "✗ 无 uid"}')
            for key_name in ['uid', 'username', 'NOWCODERUID', 'csrfToken']:
                for c in nc:
                    if c['name'] == key_name:
                        print(f'    {key_name} = {c["value"][:25]}')
        else:
            print('  ❌ 无 cookie（v20 解密可能失败）')
            # 检查 Chrome stderr
            proc.terminate()
            try:
                out, err = proc.communicate(timeout=3)
                errstr = err.decode('utf-8', errors='replace')
                if 'cookie' in errstr.lower() or 'decrypt' in errstr.lower():
                    print(f'  Chrome stderr: {errstr[:300]}')
            except:
                pass
    finally:
        try:
            proc.terminate()
            proc.wait(timeout=5)
        except:
            proc.kill()


if __name__ == '__main__':
    main()
