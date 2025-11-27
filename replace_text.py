

import requests
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

url = "http://49.232.231.203:9102/api/v1/markdow/e8fde0cf-8f4f-4324-92b0-7d9eac875df9"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/142.0.0.0 Safari/537.36 Edg/142.0.0.0",
    'referer':'http://49.232.231.203:9102/'
}
response = requests.get(url,headers=headers).json()
print(response['data'])
print(type(response['data']))
# 替换内容

new_neirong = response['data'].replace('font-size: 1.8em', 'font-size: 2.4em')

print('以下是新内容')
print(new_neirong)
























