"""
1. 查看 getPCIntelligentList 完整响应
2. 用 queryTagDetailInfo (GET) 看能否获取题目列表
3. 测试用其他标签组合
"""
import json
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

# 1. getPCIntelligentList 完整响应
print('=== getPCIntelligentList ===')
r = requests.get('https://gw-c.nowcoder.com/api/sparta/intelligent/getPCIntelligentList?questionJobId=10',
                 headers=HEADERS, impersonate='chrome124', timeout=15)
data = r.json()['data']
for tag_group in data.get('tags', []):
    print(f'\n分组: {tag_group["title"]} (tagId={tag_group["tagId"]})')
    for item in tag_group.get('items', []):
        print(f'  {item["title"]:15} id={item["id"]:8} tcount={item["tcount"]:5} rcount={item["rcount"]:5} left={item["leftCount"]:5}')

# 2. queryTagDetailInfo GET
print('\n=== queryTagDetailInfo (GET) ===')
r = requests.get('https://gw-c.nowcoder.com/api/sparta/intelligent/queryTagDetailInfo?tagId=570&questionJobId=10',
                 headers=HEADERS, impersonate='chrome124', timeout=15)
print(f'  {r.status_code} {r.text[:500]}'.replace('\n',' '))

# 3. getTags
print('\n=== getTags ===')
r = requests.get('https://www.nowcoder.com/api/questiontraining/intelligent/getTags?questionJobId=10',
                 headers=HEADERS, impersonate='chrome124', timeout=15)
print(f'  {r.status_code} {r.text[:400]}'.replace('\n',' '))

# 4. 用"推荐"标签 tagId=273590 组卷
print('\n=== 用推荐标签组卷 ===')
r = requests.post('https://gw-c.nowcoder.com/api/sparta/common-practice/request-make-paper-pc',
                  json={"tagIdSets":["273590"],"classifyName":"    ","pageType":"intelligent_page","questionJobId":10},
                  headers=HEADERS, impersonate='chrome124', timeout=15)
print(f'  {r.status_code} {r.text[:300]}'.replace('\n',' '))

# 5. 用多标签组合（Java + 网络基础，分散已做题的影响）
print('\n=== Java + 网络基础 组合 ===')
r = requests.post('https://gw-c.nowcoder.com/api/sparta/common-practice/request-make-paper-pc',
                  json={"tagIdSets":["570","604"],"classifyName":"    ","pageType":"intelligent_page","questionJobId":10},
                  headers=HEADERS, impersonate='chrome124', timeout=15)
print(f'  {r.status_code} {r.text[:300]}'.replace('\n',' '))
