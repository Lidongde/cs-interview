"""
LeetCode 题目爬虫 + Markdown 转换器
====================================

功能：
1. 爬取题单列表 & 题目详情（JSON）
2. 转换为可读 MD 文档（题面→Markdown、带难度徽章、代码模板）

用法：
  python leetcode_crawler.py                   # 只爬取列表（不爬详情、不转 MD）
  python leetcode_crawler.py --detail          # 爬取列表 + 全部题目详情
  python leetcode_crawler.py --md              # 爬取列表 + 转 MD（不爬详情）
  python leetcode_crawler.py --detail --md     # 全流程：爬取 + 详情 + 转 MD
  python leetcode_crawler.py --only-md         # 只用已有 JSON 转 MD（跳过爬取）

数据来源：
- REST  /api/problems/all/          → 全部题目的元数据
- GraphQL  studyPlanV2Detail        → 热题 100、面试 150
- GraphQL  favoriteQuestionList     → 剑指Offer专项
- GraphQL  questionDetail           → 每道题的题面、代码模板等
"""

import json, re, os, time, sys
from curl_cffi import requests
from datetime import datetime

# =====================================================================
#  配置
# =====================================================================
OUTPUT_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(OUTPUT_DIR, 'leetcode_data')
DETAILS_DIR = os.path.join(DATA_DIR, 'details')
MD_DIR = os.path.join(DATA_DIR, 'output')
GRAPHQL_URL = 'https://leetcode.cn/graphql/'
REST_API_URL = 'https://leetcode.cn/api/problems/all/'

HEADERS_GQL = {
    'Origin': 'https://leetcode.cn',
    'Referer': 'https://leetcode.cn/problemset/',
    'Content-Type': 'application/json',
    'Accept': 'application/json',
}
IMPERSONATE_GQL = 'safari17_0'      # GraphQL 需要 Safari 指纹绕过 CF
IMPERSONATE_REST = 'chrome124'      # REST API 用 Chrome

STUDY_PLANS = {
    "top-100-liked": "热题 100",
    "top-interview-150": "面试经典 150",
}
FAVORITE_LISTS = {
    "8LSpuXqD": "剑指Offer专项突破",
}

# =====================================================================
#  工具函数
# =====================================================================

def gql_query(operation_name, query_str, variables, impersonate=IMPERSONATE_GQL, retries=2):
    """执行 GraphQL 查询，失败自动重试"""
    payload = {
        "operationName": operation_name,
        "variables": variables,
        "query": query_str.strip()
    }
    for attempt in range(retries + 1):
        r = requests.post(GRAPHQL_URL, json=payload, headers=HEADERS_GQL, impersonate=impersonate)
        if r.status_code == 429:
            wait = 3 * (attempt + 1)
            print(f"  ⚠️ 限流，等待 {wait} 秒...")
            time.sleep(wait)
            continue
        if r.status_code == 200:
            return r.json()
        print(f"  ❌ HTTP {r.status_code}，重试 {attempt + 1}/{retries}")
        time.sleep(2)
    return None


def rest_get(url, impersonate=IMPERSONATE_REST):
    """执行 REST API 请求"""
    r = requests.get(url, impersonate=impersonate)
    return r.json() if r.status_code == 200 else None


# =====================================================================
#  爬虫部分
# =====================================================================

def fetch_all_problems_meta():
    """从 /api/problems/all/ 获取全部题目的元数据"""
    print("=" * 60)
    print("📥 步骤 1: 获取全部题目元数据")
    print("=" * 60)

    data = rest_get(REST_API_URL)
    if not data:
        print("❌ 获取全部题目数据失败！")
        return {}

    problems = {}
    for pair in data.get('stat_status_pairs', []):
        stat = pair.get('stat', {})
        slug = stat.get('question__title_slug', '')
        if slug:
            problems[slug] = {
                'question_id': stat.get('question_id'),
                'frontend_question_id': str(stat.get('frontend_question_id', '')),
                'title': stat.get('question__title', ''),
                'slug': slug,
                'difficulty_level': pair.get('difficulty', {}).get('level'),
                'paid_only': pair.get('paid_only', False),
                'total_acs': stat.get('total_acs', 0),
                'total_submitted': stat.get('total_submitted', 0),
                'ac_rate': round(stat.get('total_acs', 0) / max(stat.get('total_submitted', 1), 1), 4),
                'is_new': stat.get('is_new_question', False),
            }
    print(f"✅ 获取了 {len(problems)} 道题的元数据")
    return problems


