"""
探查用户历史刷题页面的 API
URL: https://www.nowcoder.com/users/77826278/tests
"""
import re, json
from curl_cffi import requests

COOKIE = 'Hm_lvt_a808a1326b6c06c437de769d1b85b870=1783324773; NOWCODERCLINETID=5C624A404D820BAA561A9E407C597491; NOWCODERUID=99DB5E9FA741DBE9F474F73C04CD2DE0; acw_tc=0a18ab6c17833326692832986e66ad88590a1857ddae18de8424446dd7c7f2; t=95DEC25319FA21258C369646734311BF'
HEADERS = {
    'accept': 'text/html,application/xhtml+xml',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/150.0.0.0 Safari/537.36',
    'Cookie': COOKIE,
}

# 1. 获取历史刷题页 HTML
r = requests.get('https://www.nowcoder.com/users/77826278/tests',
                 headers=HEADERS, impersonate='chrome124', timeout=15)
print(f'HTML status={r.status_code}, len={len(r.text)}')
title = re.search(r'<title>(.*?)</title>', r.text)
print(f'title: {title.group(1) if title else "none"}')

# 找 JS
js_srcs = re.findall(r'src="([^"]+\.js[^"]*)"', r.text)
print(f'JS: {js_srcs}')

# 找内联数据（SSR 数据）
# 牛客常在 window.__INITIAL_STATE__ 或 window.xxx 注入数据
inline_data = re.findall(r'window\.(\w+)\s*=\s*(\{[^;]{10,500})', r.text)
print(f'\n内联 window 变量 ({len(inline_data)}):')
for name, val in inline_data[:5]:
    print(f'  window.{name} = {val[:150]}...')

# 找 API 端点
api_refs = re.findall(r'/api/[a-zA-Z0-9/_-]+', r.text)
print(f'\nHTML 里的 API 引用: {set(api_refs)}')

# 2. 探测历史刷题 API
print('\n=== 探测历史刷题 API ===')
HEADERS_JSON = {**HEADERS, 'accept': 'application/json', 'content-type': 'application/json',
                'x-requested-with': 'XMLHttpRequest', 'origin': 'https://www.nowcoder.com',
                'referer': 'https://www.nowcoder.com/users/77826278/tests'}
candidates = [
    ('GET', f'https://www.nowcoder.com/api/user/tests?userId=77826278&pageNo=1&pageSize=20'),
    ('GET', f'https://www.nowcoder.com/api/user/test-list?userId=77826278&pageNo=1&pageSize=20'),
    ('GET', f'https://www.nowcoder.com/api/user/testHistory?userId=77826278&pageNo=1&pageSize=20'),
    ('GET', f'https://www.nowcoder.com/api/profile/77826278/test-papers?pageNo=1&pageSize=20'),
    ('GET', f'https://www.nowcoder.com/api/profile/77826278/tests?pageNo=1&pageSize=20'),
    ('GET', f'https://gw-c.nowcoder.com/api/sparta/test/user-tests?userId=77826278&pageNo=1&pageSize=20'),
    ('GET', f'https://gw-c.nowcoder.com/api/sparta/test/test-history?userId=77826278&pageNo=1&pageSize=20'),
    ('GET', f'https://gw-c.nowcoder.com/api/sparta/test/history-list?userId=77826278&pageNo=1&pageSize=20'),
    ('GET', f'https://gw-c.nowcoder.com/api/sparta/test/list-by-user?userId=77826278&pageNo=1&pageSize=20'),
    ('GET', f'https://gw-c.nowcoder.com/api/sparta/common-practice/test-history?userId=77826278&pageNo=1&pageSize=20'),
    ('GET', f'https://gw-c.nowcoder.com/api/sparta/common-practice/history?userId=77826278&pageNo=1&pageSize=20'),
    ('GET', f'https://gw-c.nowcoder.com/api/sparta/user/tests?userId=77826278&pageNo=1&pageSize=20'),
    ('GET', f'https://gw-c.nowcoder.com/api/sparta/user/test-history?userId=77826278&pageNo=1&pageSize=20'),
]
for method, url in candidates:
    try:
        r = requests.get(url, headers=HEADERS_JSON, impersonate='chrome124', timeout=10)
        ct = r.headers.get('content-type', '')
        is_json = 'json' in ct
        has_data = is_json and ('"code":0' in r.text or '"success":true' in r.text or '"msg":"OK"' in r.text) and len(r.text) > 80
        short = url.split('api/')[-1][:60]
        if r.status_code != 404:
            marker = ' ★★★' if has_data else (' ★JSON' if is_json else '')
            print(f'  {r.status_code} {method} {short}{marker}')
            if has_data:
                print(f'    => {r.text[:300]}'.replace('\n',' '))
    except Exception as e:
        print(f'  ERR {url[-40:]}: {str(e)[:40]}')
