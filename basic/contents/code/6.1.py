'''
错误处理: 在容易出错的位置，添加 try 块
'''

from urllib import request, error

url = 'https://avatar.csdn.net/x/y/sdsds.jpg'
req = request.Request(url)
try:
    res = request.urlopen(req)
    html = res.read().decode('utf-8')
    print(len(html))
# HTTPError 要在 URLError 之后
except error.HTTPError as e:
    print(2)
    print(e.reason)
    print(e.code)
except error.URLError as e:
    print(1)
    print(e.reason)