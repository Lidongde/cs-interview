import re
with open(r'D:/Workspace/Project/cs-interview/.zcode/nowcoder_main.js', 'r', encoding='utf-8', errors='ignore') as f:
    s = f.read()
# 搜索 startPractice 附近的代码
for kw in ['startPractice', 'fetchTagData', 'singleTagPaper', 'exam/test', '/exam/', 'question-list', 'paperId', 'test?tagId', 'intelligent']:
    idxs = [m.start() for m in re.finditer(re.escape(kw), s)]
    print(f'=== {kw}: {len(idxs)} hits ===')
    for i in idxs[:3]:
        print(s[max(0,i-80):i+200].replace('\n',' '))
        print('---')
