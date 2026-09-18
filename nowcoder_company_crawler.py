"""
牛客网公司真题爬虫：试卷标签 + 指定职业分类下全部试卷
====================================================

数据来源（公司真题 written_page 页）：
  query-all-tab-list                      → 全部职业分类（tab）
  company-question/company-paper-tags     → 每类职业的标签（年份/岗位/公司）
  company-question/get-writtenPaper-list-pc → 试卷列表（分页）

用法：
  # 抓所有职业的标签 + 软件开发(careerJobId=11226)下全部试卷
  python nowcoder_company_crawler.py
  # 指定职业
  python nowcoder_company_crawler.py --career 11226
  # 内网直连超时时指定代理
  python nowcoder_company_crawler.py --proxy http://proxyhk.zte.com.cn:80

依赖：pip install curl_cffi
"""

import os, sys, json, re, time, argparse
from datetime import datetime
from curl_cffi import requests

OUTPUT_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(OUTPUT_DIR, 'nowcoder_data', 'company_papers')

BASE_API = 'https://gw-c.nowcoder.com/api/sparta'
TAB_LIST_URL = f'{BASE_API}/question-tab/query-all-tab-list'
TAGS_URL = f'{BASE_API}/company-question/company-paper-tags'
PAPER_LIST_URL = f'{BASE_API}/company-question/get-writtenPaper-list-pc'

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
    'Cookie': COOKIE,
}

PROXY = os.environ.get('NOWCODER_PROXY', '')

_session = None


def _get_session():
    global _session
    if _session is None:
        _session = requests.Session(impersonate='chrome124', timeout=30)
    return _session


def api_request(url, method='GET', params=None, body=None, retries=3, delay=1.0):
    """HTTP 请求，失败自动重试。连接超时给出代理排查提示"""
    sess = _get_session()
    kwargs = {'proxies': {'http': PROXY, 'https': PROXY}} if PROXY else {}
    for attempt in range(retries + 1):
        try:
            if method == 'GET':
                r = sess.get(url, params=params, headers=HEADERS, timeout=30, **kwargs)
            else:
                r = sess.post(url, params=params, json=body, headers=HEADERS, timeout=30, **kwargs)
            if r.status_code == 200:
                data = r.json()
                if data.get('code') == 999 or data.get('msg') == 'need login':
                    print('❌ Cookie 失效，请重新复制 cookie（需含 acw_tc）')
                    sys.exit(1)
                return data
            print(f'  ⚠️ HTTP {r.status_code}，重试 {attempt + 1}/{retries}')
        except Exception as e:
            msg = str(e)
            print(f'  ⚠️ 请求异常: {e}，重试 {attempt + 1}/{retries}')
            if attempt == retries and any(k in msg for k in ('timed out', 'timeout', 'Connection', 'connect')):
                print('  💡 连接超时通常是网络/代理问题：内网环境请设置 http_proxy/https_proxy，')
                print('     或用 --proxy http://代理地址:端口 指定代理后重试')
        time.sleep(delay * (attempt + 1))
    return None


def fetch_tabs():
    """所有职业分类 tab"""
    data = api_request(TAB_LIST_URL, 'GET')
    return data.get('data', []) if data else []


def fetch_tags(company_written_id, career_job_id):
    """某职业的试卷标签（年份/岗位/公司）"""
    data = api_request(TAGS_URL, 'GET',
                       params={'jobId': company_written_id, 'careerJobId': career_job_id})
    return data.get('data') if data else None


def fetch_papers(career_job_id, page, page_size=500, order=0):
    """一页试卷列表（接口单页上限 500，分页稳定，保证全量覆盖）"""
    data = api_request(PAPER_LIST_URL, 'POST', body={
        'order': order, 'careerJob': career_job_id, 'companyIds': [],
        'yearTags': [], 'jobIds': [], 'pageSize': page_size, 'page': page, 'query': ''})
    return data.get('data') if data else None


def fetch_all_papers(career_job_id):
    """某职业下全部试卷（pageSize=500 分页拉完，按 paperId 去重）"""
    all_records = []
    seen = set()
    page = 1
    total = None
    while True:
        d = fetch_papers(career_job_id, page)
        if not d:
            print('  ⚠️ 分页请求失败，停止')
            break
        recs = d.get('records', [])
        total = d.get('total', total)
        for p in recs:
            if p.get('paperId') not in seen:
                seen.add(p['paperId'])
                all_records.append(p)
        print(f'  第 {page} 页: {len(recs)} 份，累计 {len(all_records)}/{total}')
        if len(all_records) >= total or not recs:
            break
        page += 1
        time.sleep(0.4)
    return all_records


def save_json(name, obj):
    os.makedirs(DATA_DIR, exist_ok=True)
    safe = re.sub(r'[\\/:*?"<>|\s]+', '_', name).strip('_')
    path = os.path.join(DATA_DIR, f'{safe}.json')
    with open(path, 'w', encoding='utf-8') as f:
        json.dump(obj, f, ensure_ascii=False, indent=2)
    return path


