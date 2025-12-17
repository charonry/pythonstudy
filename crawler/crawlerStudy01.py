"""
# 自带库
from urllib.request import urlopen

url = "https://www.baidu.com"
resp = urlopen(url)

file_path = "../resource/html/baidu.html"
with open(file_path, 'w', encoding="utf-8") as f:
    f.write(resp.read().decode("utf-8"))
"""

"""
# requests库
import requests
import json

# get请求
# url = "https://www.sogou.com/web?query=桥本奈奈未"
# header = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/142.0.0.0 " \
#          "Safari/537.36 "
# headers = {
#     'User-Agent': header
# }
# resp = requests.get(url, headers=headers)
# print(resp.text)
# resp.close()

# post请求
# url = "https://fanyi.baidu.com/sug"
# data = {
#     "kw": "dog"
# }
# resp = requests.post(url, data=data)
# print(json.dumps(resp.json(), ensure_ascii=False, indent=4))

url = "https://movie.douban.com/j/chart/top_list"
params = {
    "type": 24,
    "interval_id": "100:90",
    "action": "",
    "start": 0,
    "limit": 20
}
headers = {
    'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/142.0.0.0 "
                  "Safari/537.36 ",
    'Connection': 'close'
}
resp = requests.get(url, headers=headers, params=params)
print(resp.json())
"""

"""
# 豆瓣电影
import requests
import re
import csv

url = "https://movie.douban.com/top250"
headers = {
    'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/142.0.0.0 "
                  "Safari/537.36",
    'Connection': 'close'
}
obj = re.compile(r'<li>.*?<div class="info">.*?'
                 r'<span class="title">(?P<title>.*?)</span>.*?'
                 r'<br>(?P<year>.*?)&nbsp;.*?'
                 r'<span class="rating_num" property="v:average">(?P<score>.*?)</span>.*?'
                 r'<span property="v:best" content="10.0"></span>.*?<span>(?P<num>.*?)</span>.*?/li>', re.S)
get_num = re.compile(r'\d+', re.S)
file_path = "../resource/wps/doubanTop250.csv"
my_list = []
for i in range(10):
    start = 25 * i
    params = {
        "start": start,
        "filter": ""
    }
    resp = requests.get(url, headers=headers, params=params)
    page_content = resp.text
    result = obj.finditer(page_content)
    for it in result:
        movie_dict = it.groupdict()
        title = movie_dict.get("title")
        year = movie_dict.get("year").strip()
        score = movie_dict.get("score")
        num_match = get_num.search(movie_dict.get("num"))
        num = num_match.group() if num_match else "0"
        my_list.append([title, year, score, num])
with open(file_path, 'w', encoding='utf-8', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['标题', '年份', '评分', '评价人数'])
    writer.writerows(my_list)
print("over！")
"""

# 电影天堂电影
import requests
import re
import csv

url = "https://www.dytt8899.com/"
headers = {
    'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/142.0.0.0 "
                  "Safari/537.36",
    'Connection': 'close'
}
resp = requests.get(url, verify=False, headers=headers)
resp.encoding = "gb2312"
# 获取源码
ul_obj = re.compile(r"2025必看热片.*?<ul>(?P<movieUl>.*?)</ul>", re.S)
ul_result = ul_obj.search(resp.text)
# 提取内容
movieUl = ul_result.group("movieUl")
li_obj = re.compile(r"<li><a href='(?P<movieUrl>.*?)'.*?>(?P<movieName>.*?)</a>.*?</li>", re.S)
li_result = li_obj.finditer(movieUl)
movies = []
movie_obj = re.compile(r'◎片　　名(?P<movieInName>.*?)<br />.*?'
                       r'bgcolor="#fdfddf"><a href="(?P<download>.*?)">', re.S)
for it in li_result:
    movie_dict = it.groupdict()
    movie_dict["movieDetailUrl"] = url + it.group("movieUrl").strip("/")
    movies.append(movie_dict)
for it in movies:
    movieDetailUrl = it.get("movieDetailUrl")
    resp_detail_movie = requests.get(movieDetailUrl, verify=False, headers=headers)
    resp_detail_movie.encoding = "gb2312"
    context = resp_detail_movie.text
    result_detail_movie = movie_obj.search(context)
    it["movieInName"] = result_detail_movie.group("movieInName").strip()
    it["download"] = result_detail_movie.group("download")
file_path = "./resource/wps/dianyingtiantang.csv"
with open(file_path, 'w', encoding='utf-8', newline='') as f:
    writer = csv.DictWriter(f, ['movieUrl', 'movieName', 'movieDetailUrl', 'movieInName', 'download'])
    writer.writerows(movies)
print("over！")






