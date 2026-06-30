"""
更新课表文档：M10 算法资源库 + 每日课表算法题目 → 本地 MD 直链
"""
import json, re

DOC = 'docs/career-plan/2026-07-java-backend-interview-prep.md'
DATA_DIR = 'leetcode_data'

# 相对路径：docs/career-plan/xxx.md → leetcode_data/output/yyy.md
# 从 docs/career-plan/ 到 leetcode_data/output/ 需要 ../../leetcode_data/output/
MD_PREFIX = '../../leetcode_data/output/'

# ========== 1. 加载题单数据 ==========
by_slug = {}
for fname, short in [('top-100-liked.json', '热题100'), ('top-interview-150.json', '面试150'), ('8LSpuXqD.json', '剑指Offer')]:
    with open(f'{DATA_DIR}/{fname}', encoding='utf-8') as f:
        data = json.load(f)
    for item in data:
        slug = item['titleSlug']
        qid = item['frontendQuestionId']
        title = item.get('titleCn', '')
        if slug not in by_slug:
            by_slug[slug] = {'id': qid, 'title': title, 'lists': []}
        by_slug[slug]['lists'].append({'name': short, 'file': fname.replace('.json', '.md')})

PRIORITY = {'热题100': 0, '面试150': 1, '剑指Offer': 2}

def link_text(slug):
    """返回: [1. 两数之和](../../leetcode_data/output/top-100-liked.md#two-sum)〔热题100 + 面试150〕"""
    info = by_slug[slug]
    sorted_lists = sorted(info['lists'], key=lambda x: PRIORITY.get(x['name'], 9))
    primary = sorted_lists[0]
    url = f'{MD_PREFIX}{primary["file"]}#{slug}'
    text = f'[{info["id"]}. {info["title"]}]({url})'
    if len(sorted_lists) > 1:
        text += '〔' + ' + '.join(li['name'] for li in sorted_lists) + '〕'
    return text

