import requests
import re, json

# header头信息
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:43.0) Gecko/20100101 Firefox/43.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language': 'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3',
    'Accept-Encoding': 'gzip, deflate',
    'Referer': 'https://item.jd.com/100005171461.html',
    'Connection': 'keep-alive',
    'Cache-Control': 'max-age=0',
}

#请求url地址, 此处实际上是一个jsonp请求
url = "https://club.jd.com/comment/productPageComments.action?callback=fetchJSON_comment98vv1950&productId=100005171461&score=0&sortType=5&page=0&pageSize=10&isShadowSku=0&fold=1"

# 提交请求爬取信息
response = requests.get(url,headers=headers)
txt = response.text

start = txt.find('(') + 1
end = txt.rfind(");")

jsonstr = txt[start:end]
data_json = json.loads(jsonstr)
comments = data_json.get('comments')

for c in comments:
    print(c.get('content'))
    print("="*80)