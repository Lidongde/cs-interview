"""
用 paperId/testId 获取题目内容
先导航到答题页，抓取题目内容 API
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

PAPER_ID = 67855290
TEST_ID = 97742075

# 候选：获取题目内容的 API
candidates = [
    ('GET', f'https://gw-c.nowcoder.com/api/sparta/common-practice/get-paper?paperId={PAPER_ID}&testId={TEST_ID}'),
    ('GET', f'https://gw-c.nowcoder.com/api/sparta/common-practice/paper?paperId={PAPER_ID}&testId={TEST_ID}'),
    ('GET', f'https://gw-c.nowcoder.com/api/sparta/common-practice/questions?paperId={PAPER_ID}&testId={TEST_ID}'),
    ('GET', f'https://gw-c.nowcoder.com/api/sparta/common-practice/question-list?paperId={PAPER_ID}'),
    ('GET', f'https://gw-c.nowcoder.com/api/sparta/common-practice/get-questions?paperId={PAPER_ID}&testId={TEST_ID}'),
    ('GET', f'https://gw-c.nowcoder.com/api/sparta/exam/paper?paperId={PAPER_ID}&testId={TEST_ID}'),
    ('GET', f'https://gw-c.nowcoder.com/api/sparta/exam/questions?paperId={PAPER_ID}&testId={TEST_ID}'),
    ('GET', f'https://gw-c.nowcoder.com/api/sparta/exam/get-paper?paperId={PAPER_ID}'),
    # 可能是 questiontraining 路径
    ('GET', f'https://www.nowcoder.com/api/questiontraining/intelligent/paper?paperId={PAPER_ID}&testId={TEST_ID}'),
    ('GET', f'https://www.nowcoder.com/api/questiontraining/paper?paperId={PAPER_ID}'),
    ('GET', f'https://www.nowcoder.com/api/questiontraining/questions?paperId={PAPER_ID}'),
    # testId 为主
    ('GET', f'https://gw-c.nowcoder.com/api/sparta/common-practice/test?testId={TEST_ID}'),
    ('GET', f'https://gw-c.nowcoder.com/api/sparta/common-practice/get-test?testId={TEST_ID}'),
    ('GET', f'https://gw-c.nowcoder.com/api/sparta/common-practice/paper-info?testId={TEST_ID}'),
    ('GET', f'https://gw-c.nowcoder.com/api/sparta/common-practice/paper-detail?testId={TEST_ID}'),
    # POST 方式
    ('POST', f'https://gw-c.nowcoder.com/api/sparta/common-practice/get-paper', {'paperId': PAPER_ID, 'testId': TEST_ID}),
    ('POST', f'https://gw-c.nowcoder.com/api/sparta/common-practice/paper-detail', {'testId': TEST_ID}),
]

print('=== 探测题目内容 API ===')
for item in candidates:
    method = item[0]
    url = item[1]
    body = item[2] if len(item) > 2 else None
    try:
        if method == 'GET':
            r = requests.get(url, headers=HEADERS, impersonate='chrome124', timeout=15)
        else:
            r = requests.post(url, json=body, headers=HEADERS, impersonate='chrome124', timeout=15)
        ct = r.headers.get('content-type', '')
        is_waf = 'aliyun_waf' in r.text[:300]
        tag = 'WAF' if is_waf else ('JSON' if 'json' in ct else 'HTML')
        short = url.split('api/')[-1][:60] if 'api/' in url else url[-60:]
        status = r.status_code
        preview = r.text[:150].replace('\n', ' ') if 'json' in ct and not is_waf else ''
        # 判断是否有真实数据（code:0 或有 question 字段）
        has_data = '"code":0' in r.text or 'question' in r.text.lower()[:200]
        marker = ' ★有数据' if has_data and not is_waf else ''
        print(f'  {status} {method} {tag:4} {short}{marker}')
        if has_data and not is_waf:
            print(f'      => {preview}')
    except Exception as e:
        print(f'  ERR {url[-50:]}: {str(e)[:50]}')