# ========== 2. 题目名 → slug 映射 ==========
P = {
    # 数组
    '两数之和 I+II': ['two-sum', 'two-sum-ii-input-array-is-sorted'],
    '两数之和 I、II': ['two-sum', 'two-sum-ii-input-array-is-sorted'],
    '两数之和 I': ['two-sum'],
    '两数之和 II': ['two-sum-ii-input-array-is-sorted'],
    '两数之和': ['two-sum'],
    '三数之和': ['3sum'],
    '合并有序数组': ['merge-sorted-array'],
    '除自身以外数组乘积': ['product-of-array-except-self'],
    # 链表
    '反转链表 I+II': ['reverse-linked-list', 'reverse-linked-list-ii'],
    '反转链表 I、II': ['reverse-linked-list', 'reverse-linked-list-ii'],
    '反转链表': ['reverse-linked-list'],
    '反转链表 II': ['reverse-linked-list-ii'],
    '环形链表': ['linked-list-cycle'],
    '合并2个有序链表': ['merge-two-sorted-lists'],
    '合并 2 个有序链表': ['merge-two-sorted-lists'],
    '删除倒数第N个': ['remove-nth-node-from-end-of-list'],
    '删除链表的倒数第 N 个结点': ['remove-nth-node-from-end-of-list'],
    'K 个一组翻转链表': ['reverse-nodes-in-k-group'],
    'K个一组翻转': ['reverse-nodes-in-k-group'],
    '两数相加': ['add-two-numbers'],
    '随机链表的复制': ['copy-list-with-random-pointer'],
    '排序链表': ['sort-list'],
    'LRU 缓存': ['lru-cache'],
    '合并K个升序链表': ['merge-k-sorted-lists'],
    # 栈/队列
    '有效括号': ['valid-parentheses'],
    '最小栈': ['min-stack'],
    '单调栈': ['daily-temperatures'],
    '滑动窗口最大值': ['sliding-window-maximum'],
    # 二叉树
    '层序遍历': ['binary-tree-level-order-traversal'],
    '最大深度': ['maximum-depth-of-binary-tree'],
    '最近公共祖先': ['lowest-common-ancestor-of-a-binary-tree'],
    '二叉树的最近公共祖先': ['lowest-common-ancestor-of-a-binary-tree'],
    '路径和': ['path-sum'],
    '路径和 II': ['path-sum-ii'],
    '二叉树展开为链表': ['flatten-binary-tree-to-linked-list'],
    '对称二叉树': ['symmetric-tree'],
    '验证二叉搜索树': ['validate-binary-search-tree'],
    '二叉树右视图': ['binary-tree-right-side-view'],
    '二叉树的右视图': ['binary-tree-right-side-view'],
    '翻转二叉树': ['invert-binary-tree'],
    '将有序数组转换为二叉搜索树': ['convert-sorted-array-to-binary-search-tree'],
    '二叉搜索树中第 K 小的元素': ['kth-smallest-element-in-a-bst'],
    '从前序与中序遍历序列构造二叉树': ['construct-binary-tree-from-preorder-and-inorder-traversal'],
    '二叉树中的最大路径和': ['binary-tree-maximum-path-sum'],
    # DFS/BFS
    '岛屿数量': ['number-of-islands'],
    '被围绕的区域': ['surrounded-regions'],
    '课程表': ['course-schedule'],
    '图的克隆': ['clone-graph'],
    # 回溯
    '全排列': ['permutations'],
    '组合': ['combinations'],
    '子集': ['subsets'],
    '组合总和': ['combination-sum'],
    '分割回文串': ['palindrome-partitioning'],
    '电话号码的字母组合': ['letter-combinations-of-a-phone-number'],
    '括号生成': ['generate-parentheses'],
    '单词搜索': ['word-search'],
    # 二分
    '搜索旋转排序数组': ['search-in-rotated-sorted-array'],
    '寻找峰值': ['find-peak-element'],
    '在排序数组中找元素首尾': ['find-first-and-last-position-of-element-in-sorted-array'],
    'x的平方根': ['sqrtx'],
    '寻找重复数': ['find-the-duplicate-number'],
    '搜索插入位置': ['search-insert-position'],
    '搜索二维矩阵': ['search-a-2d-matrix'],
    '寻找旋转排序数组中的最小值': ['find-minimum-in-rotated-sorted-array'],
    '寻找两个正序数组的中位数': ['median-of-two-sorted-arrays'],
    # DP
    '斐波那契': ['fei-bo-na-qi-shu-lie-lcof'],
    '爬楼梯': ['climbing-stairs'],
    '打家劫舍': ['house-robber'],
    '最大子数组和': ['maximum-subarray'],
    '不同路径': ['unique-paths'],
    '零钱兑换': ['coin-change'],
    '单词拆分': ['word-break'],
    '最长递增子序列': ['longest-increasing-subsequence'],
    '最长公共子序列': ['longest-common-subsequence'],
    '编辑距离': ['edit-distance'],
    '最长有效括号': ['longest-valid-parentheses'],
    '正则匹配': ['regular-expression-matching'],
    '最小路径和': ['minimum-path-sum'],
    '买卖股票的最佳时机': ['best-time-to-buy-and-sell-stock'],
    '跳跃游戏': ['jump-game'],
    '跳跃游戏 II': ['jump-game-ii'],
    # 滑动窗口/双指针
    '无重复字符最长子串': ['longest-substring-without-repeating-characters'],
    '无重复字符的最长子串': ['longest-substring-without-repeating-characters'],
    '最小覆盖子串': ['minimum-window-substring'],
    '和为s的连续正数序列': ['he-wei-sde-lian-xu-zheng-shu-xu-lie-lcof'],
    '移动零': ['move-zeroes'],
    '盛最多水的容器': ['container-with-most-water'],
    '接雨水': ['trapping-rain-water'],
    # 字符串
    '最长回文子串': ['longest-palindromic-substring'],
    '最长公共前缀': ['longest-common-prefix'],
    # 堆
    '数组中的第K个最大元素': ['kth-largest-element-in-an-array'],
    '前K高频元素': ['top-k-frequent-elements'],
    '数据流中位数': ['find-median-from-data-stream'],
    # 通用
    '合并区间': ['merge-intervals'],
    '轮转数组': ['rotate-array'],
    '矩阵置零': ['set-matrix-zeroes'],
    '螺旋矩阵': ['spiral-matrix'],
    '旋转图像': ['rotate-image'],
    '字母异位词分组': ['group-anagrams'],
    '最长连续序列': ['longest-consecutive-sequence'],
    '只出现一次的数字': ['single-number'],
    '多数元素': ['majority-element'],
    '实现 Trie (前缀树)': ['implement-trie-prefix-tree'],
    # 手写（无链接）
    '手写快排': [],
    '归并排序': [],
    '堆排序': [],
    '0-1背包': [],
    '完全背包': [],
    '省份数量': [],
    '用队列实现栈': [],
    '并查集模板': [],
    '前中后序递归+迭代': [],
    '前/中/后序递归+迭代': [],
}

# 过滤不在数据中的 slug
for name in list(P.keys()):
    P[name] = [s for s in P[name] if s in by_slug]

SORTED_NAMES = sorted(P.keys(), key=lambda x: -len(x))

def replace_problem(text):
    """精准替换单个题目名"""
    t = text.strip()
    for name in SORTED_NAMES:
        if t == name:
            slugs = P[name]
            if not slugs:
                return f'`{name}`（手写算法）'
            if len(slugs) == 1:
                return link_text(slugs[0])
            return ' + '.join(link_text(s) for s in slugs)
    return text

