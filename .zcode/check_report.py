import json
from curl_cffi import requests
COOKIE = 'Hm_lvt_a808a1326b6c06c437de769d1b85b870=1783324773; NOWCODERUID=99DB5E9FA741DBE9F474F73C04CD2DE0; acw_tc=0a18ab6c17833326692832986e66ad88590a1857ddae18de8424446dd7c7f2; t=95DEC25319FA21258C369646734311BF'
H = {'content-type':'application/json','origin':'https://www.nowcoder.com','referer':'https://www.nowcoder.com/','user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36','x-requested-with':'XMLHttpRequest','Cookie':COOKIE,'accept':'application/json'}
r = requests.post('https://gw-c.nowcoder.com/api/sparta/test/report', json={'testId':97743362,'paperId':67856352}, headers=H, impersonate='chrome124', timeout=15)
print(json.dumps(r.json(), ensure_ascii=False, indent=2)[:3000])
