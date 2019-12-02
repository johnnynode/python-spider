'''
错误处理: 在容易出错的位置，添加 try 块
'''

from urllib import request, error

url = 'https://avatar.csdn.net/x/y/sdsds.jpg'
req = request.Request(url)
try:
    res = request.urlopen(req)
    html = res.read().decode('utf-8') # 此处二进制内容转换为utf8的内容
    print(len(html))
# HTTPError 要在 URLError 之后
except error.HTTPError as e:
    print('HTTPError')
    print(e.reason)
    print(e.code)
except error.URLError as e:
    print('URLError')
    print(e.reason)