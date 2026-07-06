"""
submission-history 用 POST，collect/tag-question-list 加 userId
"""
import json
from curl_cffi import requests

COOKIE = 'Hm_lvt_a808a1326b6c06c437de769d1b85b870=1783324773; NOWCODERCLINETID=5C624A404D820BAA561A9E407C597491; NOWCODERUID=99DB5E9FA741DBE9F474F73C04CD2DE0; acw_tc=0a18ab6c17833326692832986e66ad88590a1857ddae18de8424446dd7c7f2; t=95DEC25319FA21258C369646734311BF'
HEADERS = {
    'accept': 'application/json, text/plain, */*',
    'content-type': 'application/json',
    'origin': 'https://www.nowcoder.com',
    'referer': 'https://www.nowcoder.com/users/77826278/tests',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/150.0.0.0 Safari/537.36',
    'x-requested-with': 'XMLHttpRequest',
    'Cookie': COOKIE,
}

# 1. submission-history POST
print('=== submission-history (POST) ===')
bodies = [
    {'pageNo': 1, 'pageSize': 20},
    {'pageNo': 1, 'pageSize': 20, 'userId': 77826278},
    {'pageNo': 1, 'pageSize': 20, 'questionJobId': 10},
    {'pageNo': 1, 'pageSize': 20, 'subTabName': 'intelligent_page', 'questionJobId': 10},
]
for body in bodies:
    r = requests.post('https://gw-c.nowcoder.com/api/sparta/user/question-training/submission-history',
                      json=body, headers=HEADERS, impersonate='chrome124', timeout=15)
    data = r.json()
    d = data.get('data', {})
    records = []
    if isinstance(d, dict):
        records = d.get('records', d.get('list', d.get('data', d.get('rows', []))))
        if not records and d:
            # 可能直接是数据
            for k in d:
                v = d[k]
                if isinstance(v, list) and len(v) > 0:
                    records = v
                    print(f'  数据在 data.{k}')
                    break
    elif isinstance(d, list):
        records = d

    count = len(records) if isinstance(records, list) else 0
    total = d.get('totalCount', d.get('total', '?')) if isinstance(d, dict) else '?'
    print(f'  body={body}: records={count}, total={total}')
    if count > 0:
        print(f'    第一项: {json.dumps(records[0], ensure_ascii=False)[:300]}')
        print(f'    第一项 keys: {list(records[0].keys()) if isinstance(records[0], dict) else type(records[0])}')
        break
    elif data.get('success') or data.get('code') == 0:
        print(f'    resp: {r.text[:250]}'.replace('\n',' '))

# 2. collect/tag-question-list 加 userId
print('\n=== collect/tag-question-list (GET + userId) ===')
r = requests.get('https://gw-c.nowcoder.com/api/sparta/user/collect/tag-question-list?tagId=570&userId=77826278&pageNo=1&pageSize=20',
                 headers=HEADERS, impersonate='chrome124', timeout=10)
print(f'  {r.status_code} {r.text[:300]}'.replace('\n',' '))

# 也试 POST
r = requests.post('https://gw-c.nowcoder.com/api/sparta/user/collect/tag-question-list',
                  json={'tagId': 570, 'userId': 77826278, 'pageNo': 1, 'pageSize': 20},
                  headers=HEADERS, impersonate='chrome124', timeout=10)
print(f'  POST: {r.status_code} {r.text[:300]}'.replace('\n',' '))
