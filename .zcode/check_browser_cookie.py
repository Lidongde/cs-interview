"""
检查 Chrome / Edge 的 cookie 数据库，看哪个浏览器登录了牛客
Windows: Chrome cookie 用 DPAPI 加密（AES-GCM，key 存在 Local State）
这里先不解密，只看是否存在 nowcoder.com 的 cookie 条目
"""
import os, sqlite3, shutil, tempfile, sys

def check_cookies(cookie_path, browser_name):
    if not os.path.exists(cookie_path):
        print(f'  [{browser_name}] cookie 文件不存在')
        return
    # 复制到临时文件（避免锁冲突）
    tmp = os.path.join(tempfile.gettempdir(), f'cookies_{browser_name}.db')
    try:
        shutil.copy2(cookie_path, tmp)
    except Exception as e:
        print(f'  [{browser_name}] 复制失败: {e}')
        return
    try:
        conn = sqlite3.connect(tmp)
        cur = conn.cursor()
        # 查看 nowcoder.com 相关的 cookie
        cur.execute("SELECT host_key, name, length(encrypted_value), expires_utc FROM cookies WHERE host_key LIKE '%nowcoder%' ORDER BY name")
        rows = cur.fetchall()
        print(f'  [{browser_name}] nowcoder cookie 条目数: {len(rows)}')
        for host, name, vlen, exp in rows:
            print(f'      {host:25} {name:30} value_len={vlen}')
        conn.close()
        # 也看下是否登录（NOWCODERUID 是否存在且较长）
    except Exception as e:
        print(f'  [{browser_name}] 读取失败: {e}')
    finally:
        try: os.remove(tmp)
        except: pass

local = os.environ.get('LOCALAPPDATA')
chrome_cookies = os.path.join(local, 'Google', 'Chrome', 'User Data', 'Default', 'Network', 'Cookies')
edge_cookies = os.path.join(local, 'Microsoft', 'Edge', 'User Data', 'Default', 'Network', 'Cookies')
# Edge 还有 Profile 1
edge_profile1 = os.path.join(local, 'Microsoft', 'Edge', 'User Data', 'Profile 1', 'Network', 'Cookies')

print('=== 检查浏览器 cookie ===')
check_cookies(chrome_cookies, 'Chrome-Default')
check_cookies(edge_cookies, 'Edge-Default')
check_cookies(edge_profile1, 'Edge-Profile1')