def fetch_study_plan(plan_slug, plan_name):
    """通过 studyPlanV2Detail 获取学习计划题目"""
    print(f"\n📥 获取学习计划: {plan_name} ({plan_slug})")
    query = """
    query studyPlanDetail($planSlug: String!) {
      studyPlanV2Detail(planSlug: $planSlug) {
        name
        planSubGroups {
          name slug
          questions {
            titleSlug title translatedTitle questionFrontendId difficulty
          }
        }
      }
    }
    """
    result = gql_query("studyPlanDetail", query, {"planSlug": plan_slug})
    if not result or 'errors' in result:
        print(f"  ❌ 获取失败")
        return []
    plan = result.get('data', {}).get('studyPlanV2Detail', {})
    all_questions = []
    for sg in plan.get('planSubGroups', []):
        chapter = sg.get('name', '')
        for q in sg.get('questions', []):
            all_questions.append({
                'titleSlug': q['titleSlug'],
                'titleCn': q.get('translatedTitle', q.get('title', '')),
                'frontendQuestionId': q.get('questionFrontendId', ''),
                'difficulty': q['difficulty'],
                'chapter': chapter,
                'planName': plan_name,
                'planSlug': plan_slug,
            })
    print(f"  ✅ {len(all_questions)} 道题")
    return all_questions


def fetch_favorite_list(list_slug, list_name):
    """通过 favoriteQuestionList 获取收藏夹题单"""
    print(f"\n📥 获取题单: {list_name} ({list_slug})")
    query = """
    query favoriteQuestionList($favoriteSlug: String!, $limit: Int, $skip: Int) {
      favoriteQuestionList(favoriteSlug: $favoriteSlug, limit: $limit, skip: $skip) {
        questions {
          titleSlug title translatedTitle questionFrontendId difficulty
          topicTags { name nameTranslated }
        }
      }
    }
    """
    result = gql_query("favoriteQuestionList", query,
                       {"favoriteSlug": list_slug, "limit": 200, "skip": 0})
    if not result or 'errors' in result:
        print(f"  ❌ 获取失败")
        return []
    questions_data = result.get('data', {}).get('favoriteQuestionList', {}).get('questions', [])
    all_questions = []
    for q in questions_data:
        all_questions.append({
            'titleSlug': q['titleSlug'],
            'titleCn': q.get('translatedTitle', q.get('title', '')),
            'frontendQuestionId': q.get('questionFrontendId', ''),
            'difficulty': q['difficulty'],
            'topics': [t.get('nameTranslated', t.get('name', '')) for t in q.get('topicTags', [])],
            'planName': list_name,
            'planSlug': list_slug,
        })
    print(f"  ✅ {len(all_questions)} 道题")
    return all_questions


QUESTION_DETAIL_QUERY = """
query getQuestionDetail($titleSlug: String!) {
  question(titleSlug: $titleSlug) {
    questionId questionFrontendId title translatedTitle titleSlug
    content translatedContent difficulty
    topicTags { name slug }
    hints sampleTestCase exampleTestcases metaData
    codeSnippets { lang langSlug code }
    stats similarQuestions enableRunCode enableSubmit
  }
}
"""


def extract_images_from_content(content_html):
    """从题面 HTML 中提取图片 URL"""
    if not content_html:
        return []
    urls = re.findall(r'<img[^>]+src=["\']([^"\']+)["\']', content_html)
    urls += re.findall(r'!\[.*?\]\(([^)]+)\)', content_html)
    result = []
    for url in urls:
        if url.startswith('http'):
            result.append(url)
        elif url.startswith('/'):
            result.append(f'https://leetcode.cn{url}')
        elif url.startswith('data:image'):
            fmt = re.search(r'data:image/(\w+);', url)
            f = fmt.group(1) if fmt else 'unknown'
            result.append(f'[base64 image/{f}, {len(url)} chars]')
    return result


def fetch_question_detail(slug):
    """通过 GraphQL 获取单题详情"""
    result = gql_query("getQuestionDetail", QUESTION_DETAIL_QUERY, {"titleSlug": slug})
    if not result or 'errors' in result:
        return None
    return result.get('data', {}).get('question')


