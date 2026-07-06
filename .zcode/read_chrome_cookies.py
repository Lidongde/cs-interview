"""
从 Chrome 读取并解密 cookie（Windows DPAPI + AES-GCM）
需要 Chrome 关闭，或用快捷方式绕过锁
"""
import os, sys, json, base64, shutil, sqlite3, tempfile

def get_chrome_cookie_key(local_state_path):
    """从 Local State 读取加密的 cookie key，用 DPAPI 解密"""
    import win32crypt
    with open(local_state_path, 'r', encoding='utf-8') as f:
        ls = json.load(f)
    encrypted_key_b64 = ls['os_crypt']['encrypted_key']
    encrypted_key = base64.b64decode(encrypted_key_b64)
    # 去掉 'DPAPI' 前缀
    if encrypted_key[:5] == b'DPAPI':
        encrypted_key = encrypted_key[5:]
    # DPAPI 解密
    key = win32crypt.CryptUnprotectData(encrypted_key, None, None, None, 0)[1]
    return key

def decrypt_cookie_value(encrypted_value, key):
    """解密单个 cookie value (AES-GCM)"""
    from Crypto.Cipher import AES
    # Chrome 用 'v10' 或 'v20' 前缀
    if encrypted_value[:3] in (b'v10', b'v20'):
        nonce = encrypted_value[3:15]  # 12 bytes
        ciphertext = encrypted_value[15:-16]
        tag = encrypted_value[-16:]
        cipher = AES.new(key, AES.MODE_GCM, nonce=nonce)
        try:
            return cipher.decrypt_and_verify(ciphertext, tag).decode('utf-8', errors='replace')
        except Exception as e:
            return f'[decrypt-fail: {e}]'
    else:
        # 旧版 DPAPI 直接加密
        import win32crypt
        try:
            return win32crypt.CryptUnprotectData(encrypted_value, None, None, None, 0)[1].decode('utf-8', errors='replace')
        except:
            return '[dpapi-fail]'

def read_chrome_cookies(cookie_db_path, local_state_path, host_filter='nowcoder'):
    key = get_chrome_cookie_key(local_state_path)
    # 复制 db（避免锁）
    tmp = os.path.join(tempfile.gettempdir(), 'chrome_cookies_tmp.db')
    # 尝试多种复制方式
    copied = False
    for attempt in range(3):
        try:
            shutil.copy2(cookie_db_path, tmp)
            copied = True
            break
        except PermissionError:
            if attempt == 0:
                # 尝试用 powershell 复制
                import subprocess
                subprocess.run(['powershell', '-Command', f'Copy-Item "{cookie_db_path}" "{tmp}" -Force'], capture_output=True)
                if os.path.exists(tmp):
                    copied = True
                    break
            import time
            time.sleep(1)
    if not copied:
        print('无法复制 cookie 文件（Chrome 开着）。请关闭 Chrome 后重试，或继续用 agent-browser 登录。', file=sys.stderr)
        return None

    conn = sqlite3.connect(tmp)
    cur = conn.cursor()
    cur.execute("SELECT host_key, name, encrypted_value, path, expires_utc, is_secure, is_httponly FROM cookies WHERE host_key LIKE ?", (f'%{host_filter}%',))
    rows = cur.fetchall()
    conn.close()
    os.remove(tmp)

    cookies = []
    for host, name, enc_val, path, exp, secure, httponly in rows:
        val = decrypt_cookie_value(enc_val, key)
        cookies.append({
            'host': host, 'name': name, 'value': val, 'path': path,
            'expires': exp, 'secure': secure, 'httponly': httponly
        })
    return cookies

if __name__ == '__main__':
    local = os.environ.get('LOCALAPPDATA')
    cookie_db = os.path.join(local, 'Google', 'Chrome', 'User Data', 'Default', 'Network', 'Cookies')
    local_state = os.path.join(local, 'Google', 'Chrome', 'User Data', 'Local State')
    cookies = read_chrome_cookies(cookie_db, local_state, 'nowcoder')
    if cookies is None:
        sys.exit(1)
    print(f'=== 找到 {len(cookies)} 个 nowcoder cookie ===')
    for c in cookies:
        v = c['value']
        # 脱敏显示（只显示前10位）
        vshow = v[:15] + '...' if len(v) > 15 else v
        print(f'  {c["host"]:25} {c["name"]:30} = {vshow}')
