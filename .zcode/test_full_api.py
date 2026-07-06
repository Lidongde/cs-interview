"""
用完整 cookie（含 acw_tc）测试需要登录的 API
并直接调用 request-make-paper-pc 创建新试卷，然后找题目 API
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

# 1. 测试登录态 API
print('=== 1. practiceHistory（之前返回未登录）===')
r = requests.get('https://www.nowcoder.com/api/questiontraining/intelligent/practiceHistory?subTabName=intelligent_page&questionJobId=10',
                 headers=HEADERS, impersonate='chrome124', timeout=15)
print(f'  {r.status_code}: {r.text[:200]}')

# 2. 创建新试卷
print('\n=== 2. 创建试卷 ===')
body = {"tagIdSets":["570"],"classifyName":"    ","pageType":"intelligent_page","questionJobId":10}
r = requests.post('https://gw-c.nowcoder.com/api/sparta/common-practice/request-make-paper-pc',
                  json=body, headers=HEADERS, impersonate='chrome124', timeout=20)
print(f'  {r.status_code}: {r.text[:200]}')
paper_data = r.json().get('data', {}) if r.status_code == 200 else {}
paper_id = paper_data.get('paperId')
test_id = paper_data.get('testId')
question_uuid = paper_data.get('questionUUID')
print(f'  paperId={paper_id}, testId={test_id}, uuid={question_uuid}')

# 3. 用 questionUUID 探测题目内容 API
print('\n=== 3. 探测题目内容 API ===')
hit_urls = [
    f'https://www.nowcoder.com/api/questiontraining/intelligent/paper?paperId={paper_id}&testId={test_id}',
    f'https://www.nowcoder.com/api/questiontraining/paper/questions?paperId={paper_id}',
]
for url in hit_urls:
    try:
        r = requests.get(url, headers=HEADERS, impersonate='chrome124', timeout=15)
        print(f'\n  GET {url.split("api/")[-1][:70]}')
        print(f'  status={r.status_code}')
        print(f'  body: {r.text[:800]}'.replace('\n', ' '))
    except Exception as e:
        print(f'  ERR: {str(e)[:80]}')
