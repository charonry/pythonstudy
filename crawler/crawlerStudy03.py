from lxml import etree
import requests

url = 'https://biizhi.com/'
headers = {
    'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/142.0.0.0 "
                  "Safari/537.36",
    'Connection': 'close'
}
resp = requests.get(url, verify=False, headers=headers)
html = etree.HTML(resp.text)
ul = html.xpath("/html/body/div[1]/div[1]/div/div/div[1]/div/ul")
my_list = []
for li in ul:
    context = li.xpath("./li/a/text()")
    href = li.xpath("./li/a/@href")
    my_dict = {"context": context, "href": href}
    my_list.append(my_dict)
print(my_list)
