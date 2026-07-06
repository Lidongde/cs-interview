import requests
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36',
    'Referer': 'https://www.nowcoder.com/exam/intelligent',
    'Origin': 'https://www.nowcoder.com',
}
# 探测可能的 API 端点
candidates = [
    'https://gw-c.nowcoder.com/api/sparta/exam/question-list-by-tag?tagId=273590',
    'https://gw-c.nowcoder.com/api/sparta/exam/questionList?tagId=273590',
    'https://gw-c.nowcoder.com/api/sparta/exam/intelligent?tagId=273590',
    'https://gw-c.nowcoder.com/api/sparta/exam/collection?tagId=273590',
    'https://gw-c.nowcoder.com/api/sparta/question/list?tagId=273590',
    'https://gw-c.nowcoder.com/api/sparta/exam/paper?tagId=273590',
    'https://gw-c.nowcoder.com/api/sparta/exam/test?tagId=273590',
    'https://gw-c.nowcoder.com/api/sparta/exam/questions?tagId=273590',
]
for url in candidates:
    try:
        r = requests.get(url, headers=headers, timeout=10)
        print(r.status_code, url, str(r.text)[:150])
    except Exception as e:
        print('ERR', url, str(e)[:80])