def process_list_cell(cell):
    """按 / 或 、 分割后逐项替换"""
    pieces = re.split(r'\s*/\s*|、', cell)
    return ' / '.join(replace_problem(p) for p in pieces if p.strip())

# ========== 3. 读取文件 ==========
with open(DOC, 'r', encoding='utf-8') as f:
    content = f.read()

lines = content.split('\n')
new_lines = []
modified = 0

for line in lines:
    is_algo_row = '🕐' in line and ('算法' in line or 'M10' in line) and line.strip().startswith('|')
    
    if is_algo_row:
        parts = line.split('|')
        if len(parts) >= 5:
            old = parts[4]
            parts[4] = ' ' + process_list_cell(parts[4]) + ' '
            line = '|'.join(parts)
            if old != parts[4]:
                modified += 1
    new_lines.append(line)

new_content = '\n'.join(new_lines)

# ========== 4. M10 资源库更新 ==========
# 原始文本替换为本地 MD 链接
new_content = new_content.replace(
    '| M10-D2 | LeetCode Hot 100 | 题库 | [leetcode.cn/problem-list/hot-100](https://leetcode.cn/problem-list/hot-100/) | ⭐⭐⭐ |',
    f'| M10-D2 | 热题 100（本地文档） | 题库 | [top-100-liked.md]({MD_PREFIX}top-100-liked.md) | ⭐⭐⭐ |'
)
new_content = new_content.replace(
    '| M10-D3 | 剑指 Offer 专项 | 题库 | [leetcode.cn/problem-list/剑指](https://leetcode.cn/problem-list/剑指/) | ⭐⭐⭐ |',
    f'| M10-D3 | 剑指Offer 专项突破（本地文档） | 题库 | [jianzhi-offer.md]({MD_PREFIX}jianzhi-offer.md) | ⭐⭐⭐ |'
)
new_content = new_content.replace(
    '| M10-D4 | 大厂面试高频算法 TOP 50 | 文档 | [LeetCode 热题100](https://leetcode.cn/problem-list/hot-100/) + [剑指Offer专项](https://leetcode.cn/problem-list/剑指/) | ⭐⭐⭐ |',
    f'| M10-D4 | 面试经典 150（本地文档） | 题库 | [top-interview-150.md]({MD_PREFIX}top-interview-150.md) + [剑指Offer]({MD_PREFIX}jianzhi-offer.md) | ⭐⭐⭐ |'
)

# ========== 5. 非表格里的 Hot 100 / 剑指 引用 ==========
extras = {
    '把 Hot 100 前30题再刷一遍': f'把 [热题100 前30题]({MD_PREFIX}top-100-liked.md) 再刷一遍',
    'Hot 100 31-50题': f'[热题100 31-50题]({MD_PREFIX}top-100-liked.md)',
    'Hot 100 前20题': f'[热题100 前20题]({MD_PREFIX}top-100-liked.md)',
    'Hot 100 21-40题': f'[热题100 21-40题]({MD_PREFIX}top-100-liked.md)',
    'Hot 100 41-60题': f'[热题100 41-60题]({MD_PREFIX}top-100-liked.md)',
    'Hot 100 61-80题': f'[热题100 61-80题]({MD_PREFIX}top-100-liked.md)',
    'Hot 100 81-100题': f'[热题100 81-100题]({MD_PREFIX}top-100-liked.md)',
    'Hot 100 第一轮': f'[热题100 第一轮]({MD_PREFIX}top-100-liked.md)',
    'Hot 100 第二轮': f'[热题100 第二轮]({MD_PREFIX}top-100-liked.md)',
    'Hot 100 第三遍': f'[热题100 第三遍]({MD_PREFIX}top-100-liked.md)',
    'Hot 100 限时 4题': f'[热题100 限时 4题]({MD_PREFIX}top-100-liked.md)',
    '剑指 Offer 精选 10 题': f'[剑指Offer 精选 10 题]({MD_PREFIX}jianzhi-offer.md)',
}
for old, new in extras.items():
    if old in new_content:
        new_content = new_content.replace(old, new)

# ========== 6. 写入 ==========
with open(DOC, 'w', encoding='utf-8') as f:
    f.write(new_content)

# ========== 7. 验证 ==========
urls = re.findall(r'\]\(\.\./\.\./leetcode_data/output/[^)]+\)', new_content)
print(f'✅ 文档已更新')
print(f'  修改的表格行: {modified}')
print(f'  总直链数: {len(urls)}')

# 验证无空格问题
bad = [u for u in urls if ' ' in u]
if bad:
    print(f'⚠️ 警告: {len(bad)} 个 URL 包含空格')
else:
    print('✅ 所有 URL 格式正确')