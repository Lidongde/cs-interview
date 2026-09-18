# CS Interview — 面试刷题资料库

Java 后端面试备战资料，包含 LeetCode 算法题、牛客网专项练习题、8 周突击课表与知识点笔记。

## 目录结构

```
cs-interview/
├── leetcode_crawler.py          # LeetCode 爬虫
├── nowcoder_crawler.py          # 牛客网专项练习爬虫
├── nowcoder_company_crawler.py  # 牛客网公司真题爬虫
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
│   ├── company_papers/          # 公司真题数据（职业标签 + 试卷清单）
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

# 列出全部有效标签 ID（供 --tags 使用）
python nowcoder_crawler.py --list-tags

# 爬指定标签（Java 570 / Spring 3935 / Redis 21048 ...）
python nowcoder_crawler.py --tags 570 3935 21048

# 限制每标签 50 题
python nowcoder_crawler.py --tags 570 --count 50

# 直接爬指定试卷 URL（testId + pid，只读，不新建试卷）
python nowcoder_crawler.py --url "https://www.nowcoder.com/exam/test/99849624/detail?pid=69356018"

# 内网直连超时时指定代理
python nowcoder_crawler.py --tags 570 --proxy http://proxyhk.zte.com.cn:80

# 爬取后不生成 MD
python nowcoder_crawler.py --no-md

# 强制只用历史补全模式（不做智能组卷）
python nowcoder_crawler.py --supplement-only --tags 570

# 只用已有 JSON 全量重新生成 MD（含 README 索引）
python nowcoder_crawler.py --only-md
```

### 参数说明

| 参数 | 说明 |
|------|------|
| `--tags` | 标签 ID 列表（如 `570 3935 21048`），不指定默认 Java |
| `--all` | 爬取所有预设标签 |
| `--count` | 每标签爬取题数上限（默认 10000=全部，仅智能组卷阶段生效） |
| `--url` | 直接爬取指定试卷 URL（解析 testId/pid/testclass，只读） |
| `--name` | `--url` 模式下自定义标签名（默认取 URL 的 testclass 参数） |
| `--proxy` | 指定 HTTP 代理，如 `http://127.0.0.1:7890` |
| `--list-tags` | 实时列出智能组卷全部标签 ID（供 `--tags` 使用） |
| `--supplement-only` | 强制只用历史补全模式 |
| `--only-md` | 只用已有 JSON 全量转 MD（不爬取） |
| `--no-md` | 爬取后不生成 MD |

> **连接超时排查**：公司/内网环境直连牛客常被网络层阻断（报 `curl: Connection timed out`），需要走代理。设置环境变量 `http_proxy`/`https_proxy`，或直接加 `--proxy http://代理地址:端口`。

> **MD 生成范围**：爬取后默认只生成本次爬到的标签，**不会重写其他标签的 MD 文件**；`--only-md` 才会全量重写（含 README 索引）。

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
| Java | 570 | Spring | 3935 |
| Redis | 21048 | Kafka | 21049 |
| 网络基础 | 604 | 数据库 | 606 |
| 操作系统 | 607 | Linux | 618 |
| 设计模式 | 3410 | SQL | 3427 |
| C++ | 569 | Python | 573 |
| Go | 809 | 提示词工程 | 305566 |
| Agent | 305563 | 大模型概念 | 292035 |
| RAG | 305564 | 微调 | 305562 |

> 完整标签列表（含题数/进度）实时获取：`python nowcoder_crawler.py --list-tags`

### 输出

- `nowcoder_data/{tagId}_{tagName}.json` — 题目原始数据
- `nowcoder_data/output/{tagName}.md` — 交互式 Markdown 文档

交互式功能：
- ✅ 勾选选项自测（`- [ ]` task list）
- ✅ 填写回答区域
- ✅ 点击展开答案与官方解析（`<details>` 折叠）
- ✅ 进度统计表（localStorage 持久化）

---

## 牛客网公司真题爬虫（nowcoder_company_crawler.py）

爬取公司真题页（`exam/company?subTabName=written_page`）的试卷标签，以及指定职业分类下的全部试卷清单。

### 依赖与 Cookie

依赖 `curl_cffi`；Cookie 配置与专项练习爬虫相同（见上文"Cookie 配置"）。

### 用法

```bash
# 抓所有职业的标签 + 软件开发（careerJobId=11226）下全部试卷
python nowcoder_company_crawler.py

# 指定职业（如通信/硬件 11227）
python nowcoder_company_crawler.py --career 11227

# 只抓试卷列表，不抓各职业标签
python nowcoder_company_crawler.py --only-papers

# 内网直连超时时指定代理
python nowcoder_company_crawler.py --proxy http://proxyhk.zte.com.cn:80
```

### 参数说明

| 参数 | 说明 |
|------|------|
| `--career` | 职业 `careerJobId`（默认 11226=软件开发） |
| `--only-papers` | 只抓试卷列表，不抓各职业标签 |
| `--proxy` | 指定 HTTP 代理 |

### 输出

- `nowcoder_data/company_papers/tabs.json` — 全部 15 个职业分类
- `nowcoder_data/company_papers/tags_{职业}.json` — 各职业标签（年份/岗位/公司）
- `nowcoder_data/company_papers/papers_软件开发.json` — 软件开发下全部 2290 份试卷（含 paperId、公司、参与人数）
- `nowcoder_data/company_papers/README.md` — 汇总文档（职业表 + 各职业标签 + 试卷清单）

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
