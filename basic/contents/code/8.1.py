#coding=utf-8

import requests
import re
import ssl

context = ssl._create_unverified_context() # 使用ssl创建未经验证的上下文
url = 'http://bj.58.com/job/'
data = {'key':'python', 'final':1, 'jump': 1}

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36'}

try:
    res = requests.get(url, headers=headers, params=data) # 封装请求对象
    html = res.content.decode("utf-8")
    print(len(html))
    pat = '<span class="address">(.*?)</span>  \| <span class="name">(.*?)</span>'
    dlist = re.findall(pat, html)
    for v in dlist:
        print(v[0] + ' : ' + v[1])

# HTTPError 要在 URLError 之后
except Exception as e:
    if hasattr(e, "code"):
        print("HTTPError")
        print(e.reason)
        print(e.code)
    elif hasattr(e, "reason"):
        print("URLError")
        print(e.reason)