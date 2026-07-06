"""
用真实 cookie + 真实 API 端点测试获取题目
关键 cookie: acw_tc (WAF 通行证, HttpOnly)
"""
import json
from curl_cffi import requests

# 完整 cookie（含 acw_tc）
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

# 1. 创建试卷（生成练习）
print('=== 1. 创建试卷 (request-make-paper-pc) ===')
body = {"tagIdSets":["570"],"classifyName":"    ","pageType":"intelligent_page","questionJobId":10}
r = requests.post(
    'https://gw-c.nowcoder.com/api/sparta/common-practice/request-make-paper-pc',
    json=body, headers=HEADERS, impersonate='chrome124', timeout=20)
print(f'status: {r.status_code}')
print(f'body: {r.text[:500]}')

if r.status_code == 200:
    data = r.json()
    print(f'\n完整响应结构:')
    print(json.dumps(data, ensure_ascii=False, indent=2)[:1500])