def run_crawl(include_detail=False):
    """执行完整爬取流程"""
    os.makedirs(DATA_DIR, exist_ok=True)

    all_meta = fetch_all_problems_meta()
    with open(os.path.join(DATA_DIR, 'all_problems_meta.json'), 'w', encoding='utf-8') as f:
        json.dump(all_meta, f, ensure_ascii=False, indent=2)

    all_list_questions = []
    plan_groups = {}

    for slug, name in STUDY_PLANS.items():
        questions = fetch_study_plan(slug, name)
        all_list_questions.extend(questions)
        plan_groups[slug] = questions

    for slug, name in FAVORITE_LISTS.items():
        questions = fetch_favorite_list(slug, name)
        all_list_questions.extend(questions)
        plan_groups[slug] = questions

    for slug, questions in plan_groups.items():
        display_name = STUDY_PLANS.get(slug, FAVORITE_LISTS.get(slug, slug))
        path = os.path.join(DATA_DIR, f"{slug}.json")
        with open(path, 'w', encoding='utf-8') as f:
            json.dump(questions, f, ensure_ascii=False, indent=2)
        print(f"\n💾 已保存: {slug}.json ({len(questions)} 题, {display_name})")

    combined = {
        'meta': {
            'crawled_at': datetime.now().isoformat(),
            'total_problems': len(all_meta),
            'plans': {s: STUDY_PLANS.get(s, FAVORITE_LISTS.get(s, s)) for s in plan_groups},
        },
        'all_problems_meta': all_meta,
        'problem_lists': plan_groups,
    }
    with open(os.path.join(DATA_DIR, 'combined.json'), 'w', encoding='utf-8') as f:
        json.dump(combined, f, ensure_ascii=False, indent=2)
    print(f"\n💾 已保存: combined.json")

    if include_detail:
        print("\n" + "=" * 60)
        print("📥 步骤 4: 爬取题目详情")
        print("=" * 60)

        all_slugs = list(set(q['titleSlug'] for q in all_list_questions))
        print(f"需要爬取 {len(all_slugs)} 道题的详情（去重）")
        os.makedirs(DETAILS_DIR, exist_ok=True)

        detailed_problems = {}
        for i, slug in enumerate(all_slugs):
            print(f"  [{i+1}/{len(all_slugs)}] {slug}...", end=' ', flush=True)
            detail = fetch_question_detail(slug)
            if detail:
                content = detail.get('translatedContent') or detail.get('content', '')
                info = {
                    'slug': slug,
                    'questionId': detail.get('questionId'),
                    'frontendQuestionId': detail.get('questionFrontendId'),
                    'title': detail.get('title'),
                    'translatedTitle': detail.get('translatedTitle'),
                    'content': content,
                    'difficulty': detail.get('difficulty'),
                    'topicTags': [{'name': t.get('name')} for t in detail.get('topicTags', [])],
                    'hints': detail.get('hints', []),
                    'images': extract_images_from_content(content),
                    'codeSnippets': detail.get('codeSnippets', []),
                    'stats': detail.get('stats'),
                }
                detailed_problems[slug] = info
                with open(os.path.join(DETAILS_DIR, f"{slug}.json"), 'w', encoding='utf-8') as f:
                    json.dump(info, f, ensure_ascii=False, indent=2)
                print(f"✅ (题面: {len(content)}字, 图片: {len(info['images'])}张)")
            else:
                detailed_problems[slug] = None
                print(f"❌")
            time.sleep(0.3)

        with open(os.path.join(DETAILS_DIR, '_summary.json'), 'w', encoding='utf-8') as f:
            json.dump(detailed_problems, f, ensure_ascii=False, indent=2)

        ok = sum(1 for v in detailed_problems.values() if v)
        imgs = sum(len(v.get('images', [])) for v in detailed_problems.values() if v)
        print(f"\n📊 详情爬取统计: 成功 {ok}/{len(all_slugs)}，图片 {imgs} 张")

    print("\n" + "=" * 60)
    print("✅ 爬取完成！")
    print(f"📁 数据目录: {DATA_DIR}")
    print("=" * 60)
    return plan_groups


# =====================================================================
#  Markdown 转换部分
# =====================================================================

