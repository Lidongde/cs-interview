import re
from curl_cffi import requests
r = requests.get('https://static.nowcoder.com/fe/file/site/www-web/prod/1.0.484/page/examTest/main.entry.js', impersonate='chrome124', timeout=20)
content = r.text
for kw in ['showAnswer', 'rightAnswer', 'correctAnswer', 'getAnswer', 'answerContent', '解析', 'analysis', 'explain', 'isCorrect', 'isRight', 'correct', 'getQuestionAnswer', 'questionAnswer', 'answerDetail']:
    idxs = [m.start() for m in re.finditer(re.escape(kw), content)]
    if idxs:
        print(f'=== {kw} ({len(idxs)} hits) ===')
        for i in idxs[:2]:
            print(f'  ...{content[max(0,i-60):i+120]}...')
        print()
