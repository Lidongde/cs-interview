"""
交卷后暴力测试 test/* 系列所有可能的答案 API
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

# 创建 + begin + finish
body = {"tagIdSets":["570"],"classifyName":"    ","pageType":"intelligent_page","questionJobId":10}
r = requests.post('https://gw-c.nowcoder.com/api/sparta/common-practice/request-make-paper-pc', json=body, headers=HEADERS, impersonate='chrome124', timeout=20)
data = r.json()['data']
pid, tid = data['paperId'], data['testId']
print(f'paperId={pid}, testId={tid}')

r = requests.post('https://gw-c.nowcoder.com/api/sparta/test/begin', json={'testId': tid, 'paperId': pid}, headers=HEADERS, impersonate='chrome124', timeout=15)
new_tid = r.json().get('data', {}).get('testId', tid)
print(f'begin testId={new_tid}')

# finish
r = requests.post('https://gw-c.nowcoder.com/api/sparta/test/finish', json={'testId': new_tid, 'paperId': pid}, headers=HEADERS, impersonate='chrome124', timeout=15)
print(f'finish: {r.text[:100]}')

# 暴力测试所有 test/* 答案 API
print('\n=== 暴力测试答案 API ===')
quuid = ''  # 获取第一题 uuid
r = requests.post('https://gw-c.nowcoder.com/api/sparta/test/detail', json={'testId': new_tid, 'paperId': pid}, headers=HEADERS, impersonate='chrome124', timeout=15)
detail = r.json().get('data', {})
questions = detail.get('paperQuestionDetails', [])
if questions:
    quuid = questions[0]['uuid']
    qid = questions[0]['id']
    print(f'第一题: uuid={quuid}, id={qid}')

answer_apis = [
    f'test/detail?testId={new_tid}&paperId={pid}&showAnswer=true',
    f'test/detail-paper?testId={new_tid}&paperId={pid}',
    f'test/result?testId={new_tid}&paperId={pid}',
    f'test/done?testId={new_tid}&paperId={pid}',
    f'test/answer?testId={new_tid}&questionUUID={quuid}',
    f'test/analysis?testId={new_tid}&questionUUID={quuid}',
    f'test/question-detail?testId={new_tid}&questionUUID={quuid}&paperId={pid}',
    f'test/question?testId={new_tid}&questionUUID={quuid}',
    f'test/get-question?testId={new_tid}&questionUUID={quuid}',
    # common-practice
    f'common-practice/paper-result?testId={new_tid}&paperId={pid}',
    f'common-practice/result?testId={new_tid}',
    f'common-practice/done?testId={new_tid}',
    f'common-practice/answer?testId={new_tid}&questionUUID={quuid}',
    f'common-practice/detail?testId={new_tid}&paperId={pid}',
    f'common-practice/get-paper?testId={new_tid}&paperId={pid}',
    # questiontraining
    f'questiontraining/intelligent/result?testId={new_tid}',
]

for path in answer_apis:
    url = f'https://gw-c.nowcoder.com/api/sparta/{path}' if not path.startswith('questiontraining') else f'https://www.nowcoder.com/api/{path}'
    for method in ['POST']:
        try:
            post_body = {'testId': new_tid, 'paperId': pid}
            if 'questionUUID' in path:
                post_body['questionUUID'] = quuid
            r = requests.post(url, json=post_body, headers=HEADERS, impersonate='chrome124', timeout=10)
            ct = r.headers.get('content-type', '')
            is_json = 'json' in ct
            has_data = is_json and ('"code":0' in r.text or '"success":true' in r.text) and len(r.text) > 80
            short = path[:55]
            if r.status_code != 404:
                marker = ' ★★★' if has_data else (' ★JSON' if is_json and r.status_code == 200 else '')
                print(f'  {r.status_code} {method} {short}{marker}')
                if has_data:
                    # 检查是否含 answer/analysis
                    if any(k in r.text for k in ['analysis', 'answer', 'correct', 'rightAnswer', 'referenceAnswer', '解析']):
                        print(f'    ★含答案! => {r.text[:400]}'.replace('\n',' '))
                    else:
                        print(f'    => {r.text[:200]}'.replace('\n',' '))
        except Exception as e:
            pass