def html_to_markdown(html):
    """将 LeetCode 题面 HTML 转换为可读 Markdown"""
    if not html:
        return ''
    t = html
    t = re.sub(r'<img[^>]+src="([^"]+)"[^>]*alt="([^"]*)"[^>]*>', r'![\2](\1)', t)
    t = re.sub(r'<img[^>]+src="([^"]+)"[^>]*>', r'![](\1)', t)
    t = re.sub(r'<code>(.*?)</code>', lambda m: f'`{m.group(1)}`', t, flags=re.DOTALL)
    t = re.sub(r'<pre>(.*?)</pre>', lambda m: f'```\n{m.group(1).strip()}\n```', t, flags=re.DOTALL)
    t = re.sub(r'<strong[^>]*>(.*?)</strong>', r'**\1**', t, flags=re.DOTALL)
    t = re.sub(r'<em>(.*?)</em>', r'*\1*', t, flags=re.DOTALL)
    t = re.sub(r'<p[^>]*>(.*?)</p>', r'\1\n\n', t, flags=re.DOTALL)
    t = re.sub(r'<br\s*/?>', '\n', t)
    t = re.sub(r'<li[^>]*>(.*?)</li>', lambda m: f'- {m.group(1).strip()}\n', t, flags=re.DOTALL)
    t = re.sub(r'</?ul[^>]*>', '', t)
    t = re.sub(r'<ol[^>]*>(.*?)</ol>', lambda m: re.sub(r'<li>', '1. ', m.group(1)), t, flags=re.DOTALL)
    t = re.sub(r'\n{3,}', '\n\n', t)
    t = t.replace('&nbsp;', ' ')
    t = re.sub(r'<sup>(.*?)</sup>', r'^{\1}', t)
    t = re.sub(r'<sub>(.*?)</sub>', r'_{\1}', t)
    t = re.sub(r'<[^>]+>', '', t)
    t = t.replace('&gt;', '>').replace('&lt;', '<').replace('&amp;', '&')
    t = re.sub(r'\n{3,}', '\n\n', t)
    return t.strip()


def difficulty_badge(d):
    return {'EASY': '🟢 简单', 'MEDIUM': '🟡 中等', 'HARD': '🔴 困难'}.get(d.upper() if d else 'MEDIUM', d)


def build_problem_section(slug, list_info):
    """构建单题的 Markdown 章节"""
    detail_path = os.path.join(DETAILS_DIR, f'{slug}.json')
    detail = {}
    if os.path.exists(detail_path):
        with open(detail_path, 'r', encoding='utf-8') as f:
            detail = json.load(f)

    qid = list_info.get('frontendQuestionId', detail.get('frontendQuestionId', ''))
    title_cn = list_info.get('titleCn', detail.get('translatedTitle', detail.get('title', slug)))
    diff = list_info.get('difficulty', detail.get('difficulty', 'MEDIUM'))

    # 用 slug 做稳定锚点，方便外部直链
    slug_anchor = slug.replace('_', '-').lower()
    lines = [f'<a id="{slug_anchor}"></a>']
    lines.append(f'### {qid}. {title_cn}  {difficulty_badge(diff)}')

    tags = list_info.get('topics', [t.get('name', '') for t in detail.get('topicTags', [])])
    if tags:
        lines.append(f'> 标签：`{"` `".join(tags)}`')
    lines.append(f'> 🔗 <https://leetcode.cn/problems/{slug}/>')
    chapter = list_info.get('chapter', '')
    if chapter:
        lines.append(f'> 章节：{chapter}')
    lines.append('')

    content = detail.get('content', '')
    if content:
        lines.append(html_to_markdown(content))
        lines.append('')

    hints = detail.get('hints', [])
    if hints:
        lines.append('<details>\n<summary>💡 提示（点击展开）</summary>\n')
        for i, h in enumerate(hints, 1):
            lines.append(f'{i}. {html_to_markdown(h)}')
        lines.append('\n</details>\n')

    snippets = detail.get('codeSnippets', [])
    py_snippet = next((s for s in snippets if s.get('langSlug') == 'python3'), None)
    others = [s for s in snippets if s.get('langSlug') in ('java', 'cpp', 'javascript')]

    if py_snippet:
        lines.append('```python\n' + py_snippet['code'].rstrip() + '\n```\n')

    if others:
        lang_map = {'java': 'java', 'cpp': 'cpp', 'javascript': 'js'}
        lines.append('<details>\n<summary>其他语言模板</summary>\n')
        for s in others:
            lines.append(f'**{s["lang"]}**\n```{lang_map.get(s["langSlug"], "")}\n{s["code"].rstrip()}\n```\n')
        lines.append('</details>\n')

    return '\n'.join(lines)


