"""
探测其他获取题目的方式：
1. makePaper（非智能组卷）
2. 错题本/收藏题目 API
3. 练习历史 API
4. 看看能否重置已做记录
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

# 1. makePaper（非智能组卷，手动指定标签）
print('=== 1. makePaper ===')
r = requests.post('https://www.nowcoder.com/api/questiontraining/intelligent/makePaper',
                  json={'tagId': 570, 'pageType': 'intelligent_page', 'questionJobId': 10},
                  headers=HEADERS, impersonate='chrome124', timeout=15)
print(f'  {r.status_code} {r.text[:300]}'.replace('\n',' '))

# 2. makeTestPaper
print('\n=== 2. makeTestPaper ===')
r = requests.post('https://gw-c.nowcoder.com/api/sparta/intelligent/makeTestPaper',
                  json={'tagId': 570, 'questionJobId': 10},
                  headers=HEADERS, impersonate='chrome124', timeout=15)
print(f'  {r.status_code} {r.text[:300]}'.replace('\n',' '))

# 3. queryTagDetailInfo（标签详情，可能含题目列表）
print('\n=== 3. queryTagDetailInfo ===')
r = requests.post('https://gw-c.nowcoder.com/api/sparta/intelligent/queryTagDetailInfo',
                  json={'tagId': 570, 'questionJobId': 10},
                  headers=HEADERS, impersonate='chrome124', timeout=15)
print(f'  {r.status_code} {r.text[:300]}'.replace('\n',' '))

# 4. getPCIntelligentList
print('\n=== 4. getPCIntelligentList ===')
r = requests.get('https://gw-c.nowcoder.com/api/sparta/intelligent/getPCIntelligentList?questionJobId=10',
                 headers=HEADERS, impersonate='chrome124', timeout=15)
print(f'  {r.status_code} {r.text[:300]}'.replace('\n',' '))

# 5. 练习历史（含已做题目）
print('\n=== 5. practiceHistory ===')
r = requests.get('https://www.nowcoder.com/api/questiontraining/intelligent/practiceHistory?subTabName=intelligent_page&questionJobId=10',
                 headers=HEADERS, impersonate='chrome124', timeout=15)
print(f'  {r.status_code} {r.text[:400]}'.replace('\n',' '))

# 6. try request-make-paper with different pageType
print('\n=== 6. request-make-paper-pc with pageType=practice_page ===')
r = requests.post('https://gw-c.nowcoder.com/api/sparta/common-practice/request-make-paper-pc',
                  json={"tagIdSets":["570"],"classifyName":"    ","pageType":"practice_page","questionJobId":10},
                  headers=HEADERS, impersonate='chrome124', timeout=15)
print(f'  {r.status_code} {r.text[:300]}'.replace('\n',' '))

# 7. 用 continue API（继续练习，可能重新出题）
print('\n=== 7. continue ===')
r = requests.get('https://www.nowcoder.com/api/questiontraining/intelligent/continue?subTabName=intelligent_page&questionJobId=10&tagId=570',
                 headers=HEADERS, impersonate='chrome124', timeout=15)
print(f'  {r.status_code} {r.text[:400]}'.replace('\n',' '))
