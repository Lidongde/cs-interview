"""
用 cookie + chrome124 指纹测试牛客 API
"""
import json
from curl_cffi import requests

with open(r'D:/Workspace/Project/cs-interview/.zcode/nowcoder_cookies.json', 'r', encoding='utf-8') as f:
    d = json.load(f)

COOKIE = d['cookie_string']

HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36',
    'Accept': 'application/json, text/plain, */*',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Referer': 'https://www.nowcoder.com/exam/intelligent',
    'Origin': 'https://www.nowcoder.com',
    'Content-Type': 'application/json',
    'Cookie': COOKIE,
}

# 测试用户信息 API（确认登录态）
print('=== 测试用户信息 API ===')
test_apis = [
    'https://gw-c.nowcoder.com/api/sparta/user-info',
    'https://gw-c.nowcoder.com/api/sparta/account/user-info',
    'https://gw-c.nowcoder.com/api/sparta/user/info',
    'https://gw-c.nowcoder.com/api/sparta/exam/exam-paper/get-by-tag?tagId=570',
    'https://gw-c.nowcoder.com/api/sparta/exam/question/by-tag?tagId=570',
    'https://gw-c.nowcoder.com/api/sparta/exam/paper/list?tagId=570',
]
for url in test_apis:
    try:
        r = requests.get(url, headers=HEADERS, impersonate='chrome124', timeout=15)
        is_waf = 'aliyun_waf' in r.text[:500]
        ct = r.headers.get('content-type', '')
        tag = 'WAF' if is_waf else ('JSON' if 'json' in ct else 'HTML')
        short = url.split('api/sparta/')[-1][:50]
        print(f'  {r.status_code} {tag:4} {short}')
        if 'json' in ct and not is_waf:
            print(f'      => {r.text[:250]}'.replace('\n', ' '))
    except Exception as e:
        print(f'  ERR {url[-40:]}: {str(e)[:60]}')
