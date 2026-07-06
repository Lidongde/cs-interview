"""
诊断：独立目录 + VSS cookie + Local State，启用日志看 Chrome 是否解密 cookie
"""
import os, sys, json, time, subprocess, socket, shutil, urllib.request, websocket

os.environ['NO_PROXY'] = '127.0.0.1,localhost'
os.environ['no_proxy'] = '127.0.0.1,localhost'

LOCAL = os.environ.get('LOCALAPPDATA')
CHROME = r'C:\Program Files\Google\Chrome\Application\chrome.exe'
SRC_USER_DATA = os.path.join(LOCAL, 'Google', 'Chrome', 'User Data')
TMP_USER_DATA = os.path.join(LOCAL, 'Temp', 'chrome_diag_profile')
PROFILE = 'Default'
VSS_COOKIE = os.path.join(LOCAL, 'Temp', 'chrome_cookies_vss2.db')
DEBUG_PORT = 9225

# 清理
subprocess.run(['powershell', '-Command',
    "Get-Process chrome -ErrorAction SilentlyContinue | Where-Object {(Get-CimInstance Win32_Process -Filter \"ProcessId=$($_.Id)\").CommandLine -like '*remote-debugging-port*'} | Stop-Process -Force; Start-Sleep 1"],
    capture_output=True)

if os.path.exists(TMP_USER_DATA):
    shutil.rmtree(TMP_USER_DATA, ignore_errors=True)
os.makedirs(os.path.join(TMP_USER_DATA, PROFILE, 'Network'), exist_ok=True)

# 复制完整 Local State
shutil.copy2(os.path.join(SRC_USER_DATA, 'Local State'), os.path.join(TMP_USER_DATA, 'Local State'))
# 复制 Preferences
shutil.copy2(os.path.join(SRC_USER_DATA, PROFILE, 'Preferences'), os.path.join(TMP_USER_DATA, PROFILE, 'Preferences'))
# 复制 VSS cookie
shutil.copy2(VSS_COOKIE, os.path.join(TMP_USER_DATA, PROFILE, 'Network', 'Cookies'))

print('启动 Chrome（带日志）...')
proc = subprocess.Popen(
    [CHROME,
     f'--remote-debugging-port={DEBUG_PORT}',
     f'--user-data-dir={TMP_USER_DATA}',
     f'--profile-directory={PROFILE}',
     '--no-first-run', '--no-default-browser-check',
     '--headless=new', '--disable-gpu',
     '--no-proxy-server',
     '--remote-allow-origins=*',
     '--enable-logging=stderr', '--v=1',
     'about:blank'],
    stdout=subprocess.PIPE, stderr=subprocess.STDOUT)

# 等端口
end = time.time() + 30
ready = False
while time.time() < end:
    try:
        with socket.create_connection(('127.0.0.1', DEBUG_PORT), timeout=1):
            ready = True
            break
    except:
        time.sleep(0.5)

print(f'端口就绪: {ready}')

# 读日志（非阻塞，读 2 秒）
time.sleep(3)
proc.terminate()
try:
    out, _ = proc.communicate(timeout=5)
    log = out.decode('utf-8', errors='replace')
    # 找 cookie/os_crypt 相关日志
    lines = log.split('\n')
    relevant = [l for l in lines if any(k in l.lower() for k in ['cookie', 'os_crypt', 'decrypt', 'app_bound', 'v20', 'able'])]
    print(f'\n=== cookie/加密相关日志 ({len(relevant)} 行) ===')
    for l in relevant[:20]:
        print(l.strip()[:200])
    if not relevant:
        print('（无相关日志）')
        # 打印所有 ERROR
        errors = [l for l in lines if 'ERROR' in l]
        print(f'\n=== ERROR 日志 ({len(errors)} 行) ===')
        for l in errors[:10]:
            print(l.strip()[:200])
except:
    proc.kill()
