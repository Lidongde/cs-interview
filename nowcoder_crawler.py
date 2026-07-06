"""
牛客网专项练习爬虫 + 交互式 Markdown 生成器
============================================

功能：
1. 按标签（Java/Spring/Redis 等）爬取牛客专项练习题目
2. 两种爬取模式：
   - 智能组卷模式（默认）：创建试卷 → 提交答案 → 交卷 → 获取解析
   - 历史补全模式（--supplement）：从用户历史刷题记录提取题目+答案
3. 过滤相似题型（基于题干文本相似度）
4. 生成支持交互式做题的 Markdown 文档
   - <details> 折叠答案/解析（显隐答案）
   - 选择题可勾选选项自测
   - 填写回答区域
   - 进度统计表

用法：
  # 智能组卷模式（默认爬 Java 10 题）
  python nowcoder_crawler.py

  # 爬指定标签，各 20 题
  python nowcoder_crawler.py --tags 570 3935 21048 --count 20

  # 爬所有标签
  python nowcoder_crawler.py --all --count 10

  # 历史补全模式：从用户历史刷题记录补全题目（能拿到更多题）
  python nowcoder_crawler.py --supplement --tags 570 3935 21048

  # 只用已有 JSON 转 MD
  python nowcoder_crawler.py --only-md

数据来源（API 链路）：
  智能组卷：
    POST /api/sparta/common-practice/request-make-paper-pc  → 创建试卷
    POST /api/sparta/test/begin                             → 开始答题
    POST /api/sparta/test/detail                            → 获取题目+选项
    POST /api/sparta/test/recordAnswer                      → 提交答案
    POST /api/sparta/test/finish                            → 交卷
    POST /api/sparta/test/report                            → 获取答案+解析

  历史补全：
    GET  /api/sparta/user/question-training/test-papers/{uid}  → 用户试卷列表
    POST /api/sparta/test/report                               → 试卷题目+答案
    POST /api/sparta/test/detail                               → 题目选项

依赖：pip install curl_cffi
"""

import os, sys, json, re, time, argparse, hashlib
from datetime import datetime
from curl_cffi import requests

# =====================================================================
#  配置
# =====================================================================
OUTPUT_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(OUTPUT_DIR, 'nowcoder_data')
MD_DIR = os.path.join(DATA_DIR, 'output')

# API 端点
BASE_API = 'https://gw-c.nowcoder.com/api/sparta'
MAKE_PAPER_URL = f'{BASE_API}/common-practice/request-make-paper-pc'
TEST_BEGIN_URL = f'{BASE_API}/test/begin'
TEST_DETAIL_URL = f'{BASE_API}/test/detail'
TEST_RECORD_URL = f'{BASE_API}/test/recordAnswer'
TEST_FINISH_URL = f'{BASE_API}/test/finish'
TEST_REPORT_URL = f'{BASE_API}/test/report'
TEST_PAPERS_URL = f'{BASE_API}/user/question-training/test-papers'  # +/{uid}

# 用户 ID（从 cookie 的 NOWCODERUID 或登录信息获取，supplement 模式需要）
USER_ID = 77826278

# Cookie（需要从浏览器复制，关键：acw_tc + t + NOWCODERUID）
# 用法：在已登录的牛客页面 F12→Network→复制任意请求的 Cookie 头粘贴到这里
COOKIE = os.environ.get('NOWCODER_COOKIE', '') or (
    'Hm_lvt_a808a1326b6c06c437de769d1b85b870=1783324773,1783326792,1783327040,1783332669; '
    'HMACCOUNT=5B50E5714BA2371A; '
    'NOWCODERCLINETID=5C624A404D820BAA561A9E407C597491; '
    'NOWCODERUID=99DB5E9FA741DBE9F474F73C04CD2DE0; '
    'acw_tc=0a18ab6c17833326692832986e66ad88590a1857ddae18de8424446dd7c7f2; '
    'isAgreementChecked=true; '
    't=95DEC25319FA21258C369646734311BF; '
    'gr_user_id=8efaa278-603a-4231-b6df-e5959903fcdd; '
    'c196c3667d214851b11233f5c17f99d5_gr_session_id=697b7bd4-3ec7-4108-b9c0-d49935fc4cdb; '
    'Hm_lpvt_a808a1326b6c06c437de769d1b85b870=1783333797'
)

