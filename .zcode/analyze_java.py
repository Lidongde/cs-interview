"""详细分析 Java 停在 399 的原因"""
with open(r'D:/Workspace/Project/cs-interview/nowcoder_data/crawl.log', 'r', encoding='utf-8') as f:
    lines = f.readlines()

# 找 Java 部分的起止
java_start = None
java_end = None
for i, line in enumerate(lines):
    if '爬取: Java' in line:
        java_start = i
    elif java_start and '爬取: Spring' in line:
        java_end = i
        break

if java_start and java_end:
    java_lines = lines[java_start:java_end]
    # 看最后 20 行
    print('=== Java 部分最后 25 行 ===')
    for l in java_lines[-25:]:
        print(l.rstrip())

    # 统计 "本轮 0 题"（API 返回 0 题）vs "新增 0 题"（返回了题但都是重复）
    api_zero = 0  # 本轮 0 题 = API 返回空
    dup_zero = 0  # 本轮 5 题，新增 0 题 = 返回了但都是重复
    for l in java_lines:
        if '本轮 0 题' in l:
            api_zero += 1
        elif '新增 0 题' in l and '本轮 0 题' not in l:
            dup_zero += 1
    print(f'\nAPI 返回 0 题（题目数量为0）的轮数: {api_zero}')
    print(f'返回了题但全重复的轮数: {dup_zero}')
