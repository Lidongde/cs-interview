import re
with open(r'D:/Workspace/Project/cs-interview/.zcode/nowcoder_main.js', 'r', encoding='utf-8', errors='ignore') as f:
    s = f.read()
patterns = [
    r'"/[a-zA-Z0-9/_-]*question[a-zA-Z0-9/_-]*"',
    r'"/[a-zA-Z0-9/_-]*exam[a-zA-Z0-9/_-]*"',
    r'"/[a-zA-Z0-9/_-]*practice[a-zA-Z0-9/_-]*"',
    r'"/[a-zA-Z0-9/_-]*paper[a-zA-Z0-9/_-]*"',
    r'"/[a-zA-Z0-9/_-]*tag[a-zA-Z0-9/_-]*"',
    r'sparta[a-zA-Z0-9/_.-]*',
]
for p in patterns:
    found = sorted(set(re.findall(p, s, re.IGNORECASE)))
    if found:
        print('--- pattern:', p[:40])
        for x in found[:25]:
            print(x)
