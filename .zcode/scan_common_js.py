"""
搜索 common.js 里所有 /api/ 路径
"""
import re
from curl_cffi import requests

HEADERS = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'}

r = requests.get('https://static.nowcoder.com/nowcoder/2.0.312/javascripts-wp/lib/common.js',
                 headers=HEADERS, impersonate='chrome124', timeout=20)
content = r.text
print(f'common.js: {len(content)} chars')

# 找所有 /api/ 路径
apis = set()
for m in re.finditer(r'["\'](/api/[a-zA-Z0-9/_.?=&-]+)["\']', content):
    apis.add(m.group(1))

# 也找 questiontraining 和 common-practice 相关
for m in re.finditer(r'(?:questiontraining|common-practice|sparta)/[a-zA-Z0-9/_-]+', content):
    apis.add(m.group(0))

# 过滤出题目相关的
question_apis = sorted([a for a in apis if any(k in a.lower() for k in ['question', 'paper', 'exam', 'practice', 'test', 'answer', 'content'])])
print(f'\n=== 题目相关 API ({len(question_apis)}) ===')
for a in question_apis:
    print(f'  {a}')

# 也打印所有 /api/ 路径
all_apis = sorted([a for a in apis if a.startswith('/api/')])
print(f'\n=== 所有 /api/ 路径 ({len(all_apis)}) ===')
for a in all_apis:
    print(f'  {a}')
