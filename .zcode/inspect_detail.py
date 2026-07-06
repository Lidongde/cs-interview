"""
完整查看 test/detail 响应，确认题目结构
并找单题详情 API（含答案和解析）
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

# 创建试卷
body = {"tagIdSets":["570"],"classifyName":"    ","pageType":"intelligent_page","questionJobId":10}
r = requests.post('https://gw-c.nowcoder.com/api/sparta/common-practice/request-make-paper-pc',
                  json=body, headers=HEADERS, impersonate='chrome124', timeout=20)
data = r.json()['data']
pid, tid = data['paperId'], data['testId']
print(f'paperId={pid}, testId={tid}')

# 获取试卷详情
r = requests.post('https://gw-c.nowcoder.com/api/sparta/test/detail',
                  json={'testId': tid, 'paperId': pid}, headers=HEADERS, impersonate='chrome124', timeout=15)
detail = r.json()['data']
print(f'\n=== 试卷摘要 ===')
print(json.dumps(detail['paperSummary'], ensure_ascii=False, indent=2))

print(f'\n=== 题目列表 ({len(detail["paperQuestionDetails"])} 题) ===')
for i, q in enumerate(detail['paperQuestionDetails']):
    print(f'\n--- 题 {i+1} ---')
    print(json.dumps(q, ensure_ascii=False, indent=2)[:1000])

# 探测单题详情 API（含答案）
print('\n\n=== 探测单题详情 API（含答案）===')
first_q = detail['paperQuestionDetails'][0]
quuid = first_q['uuid']
qid = first_q['id']
single_apis = [
    ('POST', f'https://gw-c.nowcoder.com/api/sparta/test/question-detail', {'testId': tid, 'questionUUID': quuid, 'paperId': pid}),
    ('POST', f'https://gw-c.nowcoder.com/api/sparta/test/question', {'testId': tid, 'questionUUID': quuid}),
    ('POST', f'https://gw-c.nowcoder.com/api/sparta/test/get-question', {'testId': tid, 'questionUUID': quuid}),
    ('POST', f'https://gw-c.nowcoder.com/api/sparta/question/detail', {'questionUUID': quuid}),
    ('POST', f'https://gw-c.nowcoder.com/api/sparta/question/get-detail', {'questionUUID': quuid}),
    ('GET', f'https://gw-c.nowcoder.com/api/sparta/test/question-detail?testId={tid}&questionUUID={quuid}&paperId={pid}'),
    ('GET', f'https://gw-c.nowcoder.com/api/sparta/test/question?testId={tid}&questionUUID={quuid}'),
]
for method, url, *rest in [(a[0], a[1], a[2]) for a in single_apis]:
    post_body = rest[0] if rest else None
    try:
        if method == 'GET':
            r = requests.get(url, headers=HEADERS, impersonate='chrome124', timeout=10)
        else:
            r = requests.post(url, json=post_body, headers=HEADERS, impersonate='chrome124', timeout=10)
        ct = r.headers.get('content-type', '')
        is_json = 'json' in ct
        has_data = is_json and ('"code":0' in r.text or '"success":true' in r.text) and len(r.text) > 80
        short = url.split('sparta/')[-1][:50]
        marker = ' ★★★' if has_data else (' ★' if is_json and r.status_code == 200 else '')
        print(f'{r.status_code} {method:4} {short}{marker}')
        if has_data:
            print(f'  => {r.text[:400]}'.replace('\n', ' '))
    except Exception as e:
        print(f'ERR: {str(e)[:50]}')
