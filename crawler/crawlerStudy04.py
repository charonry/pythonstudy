"""
# session 未运行
import requests

url = 'https://biizhi.com/'
headers = {
    'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/142.0.0.0 "
                  "Safari/537.36",
    'Connection': 'close'
}
data = {
    "loginName": "abc",
    "password": "123456"
}
session = requests.session()
session.post(url, data=data, headers=headers)

in_url = "https://biizhi.com/"
resp = session.get(in_url, data=data, headers=headers)
print(resp.json())
"""

"""
# 防盗链
import requests

url = "https://www.pearvideo.com/video_1804104"
contId = url.split("_")[1]
video_url = "https://www.pearvideo.com/videoStatus.jsp"
headers = {
    'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/142.0.0.0 "
                  "Safari/537.36",
    # 防盗链
    "Referer": url,
    'Connection': 'close'
}
data = {
    "contId": contId,
    "mrd": "0.6459844842458055"
}
resp = requests.get(video_url, headers=headers, params=data)
system_time = resp.json().get('systemTime')
no_paly_url = resp.json().get('videoInfo').get('videos').get('srcUrl')
play_url = str.replace(no_paly_url, system_time, f"cont-{contId}")
video_name = play_url.split("/")[-1]
file_path = "./resource/video/" + video_name
video_resp = requests.get(play_url, verify=False)
with open(file_path, 'wb') as f:
    f.write(video_resp.content)
print("over")
"""

# 代理
import requests

proxie = {
    "https:": "https://39.104.79.145:1234",
    "http:": "http://39.104.79.145:1234"
}

url = "https://www.baidu.com"
headers = {
    'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/142.0.0.0 "
                  "Safari/537.36",
    'Connection': 'close'
}
resp = requests.get(url, headers=headers, proxies=proxie)
print(resp.text)