def build_plan_doc(plan_name, list_data):
    """构建一个题单的完整 MD 文档"""
    lines = [
        f'# 📚 {plan_name}',
        '',
        f'> 共 {len(list_data)} 题 · LeetCode 爬虫生成 · {datetime.now().strftime("%Y-%m-%d")}',
        '',
        '---', ''
    ]

    chapters = {}
    for item in list_data:
        ch = item.get('chapter')
        if not ch:
            topics = item.get('topics', [])
            ch = topics[0] if topics else '其他'
        chapters.setdefault(ch, []).append(item)

    lines.append('## 📑 目录\n')
    for ch, qs in chapters.items():
        lines.append(f'- [{ch} ({len(qs)}题)](#{ch})')
    lines.append('\n---\n')

    for ch, qs in chapters.items():
        lines.append(f'## {ch}\n\n共 {len(qs)} 题\n')
        for item in qs:
            lines.append(build_problem_section(item['titleSlug'], item))
            lines.append('---\n')

    return '\n'.join(lines)


def run_convert():
    """将 JSON 转换为 MD 文档"""
    os.makedirs(MD_DIR, exist_ok=True)
    configs = [
        ('top-100-liked.json', '热题 100', 'top-100-liked.md'),
        ('top-interview-150.json', '面试经典 150', 'top-interview-150.md'),
        ('8LSpuXqD.json', '剑指Offer 专项突破', 'jianzhi-offer.md'),
    ]

    for in_file, plan_name, out_file in configs:
        in_path = os.path.join(DATA_DIR, in_file)
        if not os.path.exists(in_path):
            print(f'⚠️ 缺失: {in_file}')
            continue
        with open(in_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        print(f'📄 正在生成: {plan_name} ({len(data)} 题)...')
        md = build_plan_doc(plan_name, data)
        out_path = os.path.join(MD_DIR, out_file)
        with open(out_path, 'w', encoding='utf-8') as f:
            f.write(md)
        print(f'  ✅ {out_file} ({len(md)} 字符)')

    try:
        h = len(json.load(open(os.path.join(DATA_DIR, 'top-100-liked.json'), encoding='utf-8')))
        i = len(json.load(open(os.path.join(DATA_DIR, 'top-interview-150.json'), encoding='utf-8')))
        j = len(json.load(open(os.path.join(DATA_DIR, '8LSpuXqD.json'), encoding='utf-8')))
    except Exception:
        h = i = j = 0

    readme = f"""# LeetCode 题集

> 爬取时间：{datetime.now().strftime("%Y-%m-%d")}
> 数据来源：LeetCode.cn

## 题单

| 题单 | 数量 | 文件 |
|------|------|------|
| [热题 100](top-100-liked.md) | {h} | `top-100-liked.md` |
| [面试经典 150](top-interview-150.md) | {i} | `top-interview-150.md` |
| [剑指Offer 专项突破](jianzhi-offer.md) | {j} | `jianzhi-offer.md` |

## 说明

- 每道题包含：题号、中文标题、难度、标签、题面正文、提示、代码模板
- 难度标识：🟢 简单 🟡 中等 🔴 困难
- 代码模板默认展示 Python3，其他语言折叠显示
"""
    readme_path = os.path.join(MD_DIR, 'README.md')
    with open(readme_path, 'w', encoding='utf-8') as f:
        f.write(readme)
    print(f'\n✅ 全部完成！文件保存在 {MD_DIR}/')
    print('📄 README.md 已生成')


# =====================================================================
#  入口
# =====================================================================

if __name__ == '__main__':
    args = sys.argv[1:]

    do_crawl = '--only-md' not in args
    do_detail = '--detail' in args or '--with-details' in args
    do_md = '--md' in args or '--markdown' in args

    if do_crawl:
        run_crawl(include_detail=do_detail)
    else:
        print("⏭️ 跳过爬取（--only-md），直接转换已有 JSON")

    if do_md or '--only-md' in args:
        run_convert()
    else:
        print("\n💡 提示：加 --md 参数可一步转换 Markdown 文档")
        print("   python leetcode_crawler.py --md")