"""
测试答案获取：
1. pc-paper-begin 开始答题
2. test/detail 重新获取（begin 后可能有答案）
3. 探测 test/answer 等答案 API
"""
import json, time
from curl_cffi import requests

COOKIE = 'Hm_lvt_a808a1326b6c06c437de769d1b85b870=1783324773,1783326792,1783327040,1783332669; HMACCOUNT=5B50E5714BA2371A; NOWCODERCLINETID=5C624A404D820BAA561A9E407C597491; NOWCODERUID=99DB5E9FA741DBE9F474F73C04CD2DE0; acw_tc=0a18ab6c17833326692832986e66ad88590a1857ddae18de8424446dd7c7f2; isAgreementChecked=true; t=95DEC25319FA21258C369646734311BF; gr_user_id=8efaa278-603a-4231-b6df-e5959903fcdd; c196c3667d214851b11233f5c17f99d5_gr_session_id=697b7bd4-3ec7-4108-b9c0-d49935fc4cdb; Hm_lpvt_a808a1326b6c06c437de769d1b85b870=1783333797'

HEADERS = {
    'accept': 'application/json, text/plain, */*',
    'content-type': 'application/json',
    'origin': 'https://www.nowcoder.com',
    'referer': 'https://www.nowcoder.com/',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/150.0.0.0 Safari/537.36',
    'x-requested-with': 'XMLHttpRequest',
    'Cookie': COOKIE,
}

# 1. 创建试卷
body = {"tagIdSets":["570"],"classifyName":"    ","pageType":"intelligent_page","questionJobId":10}
r = requests.post('https://gw-c.nowcoder.com/api/sparta/common-practice/request-make-paper-pc',
                  json=body, headers=HEADERS, impersonate='chrome124', timeout=20)
data = r.json()['data']
pid, tid = data['paperId'], data['testId']
print(f'1. 创建试卷: paperId={pid}, testId={tid}')

# 2. pc-paper-begin
r = requests.post('https://gw-c.nowcoder.com/api/sparta/common-practice/pc-paper-begin',
                  json={'paperId': pid, 'testId': tid}, headers=HEADERS, impersonate='chrome124', timeout=15)
print(f'\n2. pc-paper-begin: {r.status_code} {r.text[:300]}')

# 3. test/begin
r = requests.post('https://gw-c.nowcoder.com/api/sparta/test/begin',
                  json={'testId': tid, 'paperId': pid}, headers=HEADERS, impersonate='chrome124', timeout=15)
print(f'\n3. test/begin: {r.status_code} {r.text[:200]}')

# 4. 重新 test/detail（begin 后可能有答案）
r = requests.post('https://gw-c.nowcoder.com/api/sparta/test/detail',
                  json={'testId': tid, 'paperId': pid}, headers=HEADERS, impersonate='chrome124', timeout=15)
detail = r.json().get('data', {})
questions = detail.get('paperQuestionDetails', [])
print(f'\n4. test/detail: {len(questions)} 题')
if questions:
    q0 = questions[0]
    # 检查是否有答案字段
    print(f'   题1 字段: {list(q0.keys())}')
    # 检查 chooseAnswer 是否有 correct/answer 字段
    if q0.get('chooseAnswer'):
        print(f'   选项字段: {list(q0["chooseAnswer"][0].keys())}')
    # 看完整第一题
    print(f'\n   题1 完整:')
    print(json.dumps(q0, ensure_ascii=False, indent=2)[:800])

# 5. 探测答案/解析 API
print('\n\n5. 探测答案 API ===')
quuid = questions[0]['uuid'] if questions else ''
answer_apis = [
    ('POST', f'https://gw-c.nowcoder.com/api/sparta/test/answer', {'testId': tid, 'questionUUID': quuid, 'paperId': pid}),
    ('POST', f'https://gw-c.nowcoder.com/api/sparta/test/get-answer', {'testId': tid, 'questionUUID': quuid}),
    ('POST', f'https://gw-c.nowcoder.com/api/sparta/test/show-answer', {'testId': tid, 'questionUUID': quuid}),
    ('POST', f'https://gw-c.nowcoder.com/api/sparta/test/question-answer', {'testId': tid, 'questionUUID': quuid}),
    ('POST', f'https://gw-c.nowcoder.com/api/sparta/test/analysis', {'testId': tid, 'questionUUID': quuid}),
    ('POST', f'https://gw-c.nowcoder.com/api/sparta/test/explain', {'testId': tid, 'questionUUID': quuid}),
    ('POST', f'https://gw-c.nowcoder.com/api/sparta/test/result', {'testId': tid}),
    ('POST', f'https://gw-c.nowcoder.com/api/sparta/test/finish', {'testId': tid, 'paperId': pid}),
    ('POST', f'https://gw-c.nowcoder.com/api/sparta/test/submit', {'testId': tid, 'paperId': pid}),
    ('POST', f'https://gw-c.nowcoder.com/api/sparta/test/end', {'testId': tid, 'paperId': pid}),
    # common-practice 路径
    ('POST', f'https://gw-c.nowcoder.com/api/sparta/common-practice/answer', {'testId': tid, 'questionUUID': quuid}),
    ('POST', f'https://gw-c.nowcoder.com/api/sparta/common-practice/get-answer', {'testId': tid, 'questionUUID': quuid}),
    ('POST', f'https://gw-c.nowcoder.com/api/sparta/common-practice/finish', {'testId': tid, 'paperId': pid}),
    ('POST', f'https://gw-c.nowcoder.com/api/sparta/common-practice/submit', {'testId': tid, 'paperId': pid}),
    ('POST', f'https://gw-c.nowcoder.com/api/sparta/common-practice/result', {'testId': tid}),
    ('POST', f'https://gw-c.nowcoder.com/api/sparta/common-practice/pc-paper-result', {'testId': tid, 'paperId': pid}),
    ('POST', f'https://gw-c.nowcoder.com/api/sparta/common-practice/paper-result', {'testId': tid, 'paperId': pid}),
]
for method, url, post_body in answer_apis:
    try:
        r = requests.post(url, json=post_body, headers=HEADERS, impersonate='chrome124', timeout=10)
        ct = r.headers.get('content-type', '')
        is_json = 'json' in ct
        has_data = is_json and ('"code":0' in r.text or '"success":true' in r.text) and len(r.text) > 80
        short = url.split('sparta/')[-1][:55]
        marker = ' ★★★' if has_data else (' ★' if is_json and r.status_code == 200 else '')
        if r.status_code != 404:
            print(f'  {r.status_code} {short}{marker}')
            if has_data:
                print(f'    => {r.text[:350]}'.replace('\n', ' '))
    except Exception as e:
        print(f'  ERR {url[-40:]}: {str(e)[:40]}')