HEADERS = {
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'zh-CN,zh;q=0.9',
    'content-type': 'application/json',
    'origin': 'https://www.nowcoder.com',
    'referer': 'https://www.nowcoder.com/',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 '
                  '(KHTML, like Gecko) Chrome/150.0.0.0 Safari/537.36',
    'x-requested-with': 'XMLHttpRequest',
    'Cookie': COOKIE,
}

# 标签列表（id → 名称）
TAGS = {
    570: 'Java',
    3935: 'Spring',
    21048: 'Redis',
    21049: 'Kafka',
    604: '网络基础',
    607: '操作系统',
    606: '数据库',
    618: 'Linux',
    3410: '设计模式',
    612: '软件工程',
    578: '数组',
    580: '链表',
    583: '树',
    585: '哈希',
    590: '排序',
    3427: 'SQL',
    608: '加密和安全',
    3463: 'ZooKeeper',
    3457: 'Hive',
    3453: 'Hadoop',
    569: 'C++',
    573: 'Python',
    571: 'Javascript',
    617: 'Android',
    616: 'iOS',
}

# 名称 → ID 反查（supplement 模式按名称匹配试卷）
TAG_NAME_TO_ID = {v: k for k, v in TAGS.items()}

# 每次创建试卷默认 5 题（牛客限制）
QUESTIONS_PER_PAPER = 5


# =====================================================================
#  工具函数
# =====================================================================

def api_request(url, method='GET', body=None, retries=2, delay=0.5):
    """HTTP 请求，失败自动重试"""
    for attempt in range(retries + 1):
        try:
            if method == 'GET':
                r = requests.get(url, headers=HEADERS, impersonate='chrome124', timeout=20)
            else:
                r = requests.post(url, json=body, headers=HEADERS, impersonate='chrome124', timeout=20)
            if r.status_code == 200:
                data = r.json()
                if data.get('code') == 999 or data.get('msg') == 'need login':
                    print('❌ Cookie 失效，请重新复制 cookie（需含 acw_tc）')
                    sys.exit(1)
                return data
            print(f'  ⚠️ HTTP {r.status_code}，重试 {attempt + 1}/{retries}')
        except Exception as e:
            print(f'  ⚠️ 请求异常: {e}，重试 {attempt + 1}/{retries}')
        time.sleep(delay * (attempt + 1))
    return None


def html_to_text(html):
    """简单 HTML → 纯文本"""
    if not html:
        return ''
    t = re.sub(r'<br\s*/?>', '\n', html)
    t = re.sub(r'<p[^>]*>', '\n', t)
    t = re.sub(r'</p>', '', t)
    t = re.sub(r'<pre[^>]*>(.*?)</pre>', lambda m: '\n```\n' + m.group(1) + '\n```\n', t, flags=re.DOTALL)
    t = re.sub(r'<code>(.*?)</code>', lambda m: '`' + m.group(1) + '`', t, flags=re.DOTALL)
    t = re.sub(r'<strong[^>]*>(.*?)</strong>', r'**\1**', t, flags=re.DOTALL)
    t = re.sub(r'<b[^>]*>(.*?)</b>', r'**\1**', t, flags=re.DOTALL)
    t = re.sub(r'<em>(.*?)</em>', r'*\1*', t, flags=re.DOTALL)
    t = re.sub(r'<[^>]+>', '', t)
    entities = {'&nbsp;': ' ', '&gt;': '>', '&lt;': '<', '&amp;': '&',
                '&quot;': '"', '&#39;': "'", '&apos;': "'",
                '&times;': '×', '&divide;': '÷',
                '&ldquo;': '"', '&rdquo;': '"', '&lsquo;': "'", '&rsquo;': "'"}
    for ent, ch in entities.items():
        t = t.replace(ent, ch)
    t = re.sub(r'&#(\d+);', lambda m: chr(int(m.group(1))), t)
    t = re.sub(r'&#x([0-9a-fA-F]+);', lambda m: chr(int(m.group(1), 16)), t)
    t = re.sub(r'\n{3,}', '\n\n', t)
    return t.strip()


