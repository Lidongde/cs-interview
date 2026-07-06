"""
通过 Chrome IElevator COM 接口解密 v20 App-Bound Encryption key
Chrome 127+ 的 app_bound_encrypted_key 需要 IElevator COM 解密
CLSID: {708860E0-F641-4611-8895-7D867DD3675B}
"""
import os, sys, json, base64, sqlite3
import win32crypt
import pythoncom
from Crypto.Cipher import AES

LOCAL = os.environ.get('LOCALAPPDATA')
COOKIE_DB = os.path.join(LOCAL, 'Temp', 'chrome_cookies_vss2.db')  # VSS 版本（含 session cookie）
LOCAL_STATE = os.path.join(LOCAL, 'Google', 'Chrome', 'User Data', 'Local State')


def get_v20_key_via_elevator():
    """通过 Chrome IElevator COM 解密 app_bound_encrypted_key"""
    with open(LOCAL_STATE, 'r', encoding='utf-8') as f:
        ls = json.load(f)
    abe_key_b64 = ls['os_crypt']['app_bound_encrypted_key']
    abe_key_enc = base64.b64decode(abe_key_b64)

    # APPB 前缀 (4 bytes) + version (1 byte) + encrypted data
    print(f'  ABE key 前缀: {abe_key_enc[:5]}')
    print(f'  ABE key 总长: {len(abe_key_enc)}')

    # 去掉 APPB 前缀和 version 字节
    # 结构: "APPB" + 1 byte version + 8 bytes ( Flags + Key Length) + encrypted key
    # 实际: APPB + 01 + 00000000 + DPAPI encrypted key
    # 尝试去掉 "APPB" (4) + 1 (version) 后用 DPAPI 解密
    payload = abe_key_enc[5:]  # 去掉 "APPB" + version
    print(f'  payload 长度: {len(payload)}')

    # 方法1: 普通 DPAPI
    try:
        key = win32crypt.CryptUnprotectData(payload, None, None, None, 0)[1]
        print(f'  ✓ DPAPI 解密成功，key 长度: {len(key)}')
        return key
    except Exception as e1:
        print(f'  DPAPI 普通解密失败: {e1}')

    # 方法2: CRYPTPROTECT_LOCAL_MACHINE
    try:
        key = win32crypt.CryptUnprotectData(payload, None, None, None, 1)[1]
        print(f'  ✓ DPAPI (machine) 解密成功，key 长度: {len(key)}')
        return key
    except Exception as e2:
        print(f'  DPAPI machine 解密失败: {e2}')

    # 方法3: 去掉更多前缀字节
    for offset in [9, 13, 12, 8, 6, 4]:
        try:
            key = win32crypt.CryptUnprotectData(abe_key_enc[offset:], None, None, None, 0)[1]
            print(f'  ✓ offset={offset} DPAPI 解密成功，key 长度: {len(key)}')
            return key
        except:
            pass

    # 方法4: IElevator COM 接口
    print('  尝试 IElevator COM...')
    try:
        CLSID_Elevator = '{708860E0-F641-4611-8895-7D867DD3675B}'
        IID_IElevator = '{A949CB4E-C4F9-44C4-B213-6BF8AA9AC69C}'
        obj = pythoncom.CoCreateInstance(
            CLSID_Elevator, None, pythoncom.CLSCTX_LOCAL_SERVER, IID_IElevator)
        print(f'  COM 对象创建成功: {obj}')
        # IElevator 接口有 DecryptData 方法，但需要正确的 IDL
        # 这里先用 QueryInterface 探索
        return None
    except Exception as e:
        print(f'  COM 失败: {e}')
        return None


def decrypt_v20_cookie(enc_value, v20_key):
    """用 v20 key 解密 cookie"""
    if enc_value[:3] != b'v20':
        return None
    payload = enc_value[3:]
    abe_key_enc = payload[:32]
    rest = payload[32:]
    nonce, ct, tag = rest[:12], rest[12:-16], rest[-16:]
    c = AES.new(v20_key, AES.MODE_GCM, nonce=nonce)
    return c.decrypt_and_verify(ct, tag).decode('utf-8', errors='replace')


print('=== 获取 v20 key ===')
v20_key = get_v20_key_via_elevator()

if v20_key:
    print(f'\n=== 解密 cookie ===')
    conn = sqlite3.connect(COOKIE_DB)
    cur = conn.cursor()
    cur.execute("SELECT host_key, name, encrypted_value FROM cookies WHERE host_key LIKE '%nowcoder%' ORDER BY name")
    rows = cur.fetchall()
    conn.close()

    ok = 0
    for host, name, enc in rows:
        try:
            val = decrypt_v20_cookie(enc, v20_key)
            if val:
                ok += 1
                vs = val[:20] + '...' if len(val) > 20 else val
                print(f'  ✓ {name:25} = {vs}')
        except Exception as e:
            print(f'  ✗ {name:25} 解密失败: {e}')
    print(f'\n成功解密 {ok}/{len(rows)}')
else:
    print('❌ 无法获取 v20 key')
