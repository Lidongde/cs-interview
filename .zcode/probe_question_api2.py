"""
用 curl_cffi 创建试卷后，全面探测题目内容 API
包括用 questionUUID、paperId、testId 各种组合
"""
import json, time
from curl_cffi import requests

COOKIE = 'Hm_lvt_a808a1326b6c06c437de769d1b85b870=1783324773,1783326792,1783327040,1783332669; HMACCOUNT=5B50E5714BA2371A; NOWCODERCLINETID=5C624A404D820BAA561A9E407C597491; NOWCODERUID=99DB5E9FA741DBE9F474F73C04CD2DE0; acw_tc=0a18ab6c17833326692832986e66ad88590a1857ddae18de8424446dd7c7f2; isAgreementChecked=true; t=95DEC25319FA21258C369646734311BF; gr_user_id=8efaa278-603a-4231-b6df-e5959903fcdd; c196c3667d214851b11233f5c17f99d5_gr_session_id=697b7bd4-3ec7-4108-b9c0-d49935fc4cdb; c196c3667d214851b11233f5c17f99d5_gr_session_id_697b7bd4-3ec7-4108-b9c0-d49935fc4cdb=true; c196c3667d214851b11233f5c17f99d5_gr_last_sent_sid_with_cs1=697b7bd4-3ec7-4108-b9c0-d49935fc4cdb; c196c3667d214851b11233f5c17f99d5_gr_last_sent_cs1=77826278; Hm_lpvt_a808a1326b6c06c437de769d1b85b870=1783333797; c196c3667d214851b11233f5c17f99d5_gr_cs1=77826278'

HEADERS = {
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'zh-CN,zh;q=0.9',
    'content-type': 'application/json',
    'origin': 'https://www.nowcoder.com',
    'referer': 'https://www.nowcoder.com/',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/150.0.0.0 Safari/537.36',
    'x-requested-with': 'XMLHttpRequest',
    'Cookie': COOKIE,
}

# 创建试卷
print('=== 创建试卷 ===')
body = {"tagIdSets":["570"],"classifyName":"    ","pageType":"intelligent_page","questionJobId":10}
r = requests.post('https://gw-c.nowcoder.com/api/sparta/common-practice/request-make-paper-pc',
                  json=body, headers=HEADERS, impersonate='chrome124', timeout=20)
data = r.json()['data']
pid, tid, uuid = data['paperId'], data['testId'], data['questionUUID']
print(f'paperId={pid}, testId={tid}, uuid={uuid}')

# 全面探测题目内容 API
print('\n=== 探测题目内容 API ===')
ts = str(int(time.time()*1000))
candidates = [
    # common-practice 各种路径
    ('GET', f'https://gw-c.nowcoder.com/api/sparta/common-practice/paper-info?paperId={pid}&testId={tid}'),
    ('GET', f'https://gw-c.nowcoder.com/api/sparta/common-practice/get-paper-info?paperId={pid}'),
    ('GET', f'https://gw-c.nowcoder.com/api/sparta/common-practice/question?paperId={pid}&testId={tid}'),
    ('GET', f'https://gw-c.nowcoder.com/api/sparta/common-practice/question?questionUUID={uuid}'),
    ('GET', f'https://gw-c.nowcoder.com/api/sparta/common-practice/get-question?questionUUID={uuid}'),
    ('GET', f'https://gw-c.nowcoder.com/api/sparta/common-practice/question-detail?questionUUID={uuid}'),
    ('GET', f'https://gw-c.nowcoder.com/api/sparta/common-practice/get-question-detail?questionUUID={uuid}'),
    ('GET', f'https://gw-c.nowcoder.com/api/sparta/common-practice/paper-question?paperId={pid}'),
    ('GET', f'https://gw-c.nowcoder.com/api/sparta/common-practice/paper-question-list?paperId={pid}'),
    ('GET', f'https://gw-c.nowcoder.com/api/sparta/common-practice/get-paper-question?paperId={pid}'),
    # POST 方式
    ('POST', f'https://gw-c.nowcoder.com/api/sparta/common-practice/paper-info', {'paperId': pid, 'testId': tid}),
    ('POST', f'https://gw-c.nowcoder.com/api/sparta/common-practice/get-paper-info', {'paperId': pid}),
    ('POST', f'https://gw-c.nowcoder.com/api/sparta/common-practice/question', {'questionUUID': uuid}),
    ('POST', f'https://gw-c.nowcoder.com/api/sparta/common-practice/get-question', {'questionUUID': uuid}),
    ('POST', f'https://gw-c.nowcoder.com/api/sparta/common-practice/question-detail', {'questionUUID': uuid}),
    # 用 questionUUID 做路径参数
    ('GET', f'https://gw-c.nowcoder.com/api/sparta/common-practice/question/{uuid}'),
    ('GET', f'https://gw-c.nowcoder.com/api/sparta/common-practice/paper/{pid}'),
    # practice 路径
    ('GET', f'https://gw-c.nowcoder.com/api/sparta/practice/paper?paperId={pid}&testId={tid}'),
    ('GET', f'https://gw-c.nowcoder.com/api/sparta/practice/question?questionUUID={uuid}'),
    ('GET', f'https://gw-c.nowcoder.com/api/sparta/practice/get-question?questionUUID={uuid}'),
    # test 路径
    ('GET', f'https://gw-c.nowcoder.com/api/sparta/test/paper?testId={tid}'),
    ('GET', f'https://gw-c.nowcoder.com/api/sparta/test/question?testId={tid}'),
    ('GET', f'https://gw-c.nowcoder.com/api/sparta/test/get-questions?testId={tid}'),
    # question-bank
    ('GET', f'https://gw-c.nowcoder.com/api/sparta/question-bank/question?questionUUID={uuid}'),
    ('GET', f'https://gw-c.nowcoder.com/api/sparta/question-bank/get-question?questionUUID={uuid}'),
]

for item in candidates:
    method, url = item[0], item[1]
    body_p = item[2] if len(item) > 2 else None
    try:
        if method == 'GET':
            r = requests.get(url, headers=HEADERS, impersonate='chrome124', timeout=10)
        else:
            r = requests.post(url, json=body_p, headers=HEADERS, impersonate='chrome124', timeout=10)
        ct = r.headers.get('content-type', '')
        is_waf = 'aliyun_waf' in r.text[:300]
        is_json = 'json' in ct and not is_waf
        has_real_data = is_json and ('"code":0' in r.text or '"success":true' in r.text) and len(r.text) > 50
        short = url.split('sparta/')[-1][:60] if 'sparta/' in url else url[-60:]
        marker = ' ★有数据' if has_real_data else ''
        if r.status_code != 404 or has_real_data:
            print(f'  {r.status_code} {method} {short}{marker}')
            if has_real_data:
                print(f'      => {r.text[:300]}'.replace('\n',' '))
    except Exception as e:
        pass
