"""
解密 Chrome v20 (App-Bound Encryption) cookie
v20 key 头部 32 字节是 App-Bound 加密的，需要通过 Chrome 的 IElevator COM 接口解密
但更简单的方式：v20 的前 32 字节用 system-level DPAPI 解密（如果 Chrome 以非提升权限运行）
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

def decrypt_v10(enc_value, key):
    nonce, ct, tag = enc_value[3:15], enc_value[15:-16], enc_value[-16:]
    c = AES.new(key, AES.MODE_GCM, nonce=nonce)
    return c.decrypt_and_verify(ct, tag).decode('utf-8', errors='replace')

def decrypt_v20(enc_value, key):
    """v20: 前 3 字节 'v20'，接着 32 字节是 ABE 加密的 key，剩下是 nonce(12)+ct+tag(16)
    32 字节 ABE key 需要 Chrome 的 IElevator COM 解密。
    这里尝试用 master key 作为 fallback（部分情况）。
    """
    # 完整结构: v20 + 32字节(ABE encrypted key) + 12 nonce + ct + 16 tag
    # 真正解密需要调用 Chrome Elevator。这里先看结构
    payload = enc_value[3:]  # 去掉 v20
    abe_key_enc = payload[:32]
    rest = payload[32:]
    print(f'    v20 结构: abe_key_len={len(abe_key_enc)}, rest_len={len(rest)}')
    # 尝试用 DPAPI 解密 abe_key（v20 中这 32 字节是用 system DPAPI 加密的，普通用户解不开）
    try:
        abe_key = win32crypt.CryptUnprotectData(abe_key_enc, None, None, None, 0)[1]
        print(f'    DPAPI 解 abe_key 成功: len={len(abe_key)}')
        nonce, ct, tag = rest[:12], rest[12:-16], rest[-16:]
        c = AES.new(abe_key, AES.MODE_GCM, nonce=nonce)
        return c.decrypt_and_verify(ct, tag).decode('utf-8', errors='replace')
    except Exception as e:
        return f'[v20-dpapi-fail: {e}]'

key = get_master_key()
print(f'master key (v10): {len(key)} bytes')

# 看一个 cookie 的加密前缀，确认是 v10 还是 v20
conn = sqlite3.connect(COOKIE_DB)
cur = conn.cursor()
cur.execute("SELECT name, encrypted_value FROM cookies WHERE host_key LIKE '%nowcoder%' AND name='uid'")
row = cur.fetchone()
conn.close()
if row:
    enc = row[1]
    prefix = enc[:3]
    print(f'uid cookie 前缀: {prefix} (v10/v20)')
    print(f'总长度: {len(enc)}')
    if prefix == b'v20':
        val = decrypt_v20(enc, key)
        print(f'uid 解密结果: {val[:30]}')
    else:
        val = decrypt_v10(enc, key)
        print(f'uid 解密结果: {val[:30]}')
