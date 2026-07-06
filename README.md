# CS Interview — 面试刷题资料库

Java 后端面试备战资料，包含 LeetCode 算法题、牛客网专项练习题、8 周突击课表与知识点笔记。

## 目录结构

```
cs-interview/
├── leetcode_crawler.py          # LeetCode 爬虫
├── nowcoder_crawler.py          # 牛客网爬虫
├── leetcode_data/               # LeetCode 数据
│   ├── output/                  # 生成的 Markdown 题集
│   │   ├── top-100-liked.md     # 热题 100
│   │   ├── top-interview-150.md # 面试经典 150
│   │   └── jianzhi-offer.md     # 剑指 Offer 专项
│   └── details/                 # 题目详情 JSON
├── nowcoder_data/               # 牛客网数据
│   ├── output/                  # 生成的交互式 Markdown
│   │   ├── Java.md
│   │   ├── Spring.md
│   │   └── Redis.md
│   └── *.json                   # 题目原始 JSON
└── docs/
    ├── career-plan/             # 8 周突击课表
    └── notes/                   # 知识点笔记（M1-M9）
```

---

## LeetCode 爬虫（leetcode_crawler.py）

爬取 LeetCode 题单（热题 100 / 面试经典 150 / 剑指 Offer）并转换为 Markdown。

### 依赖

```bash
pip install curl_cffi
```

### 用法

```bash
# 只爬题单列表（不爬详情、不转 MD）
python leetcode_crawler.py

# 爬取列表 + 全部题目详情（题面、代码模板）
python leetcode_crawler.py --detail

# 爬取列表 + 转 MD（不爬详情，用已有详情）
python leetcode_crawler.py --md

# 全流程：爬取列表 + 详情 + 转 MD
python leetcode_crawler.py --detail --md

# 只用已有 JSON 转 MD（跳过爬取）
python leetcode_crawler.py --only-md
```

### 参数说明

| 参数 | 说明 |
|------|------|
| `--detail` | 爬取每道题的详情（题面 HTML、代码模板、提示） |
| `--md` | 将 JSON 转换为 Markdown 文档 |
| `--only-md` | 跳过爬取，直接用已有 JSON 生成 MD |

### 数据来源

- REST `/api/problems/all/` — 全部题目元数据
- GraphQL `studyPlanV2Detail` — 热题 100、面试经典 150
- GraphQL `favoriteQuestionList` — 剑指 Offer 专项
- GraphQL `questionDetail` — 单题详情

无需登录，通过 `curl_cffi` 的 `impersonate` 模拟浏览器 TLS 指纹绕过 Cloudflare。

### 输出

- `leetcode_data/output/top-100-liked.md` — 热题 100（带难度徽章、代码模板）
- `leetcode_data/output/top-interview-150.md` — 面试经典 150
- `leetcode_data/output/jianzhi-offer.md` — 剑指 Offer 专项突破

---

## 牛客网爬虫（nowcoder_crawler.py）

爬取牛客网专项练习题目（Java / Spring / Redis 等），含答案与官方解析，生成交互式 Markdown。

### 依赖

```bash
pip install curl_cffi
```

### Cookie 配置

牛客网需要登录态，关键 cookie 是 `acw_tc`（HttpOnly，需从 DevTools 复制）：

1. 登录 [nowcoder.com](https://www.nowcoder.com)
2. F12 → Network → 复制任意请求的 `Cookie` 头
3. 粘贴到脚本顶部的 `COOKIE` 变量，或设置环境变量：
   ```bash
   set NOWCODER_COOKIE=你的cookie
   ```

### 用法

```bash
# 自动模式爬 Java（默认全部题，自动判断策略，生成 MD）
python nowcoder_crawler.py

# 爬指定标签（Java 570 / Spring 3935 / Redis 21048 / Kafka 21049 ...）
python nowcoder_crawler.py --tags 570 3935 21048

# 限制每标签 50 题
python nowcoder_crawler.py --tags 570 --count 50

# 爬取后不生成 MD
python nowcoder_crawler.py --no-md

# 强制只用历史补全模式（不做智能组卷）
python nowcoder_crawler.py --supplement-only --tags 570

# 只用已有 JSON 重新生成 MD
python nowcoder_crawler.py --only-md
```

### 参数说明

| 参数 | 说明 |
|------|------|
| `--tags` | 标签 ID 列表（如 `570 3935 21048`），不指定默认 Java |
| `--all` | 爬取所有预设标签 |
| `--count` | 每标签爬取题数上限（默认 10000=全部，仅智能组卷阶段生效） |
| `--supplement-only` | 强制只用历史补全模式 |
| `--only-md` | 只用已有 JSON 转 MD（不爬取） |
| `--no-md` | 爬取后不生成 MD |

### 自动策略

默认（自动模式）会先查询刷题状态，智能选择爬取策略：

```
查询标签刷题状态 (getPCIntelligentList)
            │
    ┌───────┴───────┐
 已做=0            已做>0
    │                │
纯智能组卷      智能组卷 + 历史补全
(拿全部非会员题)  (组卷拿未做题 + 补全拿已做题)
```

- **未刷过的标签** → 纯智能组卷，直接拿到全部非会员题
- **已刷过的标签** → 智能组卷只能拿未做过的题，需要历史补全来补回已做过的题

### 常用标签 ID

| 标签 | ID | 标签 | ID |
|------|-----|------|-----|
| Java | 570 | Redis | 21048 |
| Spring | 3935 | Kafka | 21049 |
| 网络基础 | 604 | 数据库 | 606 |
| 操作系统 | 607 | Linux | 618 |
| 设计模式 | 3410 | SQL | 3427 |
| C++ | 569 | Python | 573 |

### 输出

- `nowcoder_data/{tagId}_{tagName}.json` — 题目原始数据
- `nowcoder_data/output/{tagName}.md` — 交互式 Markdown 文档

交互式功能：
- ✅ 勾选选项自测（`- [ ]` task list）
- ✅ 填写回答区域
- ✅ 点击展开答案与官方解析（`<details>` 折叠）
- ✅ 进度统计表（localStorage 持久化）

---

## 推荐 workflow

```bash
# 1. LeetCode 题集（一次性）
python leetcode_crawler.py --detail --md

# 2. 牛客网专项练习（Java + Spring + Redis）
python nowcoder_crawler.py --tags 570 3935 21048

# 3. 之后随时重新生成 MD
python leetcode_crawler.py --only-md
python nowcoder_crawler.py --only-md
```