def question_hash(title):
    """计算题目标题的哈希（用于去重）"""
    clean = re.sub(r'[\s\u3000\uff00-\uffef，。、；：？！""''（）()【】《》\.\,\;\:\?\!]', '', title)
    return hashlib.md5(clean[:50].encode('utf-8')).hexdigest()


def is_similar(title1, title2, threshold=0.8):
    """判断两题是否相似（基于字符集 Jaccard 相似度）"""
    s1 = set(re.sub(r'[\s\u3000\uff00-\uffef，。、；：？！""''（）()【】《》]', '', title1))
    s2 = set(re.sub(r'[\s\u3000\uff00-\uffef，。、；：？！""''（）()【】《》]', '', title2))
    if not s1 or not s2:
        return False
    return len(s1 & s2) / len(s1 | s2) >= threshold


def normalize_question(raw, tag_id=None):
    """将 API 返回的原始题目统一为标准结构"""
    return {
        'id': raw.get('id'),
        'uuid': raw.get('uuid', ''),
        'type': raw.get('type'),  # 1=单选, 2=多选, 4=判断
        'title': html_to_text(raw.get('title', '')),
        'content': html_to_text(raw.get('content', '')),
        'options': [{'id': o['id'], 'content': html_to_text(o['content'])}
                    for o in raw.get('chooseAnswer', raw.get('answers', []))],
        'userAnswer': raw.get('userAnswerContent', ''),
        'analysis': html_to_text(raw.get('analysis', '')),
        'referenceAnswer': html_to_text(raw.get('referenceAnswer', '')),
        'isMember': raw.get('isMember', False),
        'tagId': tag_id or raw.get('tagId'),
    }


def load_existing(tag_id, tag_name):
    """加载已有 JSON 数据（断点续爬），返回 (list, set of hashes)"""
    slug = f'{tag_id}_{tag_name}'
    path = os.path.join(DATA_DIR, f'{slug}.json')
    if os.path.exists(path):
        try:
            with open(path, 'r', encoding='utf-8') as f:
                questions = json.load(f)
            return questions, {question_hash(q['title']) for q in questions}
        except Exception:
            pass
    return [], set()


def save_json(tag_id, tag_name, questions):
    """保存 JSON"""
    os.makedirs(DATA_DIR, exist_ok=True)
    slug = f'{tag_id}_{tag_name}'
    path = os.path.join(DATA_DIR, f'{slug}.json')
    with open(path, 'w', encoding='utf-8') as f:
        json.dump(questions, f, ensure_ascii=False, indent=2)
    return path


# =====================================================================
#  刷题状态查询
# =====================================================================

def get_tag_stats():
    """获取所有标签的刷题统计（rcount=已做题数, tcount=总题数, leftCount=剩余）
    返回 {tag_id: {'name':, 'tcount':, 'rcount':, 'leftCount':}}
    """
    url = f'{BASE_API}/intelligent/getPCIntelligentList?questionJobId=10'
    data = api_request(url, 'GET')
    if not data or not data.get('data'):
        return {}
    stats = {}
    for group in data['data'].get('tags', []):
        for item in group.get('items', []):
            stats[item['id']] = {
                'name': item['title'],
                'tcount': item.get('tcount', 0),
                'rcount': item.get('rcount', 0),
                'leftCount': item.get('leftCount', 0),
            }
    return stats


def is_tag_practiced(tag_id, tag_stats):
    """判断某标签是否已刷过题（rcount > 0）"""
    info = tag_stats.get(tag_id)
    if not info:
        return False, 0, 0
    return info['rcount'] > 0, info['rcount'], info['tcount']


# =====================================================================
#  模式一：智能组卷爬取
# =====================================================================

