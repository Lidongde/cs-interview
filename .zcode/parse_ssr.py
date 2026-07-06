"""
正确解析 __INITIAL_STATE__，找刷题记录数据
"""
import re, json
from curl_cffi import requests

COOKIE = 'Hm_lvt_a808a1326b6c06c437de769d1b85b870=1783324773; NOWCODERCLINETID=5C624A404D820BAA561A9E407C597491; NOWCODERUID=99DB5E9FA741DBE9F474F73C04CD2DE0; acw_tc=0a18ab6c17833326692832986e66ad88590a1857ddae18de8424446dd7c7f2; t=95DEC25319FA21258C369646734311BF'
HEADERS = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36', 'Cookie': COOKIE}

r = requests.get('https://www.nowcoder.com/users/77826278/tests',
                 headers=HEADERS, impersonate='chrome124', timeout=15)
html = r.text

# 提取 __INITIAL_STATE__（到分号结尾）
m = re.search(r'window\.__INITIAL_STATE__\s*=\s*(\{.*?\})\s*;', html, re.DOTALL)
if not m:
    # 尝试到下一个 window 赋值
    m = re.search(r'window\.__INITIAL_STATE__\s*=\s*(\{.*?\})\s*\nwindow\.', html, re.DOTALL)

if m:
    raw = m.group(1)
    print(f'__INITIAL_STATE__ 长度: {len(raw)}')
    # 尝试解析（可能有 \u002F 等转义）
    try:
        state = json.loads(raw)
    except:
        # 替换 unicode 转义
        raw2 = raw.replace('\\u002F', '/')
        state = json.loads(raw2)

    print(f'顶层 keys: {list(state.keys())}')

    # 递归找含 testId/paperId 的列表
    def find_test_papers(obj, path=''):
        if isinstance(obj, dict):
            keys = list(obj.keys())
            # 检查是否是试卷记录
            if 'paperId' in keys or ('id' in keys and 'name' in keys and 'paperId' not in keys):
                if 'paperId' in keys:
                    print(f'\n★ 试卷记录 @ {path}:')
                    print(f'  {json.dumps(obj, ensure_ascii=False)[:300]}')
            for k, v in obj.items():
                find_test_papers(v, f'{path}.{k}')
        elif isinstance(obj, list):
            if len(obj) > 0 and isinstance(obj[0], dict):
                # 检查列表项是否含 testId/paperId
                if any('paperId' in item for item in obj[:3]):
                    print(f'\n★ 试卷列表 @ {path}: {len(obj)} 项')
                    for item in obj[:3]:
                        print(f'  {json.dumps(item, ensure_ascii=False)[:200]}')
            for i, item in enumerate(obj[:5]):
                find_test_papers(item, f'{path}[{i}]')

    find_test_papers(state)

    # 也搜索含 "专项练习" 或 "Java" 的数据
    def search_text(obj, path=''):
        if isinstance(obj, str):
            if '专项练习' in obj or ('Java' in obj and 'test' in path.lower()):
                print(f'\n文本 @ {path}: {obj[:100]}')
        elif isinstance(obj, dict):
            for k, v in obj.items():
                search_text(v, f'{path}.{k}')
        elif isinstance(obj, list):
            for i, item in enumerate(obj[:10]):
                search_text(item, f'{path}[{i}]')
    search_text(state)
else:
    print('未找到 __INITIAL_STATE__')
    # 找其他数据注入
    for pattern in [r'window\.pageData\s*=\s*(\{.*?\});', r'window\.envInfo\s*=\s*(\{.*?\});']:
        m = re.search(pattern, html, re.DOTALL)
        if m:
            print(f'找到: {m.group(0)[:200]}')
