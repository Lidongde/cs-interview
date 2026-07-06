"""
用 curl_cffi impersonate 重新探测牛客 API（关键：模拟浏览器 TLS 指纹绕过 WAF）
模仿 leetcode_crawler 的做法
"""
import json
from curl_cffi import requests

HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36',
    'Accept': 'application/json, text/plain, */*',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Referer': 'https://www.nowcoder.com/exam/intelligent',
    'Origin': 'https://www.nowcoder.com',
    'Content-Type': 'application/json',
}

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

for imp in ['chrome124', 'safari17_0']:
    print(f'\n========== impersonate={imp} ==========')
    print('--- GET ---')
    for url in GET_APIS:
        try:
            r = requests.get(url, headers=HEADERS, impersonate=imp, timeout=15)
            is_waf = 'aliyun_waf' in r.text[:500]
            ct = r.headers.get('content-type', '')
            tag = 'WAF' if is_waf else ('JSON' if 'json' in ct else 'HTML')
            short = url.split('api/sparta/')[-1][:55]
            print(f'  {r.status_code} {tag:4} {short}')
            if 'json' in ct and not is_waf:
                print(f'      => {r.text[:200]}'.replace('\n', ' '))
        except Exception as e:
            print(f'  ERR {url[-40:]}: {str(e)[:60]}')
    print('--- POST ---')
    for url, body in POST_APIS:
        try:
            r = requests.post(url, json=body, headers=HEADERS, impersonate=imp, timeout=15)
            is_waf = 'aliyun_waf' in r.text[:500]
            ct = r.headers.get('content-type', '')
            tag = 'WAF' if is_waf else ('JSON' if 'json' in ct else 'HTML')
            short = url.split('api/sparta/')[-1][:55]
            print(f'  {r.status_code} {tag:4} {short}')
            if 'json' in ct and not is_waf:
                print(f'      => {r.text[:200]}'.replace('\n', ' '))
        except Exception as e:
            print(f'  ERR {url[-40:]}: {str(e)[:60]}')