def fetch_one_paper(tag_id, paper_count):
    """创建一份试卷并获取题目+答案+解析"""
    # 1. 创建试卷
    result = api_request(MAKE_PAPER_URL, 'POST', {
        'tagIdSets': [str(tag_id)],
        'classifyName': '    ',
        'pageType': 'intelligent_page',
        'questionJobId': 10,
    })
    if not result or not result.get('data'):
        return []

    paper_data = result['data']
    paper_id = paper_data['paperId']
    test_id = paper_data['testId']
    print(f'  试卷 #{paper_count}: paperId={paper_id}, testId={test_id}')

    # 2. 开始答题
    result = api_request(TEST_BEGIN_URL, 'POST', {'testId': test_id, 'paperId': paper_id})
    if result and result.get('data'):
        test_id = result['data'].get('testId', test_id)

    # 3. 获取题目
    result = api_request(TEST_DETAIL_URL, 'POST', {'testId': test_id, 'paperId': paper_id})
    if not result or not result.get('data'):
        return []
    questions = result['data'].get('paperQuestionDetails', [])

    # 4. 提交所有题答案（随便选一个，目的是让 report 能返回解析）
    for q in questions:
        if q.get('chooseAnswer'):
            ans = str(q['chooseAnswer'][0]['id'])
            api_request(TEST_RECORD_URL, 'POST', {
                'questionId': q['id'], 'paperId': paper_id,
                'testId': test_id, 'answerContent': ans,
            })
            time.sleep(0.2)

    # 5. 交卷
    api_request(TEST_FINISH_URL, 'POST', {'testId': test_id, 'paperId': paper_id})

    # 6. 获取答案+解析
    result = api_request(TEST_REPORT_URL, 'POST', {'testId': test_id, 'paperId': paper_id})
    if not result or not result.get('data'):
        return []

    done_questions = result['data'].get('doneQuestionDetails', [])
    done_map = {q['uuid']: q for q in done_questions}
    merged = []
    for q in questions:
        done = done_map.get(q['uuid'], {})
        # 合并 detail 的选项 + report 的解析
        merged_raw = {**q, **{k: v for k, v in done.items() if k in (
            'analysis', 'referenceAnswer', 'userAnswerContent', 'isMember')}}
        merged.append(normalize_question(merged_raw, tag_id))
    return merged


