"""
探查做题记录页面的 API
URL: /exam/test/97744141/submission?pid=67856839&pageSource=testHistory
"""
import json, time
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

TID = 97744141  # testId
PID = 67856839  # paperId

# 1. 获取做题记录页 HTML，找 JS bundle
print('=== 1. 做题记录页 HTML ===')
r = requests.get(f'https://www.nowcoder.com/exam/test/{TID}/submission?pid={PID}&pageSource=testHistory',
                 headers={**HEADERS, 'accept': 'text/html'}, impersonate='chrome124', timeout=15)
print(f'  status={r.status_code}, len={len(r.text)}')
import re
title = re.search(r'<title>(.*?)</title>', r.text)
print(f'  title: {title.group(1) if title else "none"}')
js_srcs = re.findall(r'src="([^"]+\.js[^"]*)"', r.text)
print(f'  JS: {js_srcs}')

# 2. 探测做题记录相关 API
print('\n=== 2. 探测做题记录 API ===')
candidates = [
    # submission 相关
    ('GET', f'https://gw-c.nowcoder.com/api/sparta/test/submission?testId={TID}&paperId={PID}'),
    ('GET', f'https://gw-c.nowcoder.com/api/sparta/test/submission-list?testId={TID}&paperId={PID}'),
    ('GET', f'https://gw-c.nowcoder.com/api/sparta/test/history?testId={TID}&paperId={PID}'),
    ('GET', f'https://gw-c.nowcoder.com/api/sparta/test/test-history?testId={TID}'),
    ('POST', f'https://gw-c.nowcoder.com/api/sparta/test/submission', {'testId': TID, 'paperId': PID}),
    ('POST', f'https://gw-c.nowcoder.com/api/sparta/test/submission-list', {'testId': TID, 'paperId': PID}),
    # testHistory 相关
    ('GET', f'https://gw-c.nowcoder.com/api/sparta/test/history-list?tagId=570&pageNo=1&pageSize=20'),
    ('GET', f'https://gw-c.nowcoder.com/api/sparta/test/test-history-list?tagId=570&pageNo=1&pageSize=20'),
    ('POST', f'https://gw-c.nowcoder.com/api/sparta/test/history-list', {'tagId': 570, 'pageNo': 1, 'pageSize': 20}),
    # common-practice 历史记录
    ('GET', f'https://gw-c.nowcoder.com/api/sparta/common-practice/history?tagId=570&pageNo=1&pageSize=20'),
    ('GET', f'https://gw-c.nowcoder.com/api/sparta/common-practice/test-history?tagId=570&pageNo=1&pageSize=20'),
    ('POST', f'https://gw-c.nowcoder.com/api/sparta/common-practice/history', {'tagId': 570, 'pageNo': 1, 'pageSize': 20}),
    # questiontraining 历史
    ('GET', f'https://www.nowcoder.com/api/questiontraining/intelligent/practiceHistory?subTabName=intelligent_page&questionJobId=10'),
    # test record
    ('GET', f'https://gw-c.nowcoder.com/api/sparta/test/record?testId={TID}'),
    ('GET', f'https://gw-c.nowcoder.com/api/sparta/test/records?testId={TID}'),
    # wrong questions
    ('GET', f'https://gw-c.nowcoder.com/api/sparta/test/wrong?testId={TID}&paperId={PID}'),
    ('GET', f'https://gw-c.nowcoder.com/api/sparta/test/wrong-questions?testId={TID}'),
    # report（之前发现能返回 doneQuestionDetails）
    ('POST', f'https://gw-c.nowcoder.com/api/sparta/test/report', {'testId': TID, 'paperId': PID}),
]
for item in candidates:
    method = item[0]
    url = item[1]
    post_body = item[2] if len(item) > 2 else None
    try:
        if method == 'GET':
            r = requests.get(url, headers=HEADERS, impersonate='chrome124', timeout=10)
        else:
            r = requests.post(url, json=post_body, headers=HEADERS, impersonate='chrome124', timeout=10)
        ct = r.headers.get('content-type', '')
        is_json = 'json' in ct
        has_data = is_json and ('"code":0' in r.text or '"success":true' in r.text or '"msg":"OK"' in r.text) and len(r.text) > 80
        short = url.split('sparta/')[-1][:60] if 'sparta/' in url else url.split('api/')[-1][:60]
        if r.status_code != 404:
            marker = ' ★★★' if has_data else (' ★JSON' if is_json else '')
            print(f'  {r.status_code} {method:4} {short}{marker}')
            if has_data:
                print(f'    => {r.text[:300]}'.replace('\n',' '))
    except Exception as e:
        print(f'  ERR {url[-40:]}: {str(e)[:40]}')
