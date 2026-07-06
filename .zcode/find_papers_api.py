"""
1. 从 SSR store 找刷题记录的 API URL
2. 从 users/main.entry.js 找 prefetchData.2 对应的 API
3. 测试分页
"""
import re, json
from curl_cffi import requests

COOKIE = 'Hm_lvt_a808a1326b6c06c437de769d1b85b870=1783324773; NOWCODERCLINETID=5C624A404D820BAA561A9E407C597491; NOWCODERUID=99DB5E9FA741DBE9F474F73C04CD2DE0; acw_tc=0a18ab6c17833326692832986e66ad88590a1857ddae18de8424446dd7c7f2; t=95DEC25319FA21258C369646734311BF'
HEADERS = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36', 'Cookie': COOKIE,
           'accept': 'application/json', 'x-requested-with': 'XMLHttpRequest',
           'origin': 'https://www.nowcoder.com', 'referer': 'https://www.nowcoder.com/users/77826278/tests'}

# 1. 从 JS 找 prefetchData key "2" 对应的 API
r = requests.get('https://static.nowcoder.com/fe/file/site/www-web/prod/1.0.484/page/users/main.entry.js',
                 impersonate='chrome124', timeout=20)
content = r.text

# prefetchData 的 key "2" 通常对应某个 asyncData fetch
# 搜索 test-papers / testHistory / getTests 等
print('=== JS 中刷题记录相关 ===')
for kw in ['test-papers', 'testPapers', 'getTests', 'getTestList', 'testList', 'paperList', 'submissionHistory', 'practiceHistory', 'training-history', 'question-training']:
    idxs = [m.start() for m in re.finditer(kw, content, re.IGNORECASE)]
    if idxs:
        print(f'\n{kw} ({len(idxs)} hits):')
        for i in idxs[:1]:
            print(f'  {content[max(0,i-150):i+200]}')

# 2. 直接测试分页 API（从 common.js 找到的 getTestPapers 路径）
# common.js 里有: getTestPapers:"/profile/#{uid}/test-papers"
print('\n=== 测试 /profile/uid/test-papers ===')
r2 = requests.get('https://www.nowcoder.com/api/profile/77826278/test-papers?pageNo=1&pageSize=50',
                  headers=HEADERS, impersonate='chrome124', timeout=15)
print(f'  status={r2.status_code}, len={len(r2.text)}')
print(f'  {r2.text[:500]}'.replace('\n',' '))

# 3. 也试 wrong-questions 路径
print('\n=== /profile/uid/wrong-questions ===')
r3 = requests.get('https://www.nowcoder.com/api/profile/77826278/wrong-questions?pageNo=1&pageSize=50',
                  headers=HEADERS, impersonate='chrome124', timeout=15)
print(f'  status={r3.status_code}, len={len(r3.text)}')
print(f'  {r3.text[:300]}'.replace('\n',' '))
