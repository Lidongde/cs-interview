"""
测试 /api/sparta/test/ 系列题目 API
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
pid, tid, uuid = data['paperId'], data['testId'], data['questionUUID']
print(f'paperId={pid}, testId={tid}, uuid={uuid}\n')

# 测试 /api/sparta/test/ 系列 API
ts = str(int(time.time()*1000))
test_apis = [
    ('GET', f'https://gw-c.nowcoder.com/api/sparta/test/detail?testId={tid}&_={ts}', None),
    ('GET', f'https://gw-c.nowcoder.com/api/sparta/test/detail-paper?testId={tid}&_={ts}', None),
    ('GET', f'https://gw-c.nowcoder.com/api/sparta/test/begin?testId={tid}&_={ts}', None),
    ('POST', f'https://gw-c.nowcoder.com/api/sparta/test/detail', {'testId': tid}),
    ('POST', f'https://gw-c.nowcoder.com/api/sparta/test/detail', {'testId': tid, 'paperId': pid}),
    ('POST', f'https://gw-c.nowcoder.com/api/sparta/test/detail-paper', {'testId': tid}),
    ('POST', f'https://gw-c.nowcoder.com/api/sparta/test/detail-paper', {'testId': tid, 'paperId': pid}),
    ('POST', f'https://gw-c.nowcoder.com/api/sparta/test/begin', {'testId': tid}),
    ('POST', f'https://gw-c.nowcoder.com/api/sparta/test/begin', {'testId': tid, 'paperId': pid}),
    ('POST', f'https://gw-c.nowcoder.com/api/sparta/test/begin', {'paperId': pid, 'testId': tid, 'questionUUID': uuid}),
]

for item in test_apis:
    method, url, post_body = item
    try:
        if method == 'GET':
            r = requests.get(url, headers=HEADERS, impersonate='chrome124', timeout=15)
        else:
            r = requests.post(url, json=post_body, headers=HEADERS, impersonate='chrome124', timeout=15)
        ct = r.headers.get('content-type', '')
        is_json = 'json' in ct
        has_data = is_json and ('"code":0' in r.text or '"success":true' in r.text) and len(r.text) > 80
        short = url.split('sparta/')[-1][:55] + (' POST' if method == 'POST' else '') + (f' body={json.dumps(post_body,ensure_ascii=False)}' if method=='POST' else '')
        marker = ' ★★★ 有数据' if has_data else (' ★ JSON' if is_json and r.status_code == 200 else '')
        print(f'{r.status_code} {method:4} {short}{marker}')
        if has_data:
            print(f'  => {r.text[:600]}'.replace('\n', ' '))
            print()
    except Exception as e:
        print(f'ERR {url[-50:]}: {str(e)[:50]}')
