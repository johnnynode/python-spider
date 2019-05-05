import urllib3
import re

url = 'http://www.baidu.com' # 必须有协议名，完整路径

http = urllib3.PoolManager() # 实例化产生请求对象

res = http.request('GET', url)

print('status: %d' % res.status) # status: 200

data = res.data.decode("utf-8")

print(re.findall("<title>(.*?)</title>", data)) # ['百度一下，你就知道']