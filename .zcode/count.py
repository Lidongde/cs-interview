import json, os
data_dir = r'D:/Workspace/Project/cs-interview/nowcoder_data'
for f in sorted(os.listdir(data_dir)):
    if f.endswith('.json') and f != 'index.json':
        path = os.path.join(data_dir, f)
        try:
            d = json.load(open(path, encoding='utf-8'))
            print(f'{f}: {len(d)} 题 ({os.path.getsize(path)//1024} KB)')
        except:
            print(f'{f}: 读取失败')
