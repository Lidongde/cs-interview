"""
1. 检查已爬到的 Java 题目中 isMember 情况
2. 探测"全部题目"/"错题本"API
3. 尝试 reset/retry 已做题目
"""
import json
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

# 1. 检查已爬题目的 isMember
with open(r'D:/Workspace/Project/cs-interview/nowcoder_data/570_Java.json', 'r', encoding='utf-8') as f:
    questions = json.load(f)
member_count = sum(1 for q in questions if q.get('isMember'))
no_analysis = sum(1 for q in questions if not q.get('analysis'))
print(f'Java 已爬 {len(questions)} 题')
print(f'  isMember=true: {member_count}')
print(f'  无解析: {no_analysis}')

# 2. 探测错题本/收藏/全部题目 API
print('\n=== 探测其他题目 API ===')
test_apis = [
    ('GET', 'https://gw-c.nowcoder.com/api/sparta/test/wrong-questions?tagId=570'),
    ('GET', 'https://gw-c.nowcoder.com/api/sparta/test/wrongQuestions?tagId=570'),
    ('GET', 'https://gw-c.nowcoder.com/api/sparta/question/wrong?tagId=570'),
    ('GET', 'https://gw-c.nowcoder.com/api/sparta/common-practice/wrong-questions?tagId=570'),
    ('GET', 'https://gw-c.nowcoder.com/api/sparta/common-practice/question-list?tagId=570&pageNo=1&pageSize=20'),
    ('GET', 'https://gw-c.nowcoder.com/api/sparta/common-practice/all-questions?tagId=570'),
    ('GET', 'https://gw-c.nowcoder.com/api/sparta/question-bank/list?tagId=570&pageNo=1&pageSize=20'),
    # 搜索 API（可能返回题目列表）
    ('GET', 'https://gw-c.nowcoder.com/api/sparta/search/suggest?keyword=Java&tagId=570'),
    # 重新练习（重置已做记录）
    ('POST', 'https://gw-c.nowcoder.com/api/sparta/common-practice/reset?tagId=570'),
    ('POST', 'https://gw-c.nowcoder.com/api/sparta/common-practice/reset-progress?tagId=570'),
    # 用 continue API 获取继续练习的试卷
    ('GET', 'https://www.nowcoder.com/api/questiontraining/intelligent/continue?subTabName=intelligent_page&questionJobId=10&tagId=570'),
]
for item in test_apis:
    method = item[0]
    url = item[1]
    try:
        if method == 'GET':
            r = requests.get(url, headers=HEADERS, impersonate='chrome124', timeout=10)
        else:
            r = requests.post(url, json={'tagId': 570}, headers=HEADERS, impersonate='chrome124', timeout=10)
        ct = r.headers.get('content-type', '')
        is_json = 'json' in ct
        has_data = is_json and ('"code":0' in r.text or '"success":true' in r.text) and len(r.text) > 80
        short = url.split('sparta/')[-1][:55] if 'sparta/' in url else url.split('api/')[-1][:55]
        if r.status_code != 404:
            marker = ' ★' if has_data else (' JSON' if is_json else '')
            print(f'  {r.status_code} {method} {short}{marker}')
            if has_data:
                print(f'    => {r.text[:200]}'.replace('\n',' '))
    except Exception as e:
        print(f'  ERR {url[-40:]}: {str(e)[:40]}')
