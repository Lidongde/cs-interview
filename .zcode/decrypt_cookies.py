"""
完整解密 Chrome 的 nowcoder cookie，验证登录态
"""
import os, sys, json, base64, sqlite3
import win32crypt
from Crypto.Cipher import AES

LOCAL = os.environ.get('LOCALAPPDATA')
COOKIE_DB = r'C:\Users\10344936.WIN-43G8H8T1D0A\AppData\Local\Temp\chrome_cookies_vss.db'
LOCAL_STATE = os.path.join(LOCAL, 'Google', 'Chrome', 'User Data', 'Local State')

def get_master_key():
    with open(LOCAL_STATE, 'r', encoding='utf-8') as f:
        ls = json.load(f)
    enc_key = base64.b64decode(ls['os_crypt']['encrypted_key'])
    if enc_key[:5] == b'DPAPI':
        enc_key = enc_key[5:]
    return win32crypt.CryptUnprotectData(enc_key, None, None, None, 0)[1]

def decrypt(enc_value, key):
    if enc_value[:3] in (b'v10', b'v20'):
        nonce, ct, tag = enc_value[3:15], enc_value[15:-16], enc_value[-16:]
        c = AES.new(key, AES.MODE_GCM, nonce=nonce)
        return c.decrypt_and_verify(ct, tag).decode('utf-8', errors='replace')
    # 旧 DPAPI
    try:
        return win32crypt.CryptUnprotectData(enc_value, None, None, None, 0)[1].decode('utf-8', errors='replace')
    except:
        return '[fail]'

key = get_master_key()
print(f'master key len: {len(key)} bytes')

conn = sqlite3.connect(COOKIE_DB)
cur = conn.cursor()
cur.execute("SELECT host_key, name, encrypted_value, path FROM cookies WHERE host_key LIKE '%nowcoder%' ORDER BY host_key, name")
rows = cur.fetchall()
conn.close()

print(f'\n=== 解密 {len(rows)} 个 nowcoder cookie ===')
results = []
for host, name, enc, path in rows:
    try:
        val = decrypt(enc, key)
    except Exception as e:
        val = f'[err: {e}]'
    # 脱敏
    vs = val[:20] + '...' if len(val) > 20 else val
    print(f'  {host:25} {name:32} = {vs}')
    results.append({'host': host, 'name': name, 'value': val, 'path': path})

# 判断登录态
has_uid = any(r['name'] == 'uid' and r['value'] for r in results)
has_username = any(r['name'] == 'username' and r['value'] for r in results)
print(f'\n登录态: uid={"有" if has_uid else "无"}, username={"有" if has_username else "无"}')
print(f'是否已登录: {"是 ✓" if (has_uid and has_username) else "否 ✗"}')
