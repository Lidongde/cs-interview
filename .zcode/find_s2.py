import re
from curl_cffi import requests
r = requests.get('https://static.nowcoder.com/fe/file/site/www-web/prod/1.0.484/page/examTest/main.entry.js', impersonate='chrome124', timeout=20)
content = r.text

# 找 Q.s2 的定义。Q=n(xxx)，s2 是模块导出
# 先找 Q.s2 被调用的地方
idx = content.find('Q.s2)({body:{questionId')
if idx < 0:
    idx = content.find('answerContent:r}')
print(f'调用位置: {idx}')
if idx >= 0:
    # Q 是之前定义的变量，找 Q=n(数字)
    # 向前找 Q= 或 Q,
    chunk_before = content[max(0,idx-5000):idx]
    # 找最后一个 Q=n( 或 Q=
    q_defs = list(re.finditer(r'[,;]Q=n\((\d+)\)', chunk_before))
    if q_defs:
        module_id = q_defs[-1].group(1)
        print(f'Q = n({module_id})')
        # 找这个模块的定义 n(模块id) 的 exports
        # 搜索 s2 在模块中的定义
        # 模块定义格式: 数字:function(modules, exports, require)
        # 或者 s2:function 或 s2=
        # 搜索 .s2= 或 s2: 的定义
        for m in re.finditer(r's2\s*[:=]\s*(?:function)?\s*\(', content):
            chunk = content[max(0,m.start()-200):m.start()+300]
            if 'api' in chunk.lower() or 'post' in chunk.lower() or 'url' in chunk.lower() or 'request' in chunk.lower():
                print(f'\ns2 定义 @ {m.start()}:')
                print(chunk)

# 直接搜索 submit-answer / answer / question-answer 等
print('\n=== 搜索 answer 相关 API URL ===')
for m in re.finditer(r'["\'](/[a-zA-Z0-9/_-]*answer[a-zA-Z0-9/_-]*)["\']', content, re.IGNORECASE):
    print(f'  {m.group(1)}')
for m in re.finditer(r'["\'](/[a-zA-Z0-9/_-]*submit[a-zA-Z0-9/_-]*)["\']', content, re.IGNORECASE):
    print(f'  {m.group(1)}')

# 搜索 answerContent 附近的 URL（可能 API URL 在同一个函数里）
print('\n=== answerContent 附近更广上下文 ===')
idx = content.find('answerContent:r}')
if idx >= 0:
    print(content[max(0,idx-1000):idx+200])
