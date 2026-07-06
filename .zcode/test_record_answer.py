"""
测试 recordAnswer（提交答案）+ report/summary（获取答案解析）
"""
import json
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
r = requests.post('https://gw-c.nowcoder.com/api/sparta/common-practice/request-make-paper-pc', json=body, headers=HEADERS, impersonate='chrome124', timeout=20)
data = r.json()['data']
pid, tid = data['paperId'], data['testId']
print(f'paperId={pid}, testId={tid}')

# begin
r = requests.post('https://gw-c.nowcoder.com/api/sparta/test/begin', json={'testId': tid, 'paperId': pid}, headers=HEADERS, impersonate='chrome124', timeout=15)
new_tid = r.json().get('data', {}).get('testId', tid)
print(f'begin testId={new_tid}')

# 获取题目
r = requests.post('https://gw-c.nowcoder.com/api/sparta/test/detail', json={'testId': new_tid, 'paperId': pid}, headers=HEADERS, impersonate='chrome124', timeout=15)
detail = r.json()['data']
questions = detail['paperQuestionDetails']
q0 = questions[0]
print(f'\n题1: {q0["title"][:60]}')
print(f'  type={q0["type"]}, uuid={q0["uuid"]}, id={q0["id"]}')
print(f'  选项: {[(o["id"], o["content"]) for o in q0["chooseAnswer"]]}')

# 提交第一题答案（选第一个选项）
first_option_id = q0['chooseAnswer'][0]['id']
print(f'\n提交答案: questionId={q0["id"]}, answerContent={first_option_id}')
r = requests.post('https://gw-c.nowcoder.com/api/sparta/test/recordAnswer',
                  json={'questionId': q0['id'], 'paperId': pid, 'testId': new_tid, 'answerContent': str(first_option_id)},
                  headers=HEADERS, impersonate='chrome124', timeout=15)
print(f'recordAnswer: {r.status_code}')
print(f'  {r.text[:500]}'.replace('\n', ' '))

# 提交后再获取 detail，看是否有答案
r = requests.post('https://gw-c.nowcoder.com/api/sparta/test/detail', json={'testId': new_tid, 'paperId': pid}, headers=HEADERS, impersonate='chrome124', timeout=15)
detail2 = r.json()['data']
q0_after = detail2['paperQuestionDetails'][0]
print(f'\n提交后题1 字段: {list(q0_after.keys())}')
for key in ['analysis', 'referenceAnswer', 'rightAnswer', 'answer', 'userAnswerContent', 'questionStatus']:
    if key in q0_after and q0_after[key]:
        print(f'  ★ {key}: {str(q0_after[key])[:300]}')
# 检查选项是否有 correct
if q0_after.get('chooseAnswer'):
    print(f'  选项字段: {list(q0_after["chooseAnswer"][0].keys())}')
    for o in q0_after['chooseAnswer']:
        print(f'    {o}')

# 也测试 report / summary
print('\n=== test/report ===')
r = requests.post('https://gw-c.nowcoder.com/api/sparta/test/report', json={'testId': new_tid, 'paperId': pid}, headers=HEADERS, impersonate='chrome124', timeout=15)
print(f'  {r.status_code} {r.text[:400]}'.replace('\n', ' '))

print('\n=== test/summary ===')
r = requests.post('https://gw-c.nowcoder.com/api/sparta/test/summary', json={'testId': new_tid, 'paperId': pid}, headers=HEADERS, impersonate='chrome124', timeout=15)
print(f'  {r.status_code} {r.text[:400]}'.replace('\n', ' '))
