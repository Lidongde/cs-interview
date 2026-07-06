"""
交卷后获取 test/detail，检查是否含答案和解析
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

# 创建 + begin + finish
body = {"tagIdSets":["570"],"classifyName":"    ","pageType":"intelligent_page","questionJobId":10}
r = requests.post('https://gw-c.nowcoder.com/api/sparta/common-practice/request-make-paper-pc', json=body, headers=HEADERS, impersonate='chrome124', timeout=20)
data = r.json()['data']
pid, tid = data['paperId'], data['testId']

r = requests.post('https://gw-c.nowcoder.com/api/sparta/test/begin', json={'testId': tid, 'paperId': pid}, headers=HEADERS, impersonate='chrome124', timeout=15)
new_tid = r.json().get('data', {}).get('testId', tid)

r = requests.post('https://gw-c.nowcoder.com/api/sparta/test/finish', json={'testId': new_tid, 'paperId': pid}, headers=HEADERS, impersonate='chrome124', timeout=15)
print(f'finish: {r.text[:80]}')

# 交卷后获取 detail
r = requests.post('https://gw-c.nowcoder.com/api/sparta/test/detail', json={'testId': new_tid, 'paperId': pid}, headers=HEADERS, impersonate='chrome124', timeout=15)
resp = r.json()
detail = resp.get('data', {})
questions = detail.get('paperQuestionDetails', [])
print(f'\n交卷后 detail: {len(questions)} 题')
print(f'paperSummary 字段: {list(detail.get("paperSummary", {}).keys())}')

if questions:
    q0 = questions[0]
    print(f'\n题1 所有字段: {list(q0.keys())}')
    # 检查答案相关字段
    for key in ['analysis', 'referenceAnswer', 'rightAnswer', 'answer', 'correctAnswer', 'answered', 'isCorrect', 'userAnswerContent', 'questionStatus']:
        if key in q0:
            val = q0[key]
            if val:
                print(f'\n  ★ {key}: {str(val)[:300]}')
    # 检查 chooseAnswer 是否有 correct 字段
    if q0.get('chooseAnswer'):
        opt0 = q0['chooseAnswer'][0]
        print(f'\n  选项字段: {list(opt0.keys())}')
        for opt in q0['chooseAnswer']:
            print(f'    {opt}')

    # 打印完整第一题
    print(f'\n=== 题1 完整 ===')
    print(json.dumps(q0, ensure_ascii=False, indent=2)[:1500])
