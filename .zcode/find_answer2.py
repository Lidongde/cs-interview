import re
from curl_cffi import requests
r = requests.get('https://static.nowcoder.com/fe/file/site/www-web/prod/1.0.484/page/examTest/main.entry.js', impersonate='chrome124', timeout=20)
content = r.text

# 找 "官方解析" 附近的数据字段（答案结构）
idx = content.find('官方解析')
if idx >= 0:
    print('=== 官方解析 上下文 ===')
    print(content[max(0,idx-400):idx+400])

# 找 doneQuestionData 附近（交卷结果数据）
print('\n=== doneQuestionData 附近 ===')
idx = content.find('doneQuestionData')
if idx >= 0:
    print(content[max(0,idx-200):idx+400])

# 找 answerContent 提交 API 的 URL
# Q.s2 是函数，找它的定义。搜索 s2: 或 s2= 或 function s2
print('\n=== 找提交答案 API URL ===')
# 搜索包含 answerContent 的 API 定义
for m in re.finditer(r'(?:post|request|axios|fetch)\s*\(\s*["\']([^"\']*(?:answer|submit|question)[^"\']*)["\']', content, re.IGNORECASE):
    print(f'  {m.group(1)}')

# 搜索 answer 相关的 /api/ 路径
for m in re.finditer(r'["\'](/api/[a-zA-Z0-9/_-]*(?:answer|submit|result|finish|end)[a-zA-Z0-9/_-]*)["\']', content, re.IGNORECASE):
    print(f'  API: {m.group(1)}')

# 搜索 doneTestPaper / getDonePaper / doneDetail
for kw in ['doneTestPaper', 'getDonePaper', 'doneDetail', 'getDoneDetail', 'paperResult', 'getPaperResult', 'answerDetail', 'getAnswerDetail', 'testResult', 'getTestResult']:
    idx = content.find(kw)
    if idx >= 0:
        print(f'\n{kw} @ {idx}: {content[max(0,idx-80):idx+200]}')
