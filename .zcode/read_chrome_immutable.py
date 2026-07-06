"""
尝试用 sqlite3 只读模式 + immutable 直接读取运行中 Chrome 的 cookie
不复制文件，避免锁问题
"""
import os, sys, json, base64, sqlite3

local = os.environ.get('LOCALAPPDATA')
cookie_db = os.path.join(local, 'Google', 'Chrome', 'User Data', 'Default', 'Network', 'Cookies')

# 用 immutable 只读模式打开（绕过 Chrome 的写锁）
uri = f'file:{cookie_db}?mode=ro&immutable=1'
try:
    conn = sqlite3.connect(uri, uri=True)
    cur = conn.cursor()
    cur.execute("SELECT host_key, name, length(encrypted_value), is_httponly FROM cookies WHERE host_key LIKE '%nowcoder%' ORDER BY name")
    rows = cur.fetchall()
    print(f'=== Chrome nowcoder cookie 条目: {len(rows)} ===')
    for host, name, vlen, httponly in rows:
        print(f'  {host:28} {name:30} enc_len={vlen:5} httponly={httponly}')
    conn.close()
except Exception as e:
    print(f'读取失败: {e}')
    sys.exit(1)
