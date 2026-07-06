"""
测试：不提交答案、不交卷，只 begin + detail 获取题目
看能否绕过"已做"限制获取更多题
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

# 连续创建 3 份试卷，不提交不交卷，只看题目
for i in range(3):
    r = requests.post('https://gw-c.nowcoder.com/api/sparta/common-practice/request-make-paper-pc',
                      json={"tagIdSets":["570"],"classifyName":"    ","pageType":"intelligent_page","questionJobId":10},
                      headers=HEADERS, impersonate='chrome124', timeout=20)
    data = r.json()
    print(f'\n试卷 {i+1}: {data.get("code")} {data.get("msg", "")[:60]}')
    if data.get('data'):
        pid = data['data']['paperId']
        tid = data['data']['testId']
        # begin
        r2 = requests.post('https://gw-c.nowcoder.com/api/sparta/test/begin',
                           json={'testId': tid, 'paperId': pid}, headers=HEADERS, impersonate='chrome124', timeout=15)
        real_tid = r2.json().get('data', {}).get('testId', tid)
        # detail（不提交不交卷）
        r3 = requests.post('https://gw-c.nowcoder.com/api/sparta/test/detail',
                           json={'testId': real_tid, 'paperId': pid}, headers=HEADERS, impersonate='chrome124', timeout=15)
        qs = r3.json().get('data', {}).get('paperQuestionDetails', [])
        print(f'  题目数: {len(qs)}')
        for q in qs:
            print(f'    [{q["type"]}] {q["title"][:50]}')
    time.sleep(0.5)
