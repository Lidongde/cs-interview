"""
验证从 VSS 复制的 Chrome cookie 数据库
"""
import os, sqlite3

db = r'C:\Users\10344936.WIN-43G8H8T1D0A\AppData\Local\Temp\chrome_cookies_vss.db'
conn = sqlite3.connect(db)
cur = conn.cursor()
cur.execute("SELECT host_key, name, length(encrypted_value) FROM cookies WHERE host_key LIKE '%nowcoder%' ORDER BY name")
rows = cur.fetchall()
print(f'=== nowcoder cookie 条目: {len(rows)} ===')
for host, name, vlen in rows:
    print(f'  {host:28} {name:32} enc_len={vlen}')
conn.close()
