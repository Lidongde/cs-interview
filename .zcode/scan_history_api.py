"""
从 examTest/main.entry.js 搜索 testHistory / submission / history 相关 API
"""
import re
from curl_cffi import requests

r = requests.get('https://static.nowcoder.com/fe/file/site/www-web/prod/1.0.484/page/examTest/main.entry.js',
                 impersonate='chrome124', timeout=20)
content = r.text

# 搜索 testHistory / submission / history 相关
for kw in ['testHistory', 'submission', 'history', 'History', 'pageSource', 'wrong-question', 'wrongQuestion', 'getWrong', 'getRecord', 'recordList', 'paperList', 'testList', 'getTestList']:
    idxs = [m.start() for m in re.finditer(re.escape(kw), content)]
    if idxs:
        print(f'\n=== {kw} ({len(idxs)} hits) ===')
        for i in idxs[:2]:
            chunk = content[max(0,i-120):i+150]
            # 找附近的 /api/ 路径
            apis = re.findall(r'/api/[a-zA-Z0-9/_-]+', chunk)
            if apis:
                print(f'  API: {apis}')
            print(f'  ...{chunk[-100:]}...')

# 搜索所有含 history/testHistory 的 API 路径
print('\n=== 所有含 history/testHistory/submission/record 的 API ===')
for m in re.finditer(r'["\'](/api/[a-zA-Z0-9/_-]+)["\']', content):
    a = m.group(1)
    if any(k in a.lower() for k in ['history', 'submission', 'record', 'wrong', 'list', 'page']):
        print(f'  {a}')
