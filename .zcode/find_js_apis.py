"""
获取答题页 HTML，找 JS bundle 路径
然后下载搜索题目 API
"""
import re, json
from curl_cffi import requests

COOKIE = 'Hm_lvt_a808a1326b6c06c437de769d1b85b870=1783324773,1783326792,1783327040,1783332669; HMACCOUNT=5B50E5714BA2371A; NOWCODERCLINETID=5C624A404D820BAA561A9E407C597491; NOWCODERUID=99DB5E9FA741DBE9F474F73C04CD2DE0; acw_tc=0a18ab6c17833326692832986e66ad88590a1857ddae18de8424446dd7c7f2; isAgreementChecked=true; t=95DEC25319FA21258C369646734311BF; gr_user_id=8efaa278-603a-4231-b6df-e5959903fcdd; c196c3667d214851b11233f5c17f99d5_gr_session_id=697b7bd4-3ec7-4108-b9c0-d49935fc4cdb; Hm_lpvt_a808a1326b6c06c437de769d1b85b870=1783333797'

HEADERS = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/150.0.0.0 Safari/537.36',
    'Cookie': COOKIE,
}

# 获取答题页 HTML
r = requests.get('https://www.nowcoder.com/exam/test?testId=97743011',
                 headers=HEADERS, impersonate='chrome124', timeout=15)
print(f'答题页 status: {r.status_code}, len: {len(r.text)}')

# 找 JS 引用
js_urls = re.findall(r'src="([^"]+\.js[^"]*)"', r.text)
print(f'\nJS 文件 ({len(js_urls)}):')
for u in js_urls:
    print(f'  {u}')

# 找 main.entry.js
main_js = [u for u in js_urls if 'main.entry' in u or 'test' in u.lower()]
print(f'\n主 JS: {main_js}')

# 下载所有 JS 搜索 API
print('\n=== 下载 JS 搜索题目 API ===')
import os
for u in js_urls:
    if not u.startswith('http'):
        if u.startswith('//'):
            u = 'https:' + u
        elif u.startswith('/'):
            u = 'https://www.nowcoder.com' + u
    try:
        rj = requests.get(u, headers=HEADERS, impersonate='chrome124', timeout=15)
        if rj.status_code != 200 or len(rj.text) < 1000:
            continue
        content = rj.text
        # 搜索题目相关 API 路径
        apis = set()
        for pattern in [
            r'["\'](/api/[a-zA-Z0-9/_-]*(?:question|paper|exam|practice|test)[a-zA-Z0-9/_-]*)["\']',
            r'["\']([a-zA-Z0-9/_-]*(?:get-question|question-list|paper-detail|get-paper|question-content)[a-zA-Z0-9/_-]*)["\']',
            r'common-practice/([a-zA-Z0-9/_-]+)',
            r'questiontraining/([a-zA-Z0-9/_-]+)',
        ]:
            found = re.findall(pattern, content, re.IGNORECASE)
            for f in found:
                apis.add(f if isinstance(f, str) else f[0] if f else '')
        if apis:
            print(f'\n  [{u.split("/")[-1][:40]}] ({len(content)} chars)')
            for a in sorted(apis):
                if a and len(a) > 3:
                    print(f'    {a[:80]}')
    except Exception as e:
        pass