def crawl_tag_intelligent(tag_id, tag_name, target_count=10):
    """智能组卷模式爬取指定标签"""
    print(f'\n{"=" * 60}')
    print(f'📥 [智能组卷] {tag_name} (tagId={tag_id}), 目标 {target_count} 题')
    print(f'{"=" * 60}')

    all_questions, seen_hashes = load_existing(tag_id, tag_name)
    if all_questions:
        print(f'  📂 已有 {len(all_questions)} 题，继续补充')

    if len(all_questions) >= target_count:
        print(f'  ✅ 已有 {len(all_questions)} 题 ≥ 目标 {target_count}，跳过')
        return all_questions[:target_count]

    paper_count = 0
    max_papers = (target_count // QUESTIONS_PER_PAPER) + max(10, target_count // 2)
    no_new_streak = 0

    while len(all_questions) < target_count and paper_count < max_papers:
        paper_count += 1
        questions = fetch_one_paper(tag_id, paper_count)

        new_count = 0
        for q in questions:
            h = question_hash(q['title'])
            if h in seen_hashes:
                continue
            if any(is_similar(q['title'], exist['title']) for exist in all_questions):
                continue
            seen_hashes.add(h)
            all_questions.append(q)
            new_count += 1

        if new_count == 0:
            no_new_streak += 1
        else:
            no_new_streak = 0

        print(f'  试卷 #{paper_count}: 本轮 {len(questions)} 题，新增 {new_count} 题，累计 {len(all_questions)} 题')

        if paper_count % 10 == 0:
            save_json(tag_id, tag_name, all_questions)

        if no_new_streak >= 8:
            print(f'  ⚠️ 连续 {no_new_streak} 轮无新题，题库可能已耗尽，停止')
            break

        time.sleep(0.8)

    all_questions = all_questions[:target_count]
    print(f'\n✅ {tag_name}: 共 {len(all_questions)} 题（去重后）')
    path = save_json(tag_id, tag_name, all_questions)
    print(f'💾 保存: {path}')
    return all_questions


# =====================================================================
#  模式二：历史记录补全
# =====================================================================

def fetch_all_papers():
    """获取用户所有历史试卷列表（分页）"""
    print('=== 获取用户历史试卷列表 ===')
    all_papers = []
    page = 1
    while True:
        url = f'{TEST_PAPERS_URL}/{USER_ID}?pageNo={page}&pageSize=100&onlyFinish=false'
        data = api_request(url, 'GET')
        if not data or not data.get('data'):
            break
        d = data['data']
        records = d.get('list', d.get('records', []))
        if not records:
            break
        all_papers.extend(records)
        total = d.get('totalCount', d.get('total', 0))
        print(f'  第 {page} 页: {len(records)} 份，累计 {len(all_papers)}/{total}')
        if len(all_papers) >= total or len(records) < 100:
            break
        page += 1
        time.sleep(0.3)
    return all_papers


def fetch_paper_questions(test_id, paper_id, tag_id=None):
    """用 test/report + test/detail 获取一份试卷的题目+答案解析"""
    # report 有答案解析
    report = api_request(TEST_REPORT_URL, 'POST', {'testId': test_id, 'paperId': paper_id})
    done_qs = []
    if report and report.get('data'):
        done_qs = report['data'].get('doneQuestionDetails', [])

    # detail 有选项
    detail = api_request(TEST_DETAIL_URL, 'POST', {'testId': test_id, 'paperId': paper_id})
    detail_map = {}
    if detail and detail.get('data'):
        for q in detail['data'].get('paperQuestionDetails', []):
            detail_map[q.get('uuid', '')] = q

    questions = []
    for q in done_qs:
        uuid = q.get('uuid', '')
        d = detail_map.get(uuid, {})
        # 合并：detail 的选项 + report 的解析
        merged = {**d, **{k: v for k, v in q.items() if k in (
            'analysis', 'referenceAnswer', 'userAnswerContent', 'isMember', 'type', 'title', 'id', 'uuid')}}
        questions.append(normalize_question(merged, tag_id))
    return questions


def crawl_tag_supplement(tag_id, tag_name, all_papers):
    """从历史试卷中补全指定标签的题目"""
    print(f'\n{"=" * 60}')
    print(f'📥 [历史补全] {tag_name} (tagId={tag_id})')
    print(f'{"=" * 60}')

    # 筛选该标签的试卷（试卷名含标签名）
    tag_papers = [p for p in all_papers
                  if tag_name in p.get('name', '')]
    print(f'  匹配到 {len(tag_papers)} 份历史试卷')

    if not tag_papers:
        print(f'  ⚠️ 无匹配试卷，跳过')
        return []

    # 加载已有数据
    all_questions, seen_hashes = load_existing(tag_id, tag_name)
    existing_list = list(all_questions)
    print(f'  已有 {len(existing_list)} 题')

    new_total = 0
    for i, p in enumerate(tag_papers):
        tid, pid = p['id'], p['paperId']
        try:
            questions = fetch_paper_questions(tid, pid, tag_id)
            new_count = 0
            for q in questions:
                h = question_hash(q['title'])
                if h not in seen_hashes:
                    if not any(is_similar(q['title'], exist['title']) for exist in existing_list):
                        seen_hashes.add(h)
                        existing_list.append(q)
                        new_count += 1
            new_total += new_count
            print(f'    试卷 {i+1}/{len(tag_papers)} (testId={tid}): {len(questions)} 题，新增 {new_total} 累计')
        except Exception as e:
            print(f'    试卷 {i+1} 失败: {e}')

        # 每 20 份保存一次
        if (i + 1) % 20 == 0:
            save_json(tag_id, tag_name, existing_list)

        time.sleep(0.3)

    print(f'\n✅ {tag_name}: 共 {len(existing_list)} 题（补全 +{new_total}）')
    path = save_json(tag_id, tag_name, existing_list)
    print(f'💾 保存: {path}')
    return existing_list


def crawl_all_supplement(tags):
    """历史补全模式：爬取所有指定标签"""
    os.makedirs(DATA_DIR, exist_ok=True)
    all_papers = fetch_all_papers()
    print(f'共 {len(all_papers)} 份历史试卷')

    all_data = {}
    for tag_id, tag_name in tags.items():
        questions = crawl_tag_supplement(tag_id, tag_name, all_papers)
        all_data[tag_id] = {'name': tag_name, 'questions': questions}

    save_index(all_data)
    return all_data


# =====================================================================
#  自动模式：智能判断策略
# =====================================================================

def crawl_tag_auto(tag_id, tag_name, target_count, tag_stats, all_papers):
    """自动决策爬取策略：
    - 未刷过题（rcount=0）：纯智能组卷（能拿到全部非会员题）
    - 已刷过题（rcount>0）：智能组卷 + 历史补全（组卷拿不到已做的题，需补全）
    """
    practiced, rcount, tcount = is_tag_practiced(tag_id, tag_stats)
    print(f'\n{"=" * 60}')
    print(f'📥 [自动] {tag_name} (tagId={tag_id})')
    print(f'   总题数={tcount}, 已做={rcount}, 剩余={tcount - rcount if tcount else "?"}')
    print(f'{"=" * 60}')

    if not practiced:
        # 未刷过题：纯智能组卷即可拿全部非会员题
        print(f'  → 策略：纯智能组卷（未刷过题，组卷可拿全部）')
        return crawl_tag_intelligent(tag_id, tag_name, target_count)
    else:
        # 已刷过题：智能组卷（只能拿未做过的）+ 历史补全（拿已做过的）
        print(f'  → 策略：智能组卷 + 历史补全（已刷过 {rcount} 题，组卷拿不到已做题）')
        # 智能组卷先拿未做过的题
        questions = crawl_tag_intelligent(tag_id, tag_name, target_count)
        # 历史补全补上已做过的题
        questions = crawl_tag_supplement(tag_id, tag_name, all_papers)
        return questions


def crawl_all_auto(tags, count=10000):
    """自动模式：查询刷题状态后，为每个标签选择最优策略"""
    os.makedirs(DATA_DIR, exist_ok=True)
    print('=== 查询标签刷题状态 ===')
    tag_stats = get_tag_stats()
    for tag_id, tag_name in tags.items():
        info = tag_stats.get(tag_id, {})
        print(f'  {tag_name:10} id={tag_id:8} 总数={info.get("tcount","?"):5} '
              f'已做={info.get("rcount","?"):5} 剩余={info.get("leftCount","?"):5}')

    # 预取历史试卷列表（supplement 模式需要）
    all_papers = []
    if any(is_tag_practiced(tid, tag_stats)[0] for tid in tags):
        print('\n=== 检测到有已刷过的标签，预取历史试卷列表 ===')
        all_papers = fetch_all_papers()
        print(f'共 {len(all_papers)} 份历史试卷')
    else:
        print('\n=== 所有标签均未刷过，无需历史补全 ===')

    all_data = {}
    for tag_id, tag_name in tags.items():
        questions = crawl_tag_auto(tag_id, tag_name, count, tag_stats, all_papers)
        all_data[tag_id] = {'name': tag_name, 'questions': questions}

    save_index(all_data)
    return all_data


# =====================================================================
#  统一入口
# =====================================================================

def crawl_all(tags, count=10):
    """智能组卷模式：爬取所有标签"""
    os.makedirs(DATA_DIR, exist_ok=True)
    all_data = {}
    for tag_id, tag_name in tags.items():
        questions = crawl_tag_intelligent(tag_id, tag_name, count)
        all_data[tag_id] = {'name': tag_name, 'questions': questions}
    save_index(all_data)
    return all_data


def save_index(all_data):
    """保存索引文件"""
    index_path = os.path.join(DATA_DIR, 'index.json')
    with open(index_path, 'w', encoding='utf-8') as f:
        json.dump({
            'crawled_at': datetime.now().isoformat(),
            'tags': {tid: d['name'] for tid, d in all_data.items()},
            'counts': {str(tid): len(d['questions']) for tid, d in all_data.items()},
        }, f, ensure_ascii=False, indent=2)


# =====================================================================
#  Markdown 生成（交互式做题）
# =====================================================================

TYPE_LABEL = {1: '单选', 2: '多选', 4: '判断'}


def build_question_md(q, idx, tag_name):
    """生成单题的交互式 Markdown"""
    qtype = TYPE_LABEL.get(q['type'], '未知')
    lines = []
    anchor = f'q-{tag_name}-{idx}'
    lines.append(f'<a id="{anchor}"></a>')
    lines.append(f'### 第 {idx} 题  [{qtype}]')

    lines.append(f'> 标签：`{tag_name}` ｜ 类型：`{qtype}`')
    content = q.get('content') or q.get('title', '')
    lines.append('')
    lines.append(content)
    lines.append('')

    # 选项（可勾选自测）
    if q.get('options'):
        lines.append('**选项**（勾选你的答案）：')
        lines.append('')
        for i, opt in enumerate(q['options']):
            letter = chr(65 + i)
            lines.append(f'- [ ] **{letter}.** {opt["content"]}')
        lines.append('')

    # 填写回答区
    lines.append('**我的回答**：')
    lines.append('')
    lines.append('________________________________________')
    lines.append('')

    # 答案 + 解析（折叠）
    answer = q.get('referenceAnswer', '')
    analysis = q.get('analysis', '')
    user_ans = q.get('userAnswer', '')

    lines.append('<details>')
    lines.append('<summary>💡 点击查看答案与解析</summary>')
    lines.append('')

    if answer:
        lines.append(f'**参考答案**：{answer}')
        lines.append('')

    if q.get('options') and user_ans:
        ans_ids = [aid.strip() for aid in str(user_ans).split(',')]
        chosen = [opt['content'] for opt in q['options'] if str(opt['id']) in ans_ids]
        if chosen:
            lines.append(f'**爬虫提交的答案**：{", ".join(chosen)}（仅用于触发解析，不一定正确）')
            lines.append('')

    if analysis:
        lines.append('**官方解析**：')
        lines.append('')
        lines.append(analysis)
        lines.append('')

    if not answer and not analysis:
        lines.append('*（本题解析为会员内容，暂无法获取）*')
        lines.append('')

    lines.append('</details>')
    lines.append('')
    lines.append('---')
    lines.append('')
    return '\n'.join(lines)


def build_tag_md(tag_name, questions):
    """生成一个标签的完整 Markdown 文档"""
    slug = re.sub(r'[^\w\u4e00-\u9fff]', '-', tag_name).strip('-')
    lines = [
        f'# 📝 {tag_name} 专项练习',
        '',
        f'> 共 {len(questions)} 题 ｜ 牛客网爬取 ｜ {datetime.now().strftime("%Y-%m-%d")}',
        f'> 交互功能：勾选选项自测 → 写下回答 → 点击展开答案解析',
        '',
        '## 📊 进度统计',
        '',
        '| 指标 | 数值 |',
        '|------|------|',
        f'| 总题数 | {len(questions)} |',
        '| 已练习 | <span id="done-count">0</span> |',
        '| 已掌握 | <span id="mastered-count">0</span> |',
        '| 正确率 | <span id="accuracy">—</span> |',
        '',
        f'> 💡 进度数据保存在浏览器 localStorage（key: `nowcoder_{slug}`）',
        '',
        '---',
        '',
        '## 📑 目录',
        '',
    ]

    for i, q in enumerate(questions, 1):
        title_short = (q.get('title', ''))[:40].replace('\n', ' ')
        lines.append(f'{i}. [{title_short}](#q-{slug}-{i})')

    lines.append('')
    lines.append('---')
    lines.append('')

    for i, q in enumerate(questions, 1):
        lines.append(build_question_md(q, i, slug))

    return '\n'.join(lines), slug


def run_convert():
    """将 JSON 转换为交互式 Markdown"""
    os.makedirs(MD_DIR, exist_ok=True)
    json_files = [f for f in os.listdir(DATA_DIR) if f.endswith('.json') and f != 'index.json']

    if not json_files:
        print('⚠️ 没有找到 JSON 数据文件，请先运行爬取')
        return

    for jf in sorted(json_files):
        path = os.path.join(DATA_DIR, jf)
        with open(path, 'r', encoding='utf-8') as f:
            questions = json.load(f)
        if not questions:
            continue
        m = re.match(r'\d+_(.+)', jf.replace('.json', ''))
        tag_name = m.group(1) if m else jf.replace('.json', '')

        print(f'📄 生成: {tag_name} ({len(questions)} 题)...')
        md, slug = build_tag_md(tag_name, questions)
        out_path = os.path.join(MD_DIR, f'{slug}.md')
        with open(out_path, 'w', encoding='utf-8') as f:
            f.write(md)
        print(f'  ✅ {slug}.md ({len(md)} 字符)')

    # 生成 README
    readme = f"""# 牛客网专项练习题集

> 爬取时间：{datetime.now().strftime("%Y-%m-%d")}
> 数据来源：nowcoder.com 专项练习

## 题集

| 标签 | 文件 |
|------|------|
"""
    for jf in sorted(json_files):
        m = re.match(r'\d+_(.+)', jf.replace('.json', ''))
        name = m.group(1) if m else jf
        readme += f"| {name} | `{name}.md` |\n"

    readme += """
## 交互功能说明

- **勾选选项**：点击选项前的方框勾选你的答案
- **填写回答**：在"我的回答"下划线处写下思路
- **查看答案**：点击"💡 点击查看答案与解析"展开
- **进度统计**：顶部表格显示练习进度（需支持 localStorage 的编辑器）

## 难度与类型

- [单选] 单选题
- [多选] 多选题
- [判断] 判断题
"""
    with open(os.path.join(MD_DIR, 'README.md'), 'w', encoding='utf-8') as f:
        f.write(readme)
    print(f'\n✅ 全部完成！文件保存在 {MD_DIR}/')


# =====================================================================
#  入口
# =====================================================================

def main():
    parser = argparse.ArgumentParser(
        description='牛客网专项练习爬虫 + 交互式 Markdown 生成器',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
示例:
  python nowcoder_crawler.py                              # 自动模式爬 Java（默认全部）
  python nowcoder_crawler.py --tags 570 3935 21048         # 自动模式爬指定标签
  python nowcoder_crawler.py --count 50                    # 限制每标签 50 题
  python nowcoder_crawler.py --supplement-only --tags 570  # 强制只用历史补全
  python nowcoder_crawler.py --only-md                     # 只用已有 JSON 转 MD
  python nowcoder_crawler.py --no-md                       # 爬取后不生成 MD

策略说明:
  自动模式（默认）：先查询刷题状态
    - 未刷过的标签 → 纯智能组卷（能拿全部非会员题）
    - 已刷过的标签 → 智能组卷 + 历史补全（补回已做题）
        """)
    parser.add_argument('--tags', nargs='*', type=int, help='标签 ID 列表（如 570 3935 21048）')
    parser.add_argument('--all', action='store_true', help='爬取所有标签')
    parser.add_argument('--count', type=int, default=10000,
                        help='每个标签爬取题数上限（默认 10000=全部，仅智能组卷阶段生效）')
    parser.add_argument('--supplement-only', action='store_true',
                        help='强制只用历史补全模式（不做智能组卷）')
    parser.add_argument('--only-md', action='store_true', help='只用已有 JSON 转 MD（不爬取）')
    parser.add_argument('--no-md', action='store_true', help='爬取后不生成 MD')
    args = parser.parse_args()

    if args.only_md:
        run_convert()
        return

    if not COOKIE or 'acw_tc' not in COOKIE:
        print('❌ 请设置 Cookie！')
        print('   方法：在已登录的牛客页面 F12→Network→复制任意请求的 Cookie 头')
        print('   然后设置环境变量：set NOWCODER_COOKIE=你的cookie')
        print('   或修改本脚本顶部的 COOKIE 变量')
        sys.exit(1)

    # 确定标签
    if args.all:
        tags = TAGS
    elif args.tags:
        tags = {tid: TAGS.get(tid, f'标签{tid}') for tid in args.tags}
    else:
        tags = {570: 'Java'}

    # 执行爬取
    if args.supplement_only:
        print(f'🔄 历史补全模式，标签: {list(tags.values())}')
        all_data = crawl_all_supplement(tags)
    else:
        print(f'🔄 自动模式，标签: {list(tags.values())}')
        all_data = crawl_all_auto(tags, args.count)

    # 生成 Markdown（默认生成，--no-md 跳过）
    if not args.no_md:
        run_convert()
    else:
        print('\n⏭️ 跳过 MD 生成（--no-md）')

    # 汇总
    total = sum(len(d['questions']) for d in all_data.values())
    print(f'\n{"=" * 60}')
    print(f'✅ 全部完成！共 {total} 题，{len(all_data)} 个标签')
    print(f'📁 JSON: {DATA_DIR}')
    if not args.no_md:
        print(f'📁 Markdown: {MD_DIR}')
    print(f'{"=" * 60}')


if __name__ == '__main__':
    main()
