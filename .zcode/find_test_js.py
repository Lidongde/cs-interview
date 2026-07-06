"""
获取答题页 HTML，找所有 JS（包括动态 chunk）
特别找 test/main.entry.js 或类似的 chunk 加载器
"""
import re
from curl_cffi import requests

HEADERS = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/150.0.0.0 Safari/537.36',
}

# 答题页 HTML
r = requests.get('https://www.nowcoder.com/exam/test?testId=97743110',
                 headers=HEADERS, impersonate='chrome124', timeout=15)
html = r.text

# 找所有 JS 引用（包括 script src 和动态 import）
js_srcs = re.findall(r'src="([^"]+\.js[^"]*)"', html)
# 也找 JSONP / chunk 加载
chunk_patterns = re.findall(r'["\']([^"\']*(?:test|exam|question|paper)[^"\']*\.js[^"\']*)["\']', html, re.IGNORECASE)
# 找 webpack manifest 或 chunk mapping
manifest_matches = re.findall(r'(?:chunk|manifest|map)["\']?\s*[:=]\s*({[^}]+})', html)

print('=== script src ===')
for s in js_srcs:
    print(f'  {s}')

print('\n=== chunk/test/exam 相关 JS ===')
for c in set(chunk_patterns):
    print(f'  {c}')

# 找 HTML 里的内联 JS，可能有 webpack jsonp 或 chunk 列表
inline_scripts = re.findall(r'<script[^>]*>(.*?)</script>', html, re.DOTALL)
for i, s in enumerate(inline_scripts):
    if len(s) > 100 and ('chunk' in s.lower() or 'test' in s.lower() or 'entry' in s.lower()):
        print(f'\n=== 内联脚本 {i} ({len(s)} chars) ===')
        # 找 chunk 路径
        chunks = re.findall(r'["\']([a-zA-Z0-9/_-]*(?:test|exam|question)[a-zA-Z0-9/_-]*)["\']', s)
        if chunks:
            print(f'  chunks: {set(chunks)}')
        print(f'  preview: {s[:400]}')

# 下载 common.js 搜索 test/exam/question 相关的 API 定义
print('\n=== 搜索 common.js 中的 API 定义 ===')
r2 = requests.get('https://static.nowcoder.com/nowcoder/2.0.312/javascripts-wp/lib/common.js',
                  headers=HEADERS, impersonate='chrome124', timeout=20)
content = r2.text
# 搜索 request-make-paper 附近的代码，找到相关 API
idx = content.find('request-make-paper')
if idx >= 0:
    print(f'\n  request-make-paper 附近:')
    print(f'  {content[max(0,idx-200):idx+300]}')
else:
    print('  request-make-paper 未找到')

# 搜索 make-paper
for kw in ['make-paper', 'getPaper', 'getQuestion', 'questionList', 'paperQuestion', 'paperInfo', 'questionDetail', 'getTestPaper', 'queryQuestion']:
    idx = content.find(kw)
    if idx >= 0:
        print(f'\n  {kw} 附近:')
        print(f'  {content[max(0,idx-100):idx+200]}')
