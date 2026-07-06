import re
from curl_cffi import requests
r = requests.get('https://static.nowcoder.com/fe/file/site/www-web/prod/1.0.484/page/examTest/main.entry.js', impersonate='chrome124', timeout=20)
content = r.text

# 找 answerContent 附近的方法定义（提交答案的 API）
idx = content.find('answerContent:r')
if idx >= 0:
    # 向前找 API URL
    chunk = content[max(0, idx-600):idx+200]
    print('=== answerContent 上下文 ===')
    print(chunk)
    # 找 URL
    urls = re.findall(r'["\'](/[a-zA-Z0-9/_-]+)["\']', chunk)
    print(f'\n附近 URL: {urls}')

# 找 doneQuestionDetail / doneQuestionData 附近
print('\n=== doneQuestionDetail 附近 ===')
idx = content.find('doneQuestionDetail')
if idx >= 0:
    print(content[max(0,idx-300):idx+300])

# 找 isSubmission（提交后标志）
print('\n=== isSubmission 附近 ===')
for m in re.finditer('isSubmission', content):
    chunk = content[max(0,m.start()-100):m.start()+100]
    if 'answer' in chunk.lower() or 'detail' in chunk.lower() or 'api' in chunk.lower():
        print(chunk)
        print('---')

# 找 rightAnswer / correctOption
print('\n=== rightAnswer / officialAnswer 附近 ===')
for kw in ['rightAnswer', 'officialAnswer', 'correctOption', 'rightOption', 'answerOption', 'trueAnswer']:
    idx = content.find(kw)
    if idx >= 0:
        print(f'{kw}: {content[max(0,idx-80):idx+150]}')
