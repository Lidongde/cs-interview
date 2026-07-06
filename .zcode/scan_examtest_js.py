"""
搜索 examTest/main.entry.js 里的所有 API，特别是答案/解析相关
"""
import re
from curl_cffi import requests

HEADERS = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'}

# 下载 examTest main.entry.js
r = requests.get('https://static.nowcoder.com/fe/file/site/www-web/prod/1.0.484/page/examTest/main.entry.js',
                 headers=HEADERS, impersonate='chrome124', timeout=20)
content = r.text
print(f'examTest main.entry.js: {len(content)} chars')

# 搜索所有 /api/ 路径
apis = set()
for m in re.finditer(r'["\'](/api/[a-zA-Z0-9/_.?=&-]+)["\']', content):
    apis.add(m.group(1))

# 也搜索 sparta/ 路径
for m in re.finditer(r'(?:sparta|questiontraining)/[a-zA-Z0-9/_-]+', content):
    apis.add(m.group(0))

# 分类打印
answer_apis = sorted([a for a in apis if any(k in a.lower() for k in ['answer', '解析', 'resolve', 'explain', 'correct', 'result', 'submit', 'finish', 'end', 'check'])])
question_apis = sorted([a for a in apis if any(k in a.lower() for k in ['question', 'paper', 'test', 'detail']) and a not in answer_apis])
other_apis = sorted([a for a in apis if a not in answer_apis and a not in question_apis])

print(f'\n=== 答案/解析相关 API ({len(answer_apis)}) ===')
for a in answer_apis:
    print(f'  {a}')

print(f'\n=== 题目相关 API ({len(question_apis)}) ===')
for a in question_apis:
    print(f'  {a}')

print(f'\n=== 其他 API ({len(other_apis)}) ===')
for a in other_apis:
    print(f'  {a}')

# 也搜索 answer/correct 等关键词上下文
print('\n=== answer/correct 关键词上下文 ===')
for kw in ['answer', 'correct', '解析', 'rightAnswer', 'trueAnswer', 'showAnswer', 'submit', 'finish']:
    idx = content.find(kw)
    if idx >= 0:
        print(f'\n  {kw} @ {idx}:')
        print(f'  {content[max(0,idx-80):idx+150]}')
