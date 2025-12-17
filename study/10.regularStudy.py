import re
# res1 = re.match('[he].', "ello")
# print(res1.group())
# res2 = re.match('[a-ef-z]', "ello")
# print(res2.group())
# res3 = re.match('[^he]', "llo")
# print(res3.group())

s = "<div class = 'jay1'><span id = '1'>abc1</span></div>" \
    "<div class = 'jay2'><span id = '2'>abc2</span></div>" \
    "<div class = 'jay3'><span id = '2'>abc3</span></div>" \
    "<div class = 'jay4'><span id = '4'>abc4</span></div>"
# re.S：让.能匹配到换行符
# (?P<分组名称>正则) 可以单独从正则匹配内容中提取具体分组内容
obj = re.compile(r"<div class = '(?P<class>.*?)'><span id = '(?P<id>\d)'>(?P<name>.*?)</span></div>", re.S)
result = obj.finditer(s)
for it in result:
    print(it.group(), it.group("name"))


