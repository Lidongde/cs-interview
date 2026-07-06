"""
加 onlyFinish 参数测试
"""
import json
from curl_cffi import requests

COOKIE = 'Hm_lvt_a808a1326b6c06c437de769d1b85b870=1783324773; NOWCODERCLINETID=5C624A404D820BAA561A9E407C597491; NOWCODERUID=99DB5E9FA741DBE9F474F73C04CD2DE0; acw_tc=0a18ab6c17833326692832986e66ad88590a1857ddae18de8424446dd7c7f2; t=95DEC25319FA21258C369646734311BF'
HEADERS = {
    'accept': 'application/json, text/plain, */*',
    'origin': 'https://www.nowcoder.com',
    'referer': 'https://www.nowcoder.com/users/77826278/tests',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/150.0.0.0 Safari/537.36',
    'x-requested-with': 'XMLHttpRequest',
    'Cookie': COOKIE,
}
UID = 77826278

# count API with onlyFinish
print('=== test-papers-count ===')
for of in ['true', 'false']:
    r = requests.get(f'https://gw-c.nowcoder.com/api/sparta/user/question-training/test-papers-count/{UID}?onlyFinish={of}',
                     headers=HEADERS, impersonate='chrome124', timeout=10)
    print(f'  onlyFinish={of}: {r.text[:200]}'.replace('\n',' '))

# test-papers with onlyFinish + 分页
print('\n=== test-papers (with onlyFinish) ===')
for params in [
    '?pageNo=1&pageSize=20&onlyFinish=true',
    '?pageNo=1&pageSize=20&onlyFinish=false',
    '?pageNo=1&pageSize=50&onlyFinish=true',
    '?pageNo=1&pageSize=100&onlyFinish=false',
    '?pageNo=1&pageSize=20&onlyFinish=true&subTabName=intelligent_page',
    '?pageNo=1&pageSize=20&onlyFinish=true&questionJobId=10',
    '?pageNo=1&pageSize=20&onlyFinish=false&subTabName=intelligent_page&questionJobId=10',
]:
    url = f'https://gw-c.nowcoder.com/api/sparta/user/question-training/test-papers/{UID}{params}'
    r = requests.get(url, headers=HEADERS, impersonate='chrome124', timeout=15)
    data = r.json()
    d = data.get('data', {})
    if isinstance(d, dict):
        records = d.get('list', d.get('records', d.get('rows', d.get('data', []))))
        total = d.get('totalCount', d.get('total', d.get('count', '?')))
    elif isinstance(d, list):
        records = d
        total = len(d)
    else:
        records = []
        total = '?'
    count = len(records) if isinstance(records, list) else 0
    print(f'  {params}: {count} 条, total={total}')
    if count > 0:
        print(f'    第一项: {json.dumps(records[0], ensure_ascii=False)[:200]}')
        # 统计标签
        tags = {}
        for item in records:
            name = item.get('name', '')
            tag = name.replace('专项练习-', '') if '专项练习-' in name else name
            tags[tag] = tags.get(tag, 0) + 1
        print(f'    标签分布: {tags}')
        if total != '?' and count < total:
            print(f'    ★ 有分页！需要翻 {total} 页')
