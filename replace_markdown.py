import requests
# 创建人
cjr = 'zzz'
# 工程id
gcid = 'a9fd810a-a244-420e-85a7-7d8a011b4dbd'
# 旧内容
old_tihuan = '王烈教授'
# 新内容
new_tihuan = '医生'


login_url = 'http://49.232.231.203:9102/api/v1/login'
login_headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/142.0.0.0 Safari/537.36 Edg/142.0.0.0",
    'origin': 'http://49.232.231.203:9008',
    'referer': 'http://49.232.231.203:9008/'
}
login_data = {
    "username": "admin004",
    "password": "admin004"
}
res = requests.post(login_url, headers=login_headers, data=login_data)
print("Login successful!")
data = res.json()
token = data['data']['token']
url = f'http://49.232.231.203:9102/api/v1/tkxtgczyb/page?pageNum=1&pageSize=300&zymc=&cjr={cjr}&startDate=&endDate=&nrlx=markdown&gcid={gcid}'
request_headers = {
    "Accept": "application/json, text/plain, */*",
    "Accept-Encoding": "gzip, deflate",
    "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
    "Authorization": token,
    "Connection": "keep-alive",
    "Host": "49.232.231.203:9102",
    "Origin": "http://49.232.231.203:9008",
    "Referer": "http://49.232.231.203:9008/",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/142.0.0.0 Safari/537.36 Edg/142.0.0.0"
}
# 3. 发送请求
response = requests.get(url, headers=request_headers)
print(f"状态码: {response.status_code}")

res_json = response.json()
total = res_json['data']['total']

for i in range(total):
    zymc = res_json['data']['data'][i]['zymc']
    zyid = res_json['data']['data'][i]['zyid']
    cjsj = res_json['data']['data'][i]['cjsj']
    # 获得内容
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/142.0.0.0 Safari/537.36 Edg/142.0.0.0",
        'referer': 'http://49.232.231.203:9102/'
    }
    get_markdown_url = f'http://49.232.231.203:9102/api/v1/markdow/{zyid}'
    response = requests.get(get_markdown_url, headers=headers).json()
    # 替换内容
    new_neirong = response['data'].replace(f'{old_tihuan}', f'{new_tihuan}')
    # 上传内容
    response_json = {
          "cjmb": "",
          "cjr": cjr,
          "cjsj": cjsj,
          "gcid": gcid,
          "jmzfc": "xxx",
          "nr": new_neirong,
          "nrlx": "markdown",
          "sfkfw": "是",
          "wjlink": "",
          "wjlj": "",
          "zymc": zymc
    }
    get_url = f'http://49.232.231.203:9102/api/v1/tkxtgczyb/{zyid}'
    get_res = requests.put(get_url, headers=request_headers,json=response_json)
    print(get_res.status_code)
    print(f'{zymc}修改成功')


