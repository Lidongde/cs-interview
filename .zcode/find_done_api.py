import re
from curl_cffi import requests
r = requests.get('https://static.nowcoder.com/fe/file/site/www-web/prod/1.0.484/page/examTest/main.entry.js', impersonate='chrome124', timeout=20)
content = r.text

# 找 doneQuestionData 是从哪里赋值的（API 调用）
# 搜索 doneQuestionData = 或 doneQuestionData: 或 SET_DONE
for kw in ['doneQuestionData=', 'doneQuestionData =', 'SET_DONE', 'setDoneQuestion', 'getDoneQuestion', 'fetchDone', 'donePaper', 'getDone', 'resultDetail', 'getResult', 'paperDetail', 'doneDetail']:
    idxs = [m.start() for m in re.finditer(re.escape(kw), content)]
    if idxs:
        print(f'=== {kw} ({len(idxs)}) ===')
        for i in idxs[:2]:
            print(f'  {content[max(0,i-100):i+200]}')
        print()

# 搜索 doneQuestionData 被赋值的地方
print('=== doneQuestionData 赋值 ===')
for m in re.finditer(r'doneQuestionData[:\s]*[=:]', content):
    chunk = content[max(0,m.start()-200):m.start()+200]
    if 'api' in chunk.lower() or 'post' in chunk.lower() or 'request' in chunk.lower() or 'dispatch' in chunk.lower():
        print(chunk[:400])
        print('---')

# 搜索 test/detail-paper（之前发现的 API）的响应是否含答案
# 还有 test/result, test/done
print('\n=== 搜索 done/result/answer API ===')
for m in re.finditer(r'["\'](/[a-zA-Z0-9/_-]*(?:done|result|answer|analysis)[a-zA-Z0-9/_-]*)["\']', content, re.IGNORECASE):
    print(f'  {m.group(1)}')
