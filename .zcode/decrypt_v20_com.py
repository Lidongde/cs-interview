"""
通过 Chrome IElevator COM 接口解密 v20 App-Bound Encryption cookie
Chrome 127+ 的 cookie 用 ABE 加密，需要调用 Chrome 的 elevation service COM 接口
参考: Chrome 源码 chrome/browser/os_crypt/app_bound_encryption_provider_win.cc
"""
import os, sys, json, base64, sqlite3, ctypes
from ctypes import wintypes
import win32crypt
from Crypto.Cipher import AES

LOCAL = os.environ.get('LOCALAPPDATA')
COOKIE_DB = r'C:\Users\10344936.WIN-43G8H8T1D0A\AppData\Local\Temp\chrome_cookies_vss.db'
LOCAL_STATE = os.path.join(LOCAL, 'Google', 'Chrome', 'User Data', 'Local State')


def decrypt_app_bound_key(encrypted_key_with_prefix):
    """通过 Chrome IElevator COM 接口解密 ABE key
    encrypted_key_with_prefix: 去掉 'APPB' 前缀后的数据
    Chrome 的 IElevator COM 接口 CLSID: {708860E0-F641-4611-8895-7D867DD3675B}
    """
    # 这是一个简化的实现，实际需要调用 COM 接口的 DecryptData 方法
    # 由于复杂度，我们用另一个方法：直接读取 Chrome 的 elevation service 解密
    # 或者使用 pywin32 的 COM 调用
    import pythoncom
    import win32com.client

    # Chrome Elevator CLSID
    CLSID_Elevator = '{708860E0-F641-4611-8895-7D867DD3675B}'
    IID_IElevator = '{A949CB4E-C4F9-44C4-B213-6BF8AA9AC69C}'

    try:
        # 尝试 COM 调用
        obj = pythoncom.CoCreateInstance(
            CLSID_Elevator, None, pythoncom.CLSCTX_LOCAL_SERVER, IID_IElevator)
        # 调用 DecryptData 方法 - 但这个接口需要精确的 IDL 定义
        # 这里先标记为需要进一步实现
        return None
    except Exception as e:
        print(f'  COM 调用失败: {e}')
        return None


def try_decrypt_all_methods(enc_value, master_key_v10):
    """尝试多种解密方法"""
    prefix = enc_value[:3]

    if prefix == b'v10':
        try:
            nonce, ct, tag = enc_value[3:15], enc_value[15:-16], enc_value[-16:]
            c = AES.new(master_key_v10, AES.MODE_GCM, nonce=nonce)
            return c.decrypt_and_verify(ct, tag).decode('utf-8', errors='replace')
        except Exception as e:
            return f'[v10-fail: {e}]'

    elif prefix == b'v20':
        # v20: [v20][32字节 ABE key][12 nonce][ct][16 tag]
        payload = enc_value[3:]
        abe_key_enc = payload[:32]
        rest = payload[32:]

        # 方法1: 尝试 system-level DPAPI (需要 system 权限)
        try:
            abe_key = win32crypt.CryptUnprotectData(abe_key_enc, None, None, None, 0)[1]
            nonce, ct, tag = rest[:12], rest[12:-16], rest[-16:]
            c = AES.new(abe_key, AES.MODE_GCM, nonce=nonce)
            return c.decrypt_and_verify(ct, tag).decode('utf-8', errors='replace')
        except Exception as e1:
            # 方法2: 尝试 CRYPTPROTECT_LOCAL_MACHINE flag
            try:
                abe_key = win32crypt.CryptUnprotectData(abe_key_enc, None, None, None, 1)[1]  # CRYPTPROTECT_LOCAL_MACHINE=1
                nonce, ct, tag = rest[:12], rest[12:-16], rest[-16:]
                c = AES.new(abe_key, AES.MODE_GCM, nonce=nonce)
                return c.decrypt_and_verify(ct, tag).decode('utf-8', errors='replace')
            except Exception as e2:
                return f'[v20-fail: dpapi={e1}, machine={e2}]'
    else:
        # 旧版 DPAPI
        try:
            return win32crypt.CryptUnprotectData(enc_value, None, None, None, 0)[1].decode('utf-8', errors='replace')
        except:
            return '[dpapi-fail]'


# 测试
with open(LOCAL_STATE, 'r', encoding='utf-8') as f:
    ls = json.load(f)
enc_key = base64.b64decode(ls['os_crypt']['encrypted_key'])
if enc_key[:5] == b'DPAPI':
    enc_key = enc_key[5:]
master_key = win32crypt.CryptUnprotectData(enc_key, None, None, None, 0)[1]
print(f'v10 master key: {len(master_key)} bytes')

conn = sqlite3.connect(COOKIE_DB)
cur = conn.cursor()
cur.execute("SELECT host_key, name, encrypted_value FROM cookies WHERE host_key LIKE '%nowcoder%' AND name IN ('uid','username','csrfToken','NOWCODERUID') ORDER BY name")
rows = cur.fetchall()
conn.close()

print(f'\n=== 测试解密 {len(rows)} 个关键 cookie ===')
for host, name, enc in rows:
    val = try_decrypt_all_methods(enc, master_key)
    prefix = enc[:3]
    print(f'  {name:20} prefix={prefix} => {val[:40]}')
