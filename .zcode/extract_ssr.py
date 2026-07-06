"""
1. 提取 __INITIAL_STATE__ 里的刷题数据
2. 找到正确的分页 API
"""
import re, json
from curl_cffi import requests

COOKIE = 'Hm_lvt_a808a1326b6c06c437de769d1b85b870=1783324773; NOWCODERCLINETID=5C624A404D820BAA561A9E407C597491; NOWCODERUID=99DB5E9FA741DBE9F474F73C04CD2DE0; acw_tc=0a18ab6c17833326692832986e66ad88590a1857ddae18de8424446dd7c7f2; t=95DEC25319FA21258C369646734311BF'
HEADERS = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/150.0.0.0 Safari/537.36',
    'Cookie': COOKIE,
}

# 获取 HTML 提取 __INITIAL_STATE__
r = requests.get('https://www.nowcoder.com/users/77826278/tests',
                 headers=HEADERS, impersonate='chrome124', timeout=15)
html = r.text

# 提取 __INITIAL_STATE__
m = re.search(r'window\.__INITIAL_STATE__\s*=\s*(\{.*?\});\s*</script>', html, re.DOTALL)
if not m:
    m = re.search(r'window\.__INITIAL_STATE__\s*=\s*(\{.*?\})\s*$', html, re.MULTILINE)
if m:
    try:
        state = json.loads(m.group(1))
        print(f'__INITIAL_STATE__ keys: {list(state.keys())}')
        # 找刷题数据
        def find_tests(obj, path=''):
            if isinstance(obj, dict):
                for k, v in obj.items():
                    if 'test' in k.lower() or 'paper' in k.lower() or 'question' in k.lower():
                        if isinstance(v, list) and len(v) > 0:
                            print(f'  {path}.{k}: list[{len(v)}], 第一项 keys={list(v[0].keys()) if isinstance(v[0],dict) else type(v[0])}')
                            if isinstance(v[0], dict):
                                print(f'    第一项: {json.dumps(v[0], ensure_ascii=False)[:200]}')
                    find_tests(v, f'{path}.{k}')
            elif isinstance(obj, list):
                for i, item in enumerate(obj[:3]):
                    find_tests(item, f'{path}[{i}]')
        find_tests(state)
    except Exception as e:
        print(f'解析失败: {e}')
        print(f'前500字符: {m.group(1)[:500]}')
else:
    print('未找到 __INITIAL_STATE__')

# 找 users/main.entry.js 里的 API
print('\n=== users/main.entry.js API ===')
r2 = requests.get('https://static.nowcoder.com/fe/file/site/www-web/prod/1.0.484/page/users/main.entry.js',
                  headers=HEADERS, impersonate='chrome124', timeout=20)
content = r2.text
print(f'JS 大小: {len(content)}')

# 找 test/paper/history 相关 API
apis = set()
for m in re.finditer(r'["\'](/api/[a-zA-Z0-9/_.?=&-]+)["\']', content):
    a = m.group(1)
    if any(k in a.lower() for k in ['test', 'paper', 'history', 'wrong', 'practice', 'question']):
        apis.add(a)
for a in sorted(apis):
    print(f'  {a}')

# 找 testHistory 上下文
for kw in ['testHistory', 'test-history', 'getTests', 'testPapers', 'wrongQuestions']:
    idx = content.find(kw)
    if idx >= 0:
        print(f'\n{kw} @ {idx}: {content[max(0,idx-100):idx+200]}')