def build_summary(tabs, tags_map, papers):
    """生成可读的汇总 Markdown"""
    lines = ['# 牛客网公司真题 · 试卷标签与软件开发试卷清单', '',
             f'> 抓取时间：{datetime.now().strftime("%Y-%m-%d %H:%M")}',
             f'> 数据来源：nowcoder.com/exam/company（written_page）', '']

    lines.append('## 一、全部职业分类（15 类）')
    lines.append('')
    lines.append('| 分类 | careerJobId | companyWrittenId |')
    lines.append('|------|-------------|------------------|')
    for t in tabs:
        lines.append(f"| {t['tabName']} | {t['careerJobId']} | {t.get('companyWrittenId', 0)} |")
    lines.append('')

    lines.append('## 二、各职业试卷标签')
    lines.append('')
    for name, tags in tags_map.items():
        if not tags:
            lines.append(f'### {name}（无标签数据）')
            continue
        lines.append(f'### {name}')
        years = tags.get('allYearTags', [])
        jobs = tags.get('jobTags', [])
        cos = tags.get('authCompanys', [])
        lines.append(f'- **年份标签**：{len(years)} 个 → {"、".join(t["name"] for t in years)}')
        lines.append(f'- **岗位标签**：{len(jobs)} 个 → {"、".join(t["name"] for t in jobs)}')
        lines.append(f'- **公司**：{len(cos)} 家 → {"、".join(t["name"] for t in cos)}')
        lines.append('')

    lines.append('## 三、软件开发下全部试卷')
    lines.append('')
    lines.append(f'共 **{len(papers)}** 份试卷')
    lines.append('')
    member = sum(1 for p in papers if p.get('memberLevel'))
    free = len(papers) - member
    lines.append(f'- 免费：{free} 份')
    lines.append(f'- 会员：{member} 份')
    lines.append('')
    lines.append('| 试卷名 | 公司 | 参与人数 | 会员 | 试卷ID | 链接 |')
    lines.append('|--------|------|----------|------|--------|------|')
    for p in papers:
        lines.append(f"| {p.get('paperName')} | {p.get('vCompany', '')} | {p.get('personTotal')} | "
                     f"{'是' if p.get('memberLevel') else '否'} | {p.get('paperId')} | "
                     f"[做题](https://www.nowcoder.com/exam/test/{p.get('paperId')}/summary) |")
    lines.append('')
    return '\n'.join(lines)


def main():
    parser = argparse.ArgumentParser(description='牛客网公司真题：试卷标签 + 指定职业全部试卷')
    parser.add_argument('--career', type=int, default=11226, help='职业 careerJobId（默认 11226=软件开发）')
    parser.add_argument('--proxy', help='HTTP 代理地址，如 http://127.0.0.1:7890')
    parser.add_argument('--only-papers', action='store_true', help='只抓试卷列表，不抓各职业标签')
    args = parser.parse_args()

    if args.proxy:
        global PROXY
        PROXY = args.proxy

    if not COOKIE or 'acw_tc' not in COOKIE:
        print('❌ 请设置 Cookie！')
        sys.exit(1)

    print('=== 1. 获取全部职业分类 ===')
    tabs = fetch_tabs()
    if not tabs:
        print('❌ 获取职业分类失败')
        sys.exit(1)
    for t in tabs:
        print(f"  {t['tabName']} (careerJobId={t['careerJobId']}, companyWrittenId={t.get('companyWrittenId', 0)})")
    save_json('tabs', [{'tabId': t['tabId'], 'tabName': t['tabName'],
                        'careerJobId': t['careerJobId'],
                        'companyWrittenId': t.get('companyWrittenId', 0),
                        'subTabs': [s['subTabName'] for s in t.get('subList', [])]} for t in tabs])

    tags_map = {}
    if not args.only_papers:
        print('\n=== 2. 抓取各职业试卷标签 ===')
        for t in tabs:
            cwid = t.get('companyWrittenId', 0)
            cjid = t.get('careerJobId', 0)
            name = t['tabName']
            if not cjid:
                print(f'  ⏭️ {name}: 无 careerJobId，跳过')
                continue
            print(f'  📥 {name} (companyWrittenId={cwid}, careerJobId={cjid}) ...')
            tags = fetch_tags(cwid, cjid)
            if not tags:
                print(f'    ⚠️ 无标签数据')
                continue
            tags_map[name] = tags
            save_json(f'tags_{name}', tags)
            jt = tags.get('jobTags') or []
            cos = tags.get('authCompanys') or []
            yrs = tags.get('allYearTags') or []
            print(f'    ✅ 年份 {len(yrs)}，岗位 {len(jt)}，公司 {len(cos)}')

    print(f'\n=== 3. 抓取职业 {args.career} 下全部试卷 ===')
    target_name = next((t['tabName'] for t in tabs if t['careerJobId'] == args.career), f'职业{args.career}')
    papers = fetch_all_papers(args.career)
    print(f'✅ {target_name} 共 {len(papers)} 份试卷')
    if papers:
        save_json(f'papers_{target_name}', papers)
        member = sum(1 for p in papers if p.get('memberLevel'))
        print(f'  免费 {len(papers) - member} 份，会员 {member} 份')

    print('\n=== 4. 生成汇总 Markdown ===')
    md = build_summary(tabs, tags_map, papers)
    os.makedirs(DATA_DIR, exist_ok=True)
    md_path = os.path.join(DATA_DIR, 'README.md')
    with open(md_path, 'w', encoding='utf-8') as f:
        f.write(md)
    print(f'✅ 完成！数据目录: {DATA_DIR}')
    print(f'  - tabs.json（职业分类）')
    print(f'  - tags_*.json（各职业标签）')
    print(f'  - papers_{target_name}.json（全部试卷）')
    print(f'  - README.md（汇总）')


if __name__ == '__main__':
    main()
