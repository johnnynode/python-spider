'''
错误处理: 在容易出错的位置，添加 try 块  程序 优化
'''

from urllib import request, error

url = 'https://avatar.csdn.net/x/y/sdsds.jpg'
req = request.Request(url)
try:
    res = request.urlopen(req)
    html = res.read().decode('utf-8')
    print(len(html))
# HTTPError 要在 URLError 之后
except Exception as e:
    if hasattr(e, "code"):
        print("HTTPError")
        print(e.reason)
        print(e.code)
    elif hasattr(e, "reason"):
        print("URLError")
        print(e.reason)