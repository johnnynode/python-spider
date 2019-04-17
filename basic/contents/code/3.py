import re

f = open('./3.html', 'r', encoding="utf-8")
content = f.read()
f.close()

list = re.findall("<a href=\"(.*?)\">(.*?)</a>", content)

for i in list:
    print(i)

# 循环输出结果
'''
('http://1', '1')
('http://2', '2')
('http://3', '3')
('http://4', '4')
'''