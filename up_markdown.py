import requests
import os
# 文件夹名称
markdown_folder = "WRa5-0481-0500"
folder_path = os.path.join(os.getcwd(), markdown_folder)
if not os.path.exists(folder_path):
    print(f"文件夹不存在: {folder_path}")
    exit()
for filename in os.listdir(folder_path):
    if not filename.endswith('.md'):
        continue
    file_path = os.path.join(folder_path, filename)

    url = "http://49.232.231.203:9102/api/v1/tkxtgczyb"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/142.0.0.0 Safari/537.36 Edg/142.0.0.0",
        'origin': 'http://49.232.231.203:9008',
        'referer': 'http://49.232.231.203:9008/',
        'accept': 'application/json, text/plain, */*',
        'accept-encoding': 'gzip, deflate',
        'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
        # 这里的authorization需要替换成自己的,可以在浏览器开发者工具中找到,可能会更新
        'authorization': 'bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJhZG1pbjAwNCIsImV4cCI6MTc2Mzk1ODQyMn0.1FlZq0ugS4-14okE_dpZccDpqyntc4cBpvUOUrjPsq4',
    }
    with open(file_path, 'r', encoding='utf-8') as f:
        neirong = f.read()
    data = {
        # 创建人zzz
        'cjr': "zzz",
        # 创建时间
        'cjsj': "2025-11-23",
        # 工程id
        'gcid': "a9fd810a-a244-420e-85a7-7d8a011b4dbd",
        'nrlx': "markdown",
        'sfkfw': "是",
        'zymc': filename[:-3],
        'cjmb': "",
        'nr': neirong,
        'jmzfc': "xxx",
        'wjlink': "",
        'wjlj': "",
    }
    response = requests.post(url, headers=headers, json=data)
    if response.status_code == 200:
        print(f'{filename[:-3]}上传成功')

