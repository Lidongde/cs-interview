"""
从 practiceHistory 获取所有历史试卷，用 test/report 提取题目
这个方式能获取所有已做过的题目（包括之前爬虫交卷的 399 题）
"""
import json, time
from curl_cffi import requests

COOKIE = 'Hm_lvt_a808a1326b6c06c437de769d1b85b870=1783324773; NOWCODERCLINETID=5C624A404D820BAA561A9E407C597491; NOWCODERUID=99DB5E9FA741DBE9F474F73C04CD2DE0; acw_tc=0a18ab6c17833326692832986e66ad88590a1857ddae18de8424446dd7c7f2; t=95DEC25319FA21258C369646734311BF'
HEADERS = {
    'accept': 'application/json, text/plain, */*',
    'content-type': 'application/json',
    'origin': 'https://www.nowcoder.com',
    'referer': 'https://www.nowcoder.com/',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/150.0.0.0 Safari/537.36',
    'x-requested-with': 'XMLHttpRequest',
    'Cookie': COOKIE,
}

# 1. 获取全部练习历史
print('=== 获取练习历史 ===')
r = requests.get('https://www.nowcoder.com/api/questiontraining/intelligent/practiceHistory?subTabName=intelligent_page&questionJobId=10',
                 headers=HEADERS, impersonate='chrome124', timeout=15)
history = r.json().get('data', [])
print(f'历史记录数: {len(history)}')

# 按标签分组
by_tag = {}
for h in history:
    name = h.get('name', '')
    # 解析标签名："专项练习-Java" → "Java"
    tag_name = name.replace('专项练习-', '').split('-')[0] if '专项练习-' in name else name
    tid = h.get('id')
    pid = h.get('paperId')
    by_tag.setdefault(tag_name, []).append({'testId': tid, 'paperId': pid, 'name': name, 'status': h.get('status')})

for tag, papers in by_tag.items():
    print(f'  {tag}: {len(papers)} 份试卷')

# 2. 对第一份 Java 试卷调用 test/report，看返回的题目结构
java_papers = by_tag.get('Java', []) or by_tag.get('java', [])
if not java_papers:
    # 找含 Java 的
    for tag, papers in by_tag.items():
        if 'Java' in tag or 'java' in tag.lower():
            java_papers = papers
            break

if java_papers:
    p = java_papers[0]
    print(f'\n=== 第一份试卷: {p["name"]} (testId={p["testId"]}, paperId={p["paperId"]}) ===')
    r = requests.post('https://gw-c.nowcoder.com/api/sparta/test/report',
                      json={'testId': p['testId'], 'paperId': p['paperId']},
                      headers=HEADERS, impersonate='chrome124', timeout=15)
    resp = r.json()
    if resp.get('data'):
        done_qs = resp['data'].get('doneQuestionDetails', [])
        print(f'题目数: {len(done_qs)}')
        if done_qs:
            q0 = done_qs[0]
            print(f'题1 字段: {list(q0.keys())}')
            print(f'题1 标题: {q0.get("title","")[:60]}')
            print(f'题1 analysis: {str(q0.get("analysis",""))[:100]}')
            print(f'题1 referenceAnswer: {q0.get("referenceAnswer","")[:100]}')
            print(f'题1 options: {len(q0.get("answers",q0.get("chooseAnswer",[])))}')
