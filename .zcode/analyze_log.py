"""分析爬取日志，找出 Java 为什么停在 399 题"""
import re

with open(r'D:/Workspace/Project/cs-interview/nowcoder_data/crawl.log', 'r', encoding='utf-8') as f:
    lines = f.readlines()

# 找 Java 部分
java_start = None
for i, line in enumerate(lines):
    if '爬取: Java' in line:
        java_start = i
        break

if java_start:
    print(f'Java 部分从第 {java_start} 行开始')
    # 统计新增 0 题的轮次
    zero_new = 0
    total_rounds = 0
    last_few = []
    for line in lines[java_start:]:
        if '试卷 #' in line:
            total_rounds += 1
            if '新增 0 题' in line:
                zero_new += 1
            last_few.append(line.strip())
        if '停止' in line:
            print(f'停止: {line.strip()}')
        if '✅ Java' in line:
            print(f'结果: {line.strip()}')

    print(f'\nJava 总轮数: {total_rounds}, 新增0题的轮数: {zero_new}')
    print(f'\n最后 10 轮:')
    for l in last_few[-10:]:
        print(f'  {l}')
