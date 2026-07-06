"""
1. 看 practiceHistory 完整响应
2. 探测分页
3. 查看所有历史试卷的 report
"""
import json, time
from curl_cffi import requests

COOKIE = 'Hm_lvt_a808a1326b6c06c437de769d1b85b870=1783324773; NOWCODERCLINETID=5C624A404D820BAA561A9E407C597491; NOWCODERUID=99DB5E9FA741DBE9F474F73C04CD2DE0; acw_tc=0a18ab6c17833326692832986e66ad88590a1857ddae18de8424446dd7c7f2; t=95DEC25319FA21258C369646734311BF'
HEADERS = {'accept':'application/json','content-type':'application/json','origin':'https://www.nowcoder.com','referer':'https://www.nowcoder.com/','user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36','x-requested-with':'XMLHttpRequest','Cookie':COOKIE}

# 完整响应
r = requests.get('https://www.nowcoder.com/api/questiontraining/intelligent/practiceHistory?subTabName=intelligent_page&questionJobId=10',
                 headers=HEADERS, impersonate='chrome124', timeout=15)
print('=== practiceHistory 完整响应 ===')
print(json.dumps(r.json(), ensure_ascii=False, indent=2)[:2000])

# 探测分页参数
print('\n=== 探测分页 ===')
for params in [
    '&pageNo=1&pageSize=100',
    '&page=1&size=100',
    '&offset=0&limit=100',
    '&pageNum=1&pageSize=100',
]:
    r2 = requests.get(f'https://www.nowcoder.com/api/questiontraining/intelligent/practiceHistory?subTabName=intelligent_page&questionJobId=10{params}',
                      headers=HEADERS, impersonate='chrome124', timeout=10)
    data = r2.json().get('data', [])
    print(f'  {params}: {len(data)} 条')

# 看每个历史试卷的 report
print('\n=== 每个历史试卷的 report ===')
history = r.json().get('data', [])
for h in history:
    tid, pid, name = h['id'], h['paperId'], h['name']
    r3 = requests.post('https://gw-c.nowcoder.com/api/sparta/test/report',
                       json={'testId': tid, 'paperId': pid}, headers=HEADERS, impersonate='chrome124', timeout=15)
    resp = r3.json().get('data', {})
    done_qs = resp.get('doneQuestionDetails', [])
    tags = [t.get('name') for t in resp.get('paperTags', [])]
    print(f'\n  {name} (testId={tid}): {len(done_qs)} 题, tags={tags}')
    if done_qs:
        q0 = done_qs[0]
        print(f'    题1: {q0.get("title","")[:50]}')
        print(f'    analysis: {str(q0.get("analysis",""))[:80]}')
