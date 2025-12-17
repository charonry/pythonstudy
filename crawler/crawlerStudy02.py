"""
import requests
from bs4 import BeautifulSoup
import re

url = "http://www.shucai123.com/price/"
headers = {
    'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/142.0.0.0 "
                  "Safari/537.36",
    'Connection': 'close'
}
# 1.获取页面对象
resp = requests.get(url, verify=False, headers=headers)
# 2.BeautifulSoup解析处理，生成bs对象。
page = BeautifulSoup(resp.text, "html.parser")  # 指定html解析器
# 3.从bs中获取对象数据
tabel = page.find("table", attrs={"class": "bjtbl"})
trs = tabel.find_all("tr")[1:]
price_compile = re.compile(r'(?P<price>\d+\.?\d*)元/(?P<unit>斤|吨)', re.S)
vegetable_list = []
for tr in trs:
    vegetable_dict = {}
    tds = tr.find_all("td")
    type = tds[2].text
    price = price_compile.search(tds[3].text).group("price")
    unit = price_compile.search(tds[3].text).group("unit")
    vegetable_dict["type"] = type
    vegetable_dict["price"] = price
    vegetable_dict["unit"] = unit
    vegetable_list.append(vegetable_dict)
print(vegetable_list)
"""

import requests
from bs4 import BeautifulSoup
import time

url = 'https://biizhi.com/'
headers = {
    'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/142.0.0.0 "
                  "Safari/537.36",
    'Connection': 'close'
}
resp = requests.get(url, verify=False, headers=headers)
page = BeautifulSoup(resp.text, "html.parser")
pic_list = page.find_all("a", attrs={"class": "media-pic"})
par_file_path = "./resource/picture/"
for pic in pic_list:
    img_tag = pic.find('img')
    name = img_tag.get("alt")
    url = img_tag.get("src")
    img_resp = requests.get(url, verify=False, headers=headers)
    pic_split = url.rpartition('.')
    file_path = par_file_path + name + pic_split[1] + pic_split[2]
    with open(file_path, 'wb') as f:
        f.write(img_resp.content)
    time.sleep(0.5)
    print("over")
print("all over!")
