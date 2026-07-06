"""
测试 submission-history API 获取所有历史刷题记录
然后对每份试卷调用 test/report 获取题目+答案
"""
import json, time
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

# 测试 submission-history 各种参数
print('=== submission-history ===')
for params in [
    '?pageNo=1&pageSize=20',
    '?pageNo=1&pageSize=20&userId=77826278',
    '?pageNo=1&pageSize=20&questionJobId=10',
    '?pageNo=1&pageSize=20&subTabName=intelligent_page&questionJobId=10',
    '?pageNo=1&pageSize=20&type=intelligent',
]:
    url = f'https://gw-c.nowcoder.com/api/sparta/user/question-training/submission-history{params}'
    r = requests.get(url, headers=HEADERS, impersonate='chrome124', timeout=15)
    ct = r.headers.get('content-type', '')
    is_json = 'json' in ct
    data = r.json() if is_json else {}
    records = data.get('data', {})
    if isinstance(records, dict):
        records = records.get('records', records.get('list', records.get('data', [])))
    count = len(records) if isinstance(records, list) else 0
    print(f'  {params}: status={r.status_code}, records={count}')
    if count > 0:
        print(f'    第一项: {json.dumps(records[0], ensure_ascii=False)[:250]}')
        break
    elif is_json:
        print(f'    resp: {r.text[:200]}'.replace('\n',' '))

# 也测 collect/questions 和 collect/tag-question-list
print('\n=== collect/questions ===')
r = requests.get('https://gw-c.nowcoder.com/api/sparta/user/collect/questions?pageNo=1&pageSize=20',
                 headers=HEADERS, impersonate='chrome124', timeout=10)
print(f'  {r.status_code} {r.text[:200]}'.replace('\n',' '))

print('\n=== collect/tag-question-list ===')
r = requests.get('https://gw-c.nowcoder.com/api/sparta/user/collect/tag-question-list?tagId=570&pageNo=1&pageSize=20',
                 headers=HEADERS, impersonate='chrome124', timeout=10)
print(f'  {r.status_code} {r.text[:200]}'.replace('\n',' '))
