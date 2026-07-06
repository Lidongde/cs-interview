import re
from curl_cffi import requests
r = requests.get('https://static.nowcoder.com/fe/file/site/www-web/prod/1.0.484/page/examTest/main.entry.js', impersonate='chrome124', timeout=20)
content = r.text

# 找所有 test/ 开头的 API
print('=== 所有 test/ API ===')
for m in re.finditer(r'["\'](/api/[a-zA-Z0-9/_.-]+)["\']', content):
    a = m.group(1)
    if 'test' in a.lower():
        print(f'  {a}')

# 找所有 sparta/ API（完整列表）
print('\n=== 所有 sparta/ API ===')
all_apis = set()
for m in re.finditer(r'["\'](/api/sparta/[a-zA-Z0-9/_.-]+)["\']', content):
    all_apis.add(m.group(1))
for a in sorted(all_apis):
    print(f'  {a}')

# 找 common-practice/ API
print('\n=== common-practice/ API ===')
for m in re.finditer(r'common-practice/[a-zA-Z0-9/_-]+', content):
    all_apis.add(m.group(0))
    print(f'  {m.group(0)}')

# detail-paper 附近（这个 API 可能返回答案）
print('\n=== detail-paper 上下文 ===')
idx = content.find('detail-paper')
if idx >= 0:
    print(content[max(0,idx-200):idx+200])
