"""
测试 test/finish 完整响应（可能含答案）
并测试交卷后 test/detail 是否返回答案
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
print(f'1. 创建: paperId={pid}, testId={tid}')

# 2. test/begin
r = requests.post('https://gw-c.nowcoder.com/api/sparta/test/begin',
                  json={'testId': tid, 'paperId': pid}, headers=HEADERS, impersonate='chrome124', timeout=15)
begin_data = r.json().get('data', {})
new_tid = begin_data.get('testId', tid)
print(f'2. begin: new testId={new_tid}')

# 3. test/finish（交卷）
r = requests.post('https://gw-c.nowcoder.com/api/sparta/test/finish',
                  json={'testId': new_tid, 'paperId': pid}, headers=HEADERS, impersonate='chrome124', timeout=15)
print(f'\n3. test/finish: {r.status_code}')
finish_resp = r.json()
print(json.dumps(finish_resp, ensure_ascii=False, indent=2)[:1500])

# 4. finish 后再 test/detail（可能含答案）
r = requests.post('https://gw-c.nowcoder.com/api/sparta/test/detail',
                  json={'testId': new_tid, 'paperId': pid}, headers=HEADERS, impersonate='chrome124', timeout=15)
detail = r.json().get('data', {})
questions = detail.get('paperQuestionDetails', [])
print(f'\n4. finish 后 detail: {len(questions)} 题')
if questions:
    q0 = questions[0]
    print(f'   题1 字段: {list(q0.keys())}')
    if q0.get('chooseAnswer'):
        print(f'   选项字段: {list(q0["chooseAnswer"][0].keys())}')
        # 看选项是否有 correct/answer 字段
        print(f'   选项0: {json.dumps(q0["chooseAnswer"][0], ensure_ascii=False)}')
    # 检查新增字段
    for key in ['answer', 'correctAnswer', 'rightAnswer', 'analysis', 'explain', '解析', 'answered', 'isCorrect']:
        if key in q0:
            print(f'   ★ {key}: {q0[key]}')
    print(f'\n   题1 完整:')
    print(json.dumps(q0, ensure_ascii=False, indent=2)[:1000])
