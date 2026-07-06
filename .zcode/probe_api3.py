"""
用浏览器 cookie 探测牛客 sparta API
"""
import json
from curl_cffi import requests

COOKIE = 'csrfToken=wG3Z5kaxLVeTu7QTYxFuzxqO; NOWCODERCLINETID=2DEEDA641B91DA09AB0F8ED6A070B74D; NOWCODERUID=170DDA1FC05E2E920461A9E80E8ACF54; SERVERID=824721c4a8a596642b7bcb69b533212a|1783322899|1783319145; SERVERCORSID=824721c4a8a596642b7bcb69b533212a|1783322899|1783319145'

HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36',
    'Accept': 'application/json, text/plain, */*',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Referer': 'https://www.nowcoder.com/exam/intelligent',
    'Origin': 'https://www.nowcoder.com',
    'Content-Type': 'application/json',
    'Cookie': COOKIE,
}

# 候选 API
GET_APIS = [
    'https://gw-c.nowcoder.com/api/sparta/exam/exam-paper/get-by-tag?tagId=570',
    'https://gw-c.nowcoder.com/api/sparta/exam/question/by-tag?tagId=570&pageNo=1&pageSize=20',
    'https://gw-c.nowcoder.com/api/sparta/exam/question-list?tagId=570',
    'https://gw-c.nowcoder.com/api/sparta/exam/questions?tagId=570',
    'https://gw-c.nowcoder.com/api/sparta/exam/paper?tagId=570',
    'https://gw-c.nowcoder.com/api/sparta/exam/test?tagId=570',
    'https://gw-c.nowcoder.com/api/sparta/exam/intelligent?tagId=570',
    'https://gw-c.nowcoder.com/api/sparta/question-bank/question/list?tagId=570',
    'https://gw-c.nowcoder.com/api/sparta/exam/exam-paper/list?tagId=570&questionJobId=10',
    'https://gw-c.nowcoder.com/api/sparta/exam/collection?tagId=570',
]
POST_APIS = [
    ('https://gw-c.nowcoder.com/api/sparta/exam/exam-paper/create', {'tagId': 570, 'questionJobId': 10}),
    ('https://gw-c.nowcoder.com/api/sparta/exam/paper/create', {'tagId': 570}),
    ('https://gw-c.nowcoder.com/api/sparta/exam/start-practice', {'tagId': 570}),
    ('https://gw-c.nowcoder.com/api/sparta/exam/exam-paper/get-by-tag', {'tagId': 570}),
]

print('=== GET APIs ===')
for url in GET_APIS:
    try:
        r = requests.get(url, headers=HEADERS, impersonate='chrome124', timeout=15)
        is_waf = 'aliyun_waf' in r.text[:500]
        ct = r.headers.get('content-type', '')
        tag = 'WAF' if is_waf else ('JSON' if 'json' in ct else 'HTML')
        short = url.split('api/sparta/')[-1][:55]
        print(f'  {r.status_code} {tag:4} {short}')
        if 'json' in ct and not is_waf:
            print(f'      => {r.text[:250]}'.replace('\n',' '))
    except Exception as e:
        print(f'  ERR {url[-40:]}: {str(e)[:60]}')

print('\n=== POST APIs ===')
for url, body in POST_APIS:
    try:
        r = requests.post(url, json=body, headers=HEADERS, impersonate='chrome124', timeout=15)
        is_waf = 'aliyun_waf' in r.text[:500]
        ct = r.headers.get('content-type', '')
        tag = 'WAF' if is_waf else ('JSON' if 'json' in ct else 'HTML')
        short = url.split('api/sparta/')[-1][:55]
        print(f'  {r.status_code} {tag:4} {short}')
        if 'json' in ct and not is_waf:
            print(f'      => {r.text[:250]}'.replace('\n',' '))
    except Exception as e:
        print(f'  ERR {url[-40:]}: {str(e)[:60]}')
