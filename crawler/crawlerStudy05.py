"""
# 多线程
from threading import Thread


class MyThread(Thread):
    def __init__(self, name):
        super().__init__()
        self.name = name

    def run(self):
        for i in range(100):
            print(f"{self.name}：{i}")


if __name__ == "__main__":
    t = MyThread("abc")
    t.start()
    for i in range(100):
        print(f"主线程：{i}")
"""

"""
from concurrent.futures import ThreadPoolExecutor,ProcessPoolExecutor

def func(name):
    for i in range(1000):
        print(name, i)

if __name__ == "__main__":
    with ThreadPoolExecutor(50) as t:
        for i in range(100):
            t.submit(func, f"线程{i}")
    print("over")
"""

from concurrent.futures import ThreadPoolExecutor
from bs4 import BeautifulSoup
import requests
import re


def download_one_page(nowPageNo, lastPageNo):
    url = f"http://www.shucai123.com/price/t{nowPageNo}"
    headers = {
        'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/142.0.0.0 "
                      "Safari/537.36",
        "Referer": f"http://www.shucai123.com/price/t{lastPageNo}",
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
    return vegetable_list


if __name__ == '__main__':
    all_vegetable_data = []
    with ThreadPoolExecutor(5) as t:
        future_list = []
        for i in range(3, 11):
            future = t.submit(download_one_page, i, i - 1)
            future_list.append(future)
        for future in future_list:
            # result()方法会阻塞，直到该线程执行完成并返回结果
            page_data = future.result()
            all_vegetable_data.extend(page_data)
    print(f"总共爬取到{len(all_vegetable_data)}条蔬菜价格数据")
    for item in all_vegetable_data:
        print(item)
