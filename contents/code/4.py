import urllib.request
import re

url = "http://www.baidu.com"
res = urllib.request.urlopen(url)
# print(res.read().decode("utf-8")) # 请求的结果是html代码
# print(len(res.read())) # 153682 注：此处输出网页字符的长度
html = res.read().decode("utf-8")

dlist = re.findall("<title>(.*?)</title>", html)
print(dlist) # ['百度一下，你就知道']