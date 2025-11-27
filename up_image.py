import requests
import os


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

# 图片文件夹名称（与代码文件同级）
image_folder = "481-500"
folder_path = os.path.join(os.getcwd(), image_folder)
for filesname in os.listdir(folder_path):
    if filesname.lower().endswith(('.png', '.jpg')):
        file_path = os.path.join(image_folder, filesname)
        upload_url = 'http://49.232.231.203:9102/api/v1/uploadfile/'
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/142.0.0.0 Safari/537.36 Edg/142.0.0.0",
            "Referer": "http://49.232.231.203:9008/",
            "token":token
        }
        files = {
            "file": open(file_path, "rb")
        }
        upload_response = requests.post(upload_url,headers=headers,files=files)
        if upload_response.status_code == 200:
            upload_result = upload_response.json()
            if upload_result["code"] == 200:
                filename = upload_result["data"]["filename"]
                print(f"文件上传成功，filename: {filename}")
            else:
                print(f"文件上传失败：{upload_result['msg']}")
                exit()
        else:
            print(f"上传请求失败，状态码：{upload_response.status_code}")
            exit()
        files["file"].close()
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/142.0.0.0 Safari/537.36 Edg/142.0.0.0",
            'origin': 'http://49.232.231.203:9008',
            'referer': 'http://49.232.231.203:9008/',
            'accept': 'application/json, text/plain, */*',
            'accept-encoding': 'gzip, deflate',
            'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
            'authorization': token,
        }
        url = "http://49.232.231.203:9102/api/v1/tkxtgczyb"
        data = {
            # 创建人zzz
            'cjr': '梁桐源',
            # 创建时间
            'cjsj': "2025-11-25",
            # 工程id
            'gcid': "d8fbcbc1-ae14-44a7-93bb-6f9deab9f66e",
            'nrlx': "image",
            'sfkfw': "是",
            'zymc': f'{filesname[:-4]}',
            'cjmb': "",
            'nr': "xxx",
            'wjlink': filename,
            'jmzfc': "xxx",
            'wjlj': filename
        }
        response = requests.post(url, headers=headers, json=data)
        if response.status_code == 200:
            print(f'{filesname[:-4]}上传成功')