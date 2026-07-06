"""
探测牛客专项练习的题目 API 结构
"""
import re
import json
from curl_cffi import requests

HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36',
    'Accept': 'application/json, text/plain, */*',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
    'Referer': 'https://www.nowcoder.com/exam/intelligent',
    'Origin': 'https://www.nowcoder.com',
    'Content-Type': 'application/json',
}

# 候选 API 端点（基于牛客 sparta API 模式）
CANDIDATES = [
    # 标签相关
    ('GET', 'https://gw-c.nowcoder.com/api/sparta/exam/exam-paper/get-by-tag?tagId=570'),
    ('GET', 'https://gw-c.nowcoder.com/api/sparta/exam/exam-paper/list?tagId=570'),
    ('GET', 'https://gw-c.nowcoder.com/api/sparta/exam/question/by-tag?tagId=570&pageNo=1&pageSize=20'),
    ('GET', 'https://gw-c.nowcoder.com/api/sparta/exam/question-list?tagId=570'),
    ('GET', 'https://gw-c.nowcoder.com/api/sparta/exam/questions?tagId=570'),
    ('GET', 'https://gw-c.nowcoder.com/api/sparta/exam/paper?tagId=570'),
    ('GET', 'https://gw-c.nowcoder.com/api/sparta/exam/test?tagId=570'),
    ('GET', 'https://gw-c.nowcoder.com/api/sparta/exam/intelligent?tagId=570'),
    # 试卷创建
    ('POST', 'https://gw-c.nowcoder.com/api/sparta/exam/exam-paper/create', {'tagId': 570, 'questionJobId': 10}),
    ('POST', 'https://gw-c.nowcoder.com/api/sparta/exam/paper/create', {'tagId': 570}),
    ('POST', 'https://gw-c.nowcoder.com/api/sparta/exam/start-practice', {'tagId': 570}),
    # 题目内容
    ('GET', 'https://gw-c.nowcoder.com/api/sparta/question-bank/question/list?tagId=570'),
    ('GET', 'https://gw-c.nowcoder.com/api/sparta/question-bank/exam/list?tagId=570'),
]

for item in CANDIDATES:
    method = item[0]
    url = item[1]
    body = item[2] if len(item) > 2 else None
    try:
        if method == 'GET':
            r = requests.get(url, headers=HEADERS, impersonate='chrome124', timeout=15)
        else:
            r = requests.post(url, json=body, headers=HEADERS, impersonate='chrome124', timeout=15)
        ct = r.headers.get('content-type', '')
        is_waf = 'aliyun_waf' in r.text[:500]
        is_json = 'json' in ct
        preview = r.text[:200].replace('\n', ' ')
        print(f'{r.status_code} {method} {("WAF" if is_waf else ("JSON" if is_json else "HTML"))} {url.split("api/sparta/")[-1][:50]}')
        if is_json and not is_waf:
            print(f'    BODY: {preview}')
    except Exception as e:
        print(f'ERR {method} {url[-40:]}: {str(e)[:80]}')
