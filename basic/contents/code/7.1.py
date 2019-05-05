import requests
import re

url = 'http://www.baidu.com' # 必须有协议名，完整路径

res = requests.get(url)

print('status: %d' % res.status_code) # status: 200

data = res.content.decode("utf-8")

print(re.findall("<title>(.*?)</title>", data)) # ['百度一下，你就知道']