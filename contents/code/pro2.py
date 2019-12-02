'''
1. 模拟登陆人人网
2. 登陆成功后跳转到个人首页并获取数据
'''

# 模拟人人网登陆操作
from urllib import request, parse
import gzip
import re

# 示例：req_url = "http://www.renren.com/11111111"
req_url = "http://www.renren.com/your-id"

# 经过浏览器xhr请求分析，因为不确定具体要提交哪些参数，以下是全部参数信息
headers = {
    'Host': 'www.renren.com',
    'Connection': 'keep-alive',
    'Upgrade-Insecure-Requests': 1,
    'DNT': 1,
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.70 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
    'Referer': 'http://www.renren.com/SysHome.do',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
    'Cookie': 'anonymid=k2jogzmy45d6g1; depovince=GW; _r01_=1; JSESSIONID=abcTX9kPXDXiC-MXhZT4w; ick_login=eda6bae3-1016-4b43-8653-c0b0e88bf6c1; ick=ef6c24f7-ccc8-4110-8c8d-e60fa7783869; XNESSESSIONID=367a0c8b5c12; Hm_lvt_668f5751b331d2a1eec31f2dc0253443=1567945461; first_login_flag=1; ln_uact=15311111111; ln_hurl=http://head.xiaonei.com/photos/0/0/men_main.gif; wp_fold=0; jebecookies=34444812-0d3f-48b3-b7ca-01ae41fcf755|||||; Hm_lpvt_668f5751b331d2a1eec31f2dc0253443=1567947038; _de=57D139C64A11F200F1AEE8096E718C50; p=3e26031d8967cf591201ca56c7a2147d7; t=41388b62070609b8ad5462bac60219cd7; societyguester=41388b62070609b8ad5462bac60219cd7; id=772777777; xnsid=cc1b3f4c; loginfrom=syshome'
}

req = request.Request(req_url, headers=headers)
res = request.urlopen(req)
html = gzip.decompress(res.read()).decode('utf-8') # 因为请求头上支持gzip传输，此处在响应的时候要通过gzip来解压缩

#print(html)
print(re.findall(("<title>(.*?)</title>"), html)) # ['人人网 - 你的名字'] 此处会输出如下信息