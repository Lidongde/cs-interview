import json
with open(r'D:/Workspace/Project/cs-interview/.zcode/nowcoder_cookies.json', 'r', encoding='utf-8') as f:
    d = json.load(f)
print('全部 cookie:')
for c in d['cookies']:
    v = c['value']
    print(f'  {c["domain"]:25} {c["name"]:25} = {v[:25]}{"..." if len(v)>25 else ""}')
print()
print('cookie_string:')
print(d['cookie_string'][:300])
