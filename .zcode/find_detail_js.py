"""
获取正确答题页 /exam/test/{testId}/detail 的 HTML 和 JS
"""
import re, json, time
from curl_cffi import requests

COOKIE = 'Hm_lvt_a808a1326b6c06c437de769d1b85b870=1783324773,1783326792,1783327040,1783332669; HMACCOUNT=5B50E5714BA2371A; NOWCODERCLINETID=5C624A404D820BAA561A9E407C597491; NOWCODERUID=99DB5E9FA741DBE9F474F73C04CD2DE0; acw_tc=0a18ab6c17833326692832986e66ad88590a1857ddae18de8424446dd7c7f2; isAgreementChecked=true; t=95DEC25319FA21258C369646734311BF; gr_user_id=8efaa278-603a-4231-b6df-e5959903fcdd; c196c3667d214851b11233f5c17f99d5_gr_session_id=697b7bd4-3ec7-4108-b9c0-d49935fc4cdb; Hm_lpvt_a808a1326b6c06c437de769d1b85b870=1783333797'

HEADERS = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/150.0.0.0 Safari/537.36',
    'Cookie': COOKIE,
}

# 先创建试卷
body = {"tagIdSets":["570"],"classifyName":"    ","pageType":"intelligent_page","questionJobId":10}
r = requests.post('https://gw-c.nowcoder.com/api/sparta/common-practice/request-make-paper-pc',
                  json=body, headers={**HEADERS, 'content-type': 'application/json', 'x-requested-with': 'XMLHttpRequest', 'origin': 'https://www.nowcoder.com', 'referer': 'https://www.nowcoder.com/'},
                  impersonate='chrome124', timeout=20)
data = r.json()['data']
tid = data['testId']
print(f'testId={tid}')

# 获取答题页 HTML
r = requests.get(f'https://www.nowcoder.com/exam/test/{tid}/detail',
                 headers=HEADERS, impersonate='chrome124', timeout=15)
print(f'答题页 status={r.status_code}, len={len(r.text)}')
print(f'title: {re.search(r"<title>(.*?)</title>", r.text).group(1) if re.search(r"<title>(.*?)</title>", r.text) else "none"}')

# 找 JS
js_srcs = re.findall(r'src="([^"]+\.js[^"]*)"', r.text)
print(f'\nJS 文件 ({len(js_srcs)}):')
for s in js_srcs:
    print(f'  {s}')

# 找 main.entry
main_jss = [s for s in js_srcs if 'main' in s or 'test' in s or 'exam' in s or 'detail' in s]
print(f'\n主 JS: {main_jss}')

# 下载所有 JS 搜索题目 API
for u in js_srcs:
    if not u.startswith('http'):
        u = 'https:' + u if u.startswith('//') else 'https://www.nowcoder.com' + u
    try:
        rj = requests.get(u, headers=HEADERS, impersonate='chrome124', timeout=20)
        if rj.status_code != 200: continue
        content = rj.text
        if len(content) < 1000: continue
        # 搜索所有 /api/ 路径
        apis = set(re.findall(r'["\'](/api/[a-zA-Z0-9/_.?=&-]+)["\']', content))
        # 过滤题目相关
        q_apis = [a for a in apis if any(k in a.lower() for k in ['question', 'paper', 'exam', 'practice', 'test', 'answer', 'detail', 'content'])]
        # 搜索 request-make-paper
        has_make_paper = 'request-make-paper' in content or 'make-paper' in content
        if q_apis or has_make_paper:
            fname = u.split('/')[-1].split('?')[0]
            print(f'\n  [{fname}] ({len(content)} chars)')
            if has_make_paper:
                print(f'    ★ 含 request-make-paper')
            for a in sorted(q_apis):
                print(f'    {a}')
    except: pass
