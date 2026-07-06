"""直接用 subprocess 启动 Chrome 并捕获输出"""
import subprocess, time, os

CHROME = r'C:\Program Files\Google\Chrome\Application\chrome.exe'
USER_DATA = r'C:\Users\10344936.WIN-43G8H8T1D0A\AppData\Local\Google\Chrome\User Data'

# 用临时 profile 测试端口
tmp_profile = r'C:\Users\10344936.WIN-43G8H8T1D0A\AppData\Local\Temp\chrome_debug_profile'

print('启动 Chrome (临时 profile, headless)...')
proc = subprocess.Popen(
    [CHROME,
     '--remote-debugging-port=9223',
     f'--user-data-dir={tmp_profile}',
     '--no-first-run', '--no-default-browser-check',
     '--headless=new', '--disable-gpu',
     '--no-proxy-server',
     'about:blank'],
    stdout=subprocess.PIPE, stderr=subprocess.PIPE)

time.sleep(6)
print(f'进程存活: {proc.poll() is None}')
print(f'PID: {proc.pid}')

# 检查端口
import socket
s = socket.socket()
s.settimeout(3)
try:
    s.connect(('127.0.0.1', 9223))
    print('端口 9223 可连接 ✓')
except Exception as e:
    print(f'端口 9223 不可连接: {e}')

# 读 stderr
proc.terminate()
try:
    out, err = proc.communicate(timeout=5)
    print(f'stdout: {out[:500]}')
    print(f'stderr: {err[:500]}')
except:
    proc.kill()
