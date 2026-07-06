import json
from curl_cffi import requests

COOKIE = 'Hm_lvt_a808a1326b6c06c437de769d1b85b870=1783324773; NOWCODERCLINETID=5C624A404D820BAA561A9E407C597491; NOWCODERUID=99DB5E9FA741DBE9F474F73C04CD2DE0; acw_tc=0a18ab6c17833326692832986e66ad88590a1857ddae18de8424446dd7c7f2; t=95DEC25319FA21258C369646734311BF'
HEADERS = {'accept':'application/json','content-type':'application/json','origin':'https://www.nowcoder.com','referer':'https://www.nowcoder.com/','user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36','x-requested-with':'XMLHttpRequest','Cookie':COOKIE}

# 获取标签统计
r = requests.get('https://gw-c.nowcoder.com/api/sparta/intelligent/getPCIntelligentList?questionJobId=10',
                 headers=HEADERS, impersonate='chrome124', timeout=15)
data = r.json()['data']
for tg in data.get('tags', []):
    for item in tg.get('items', []):
        if item['id'] in (570, 3935, 21048):
            print(f'{item["title"]:10} id={item["id"]:8} 总数={item["tcount"]:5} 已做={item["rcount"]:5} 剩余={item["leftCount"]:5}')

# 检查已爬数据
for tag_file in ['570_Java', '3935_Spring', '21048_Redis']:
    path = f'D:/Workspace/Project/cs-interview/nowcoder_data/{tag_file}.json'
    with open(path, 'r', encoding='utf-8') as f:
        qs = json.load(f)
    member = sum(1 for q in qs if q.get('isMember'))
    no_an = sum(1 for q in qs if not q.get('analysis'))
    print(f'  → 已爬 {len(qs)} 题, 会员题={member}, 无解析={no_an}')
