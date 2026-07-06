import re
from curl_cffi import requests

# 下载 common.js
r = requests.get('https://static.nowcoder.com/fe/file/site/www-web/prod/1.0.484/lib/common.js', impersonate='chrome124', timeout=30)
content = r.text
print(f'common.js: {len(content)} chars')

# 搜索 answerContent 相关的 API（提交答案的 URL）
# API URL 可能直接硬编码在 common.js
print('\n=== common.js 中 answer 相关 API ===')
for m in re.finditer(r'["\'](/api/[a-zA-Z0-9/_.?=&-]*(?:answer|submit|question)[a-zA-Z0-9/_.?=&-]*)["\']', content, re.IGNORECASE):
    print(f'  {m.group(1)}')

# 搜索 test/ 系列 API
print('\n=== common.js 中 test/ API ===')
for m in re.finditer(r'["\'](/api/[a-zA-Z0-9/_.?=&-]*test[a-zA-Z0-9/_.?=&-]*)["\']', content, re.IGNORECASE):
    print(f'  {m.group(1)}')

# 搜索 answerContent
print('\n=== answerContent 上下文 ===')
for m in re.finditer('answerContent', content):
    chunk = content[max(0,m.start()-200):m.start()+100]
    if 'api' in chunk.lower() or 'post' in chunk.lower() or 'url' in chunk.lower():
        print(chunk[:300])
        print('---')

# 搜索 answerQuestion / submitAnswer / questionAnswer
for kw in ['answerQuestion', 'submitAnswer', 'questionAnswer', 'answer-question', 'submit-question', 'question-answer', 'common-practice/answer', 'common-practice/submit']:
    idx = content.find(kw)
    if idx >= 0:
        print(f'\n{kw} @ {idx}: {content[max(0,idx-100):idx+200]}')
