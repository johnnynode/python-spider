from urllib import request, parse
import json # 用于处理json数据的库
import ssl

context = ssl._create_unverified_context() # 使用ssl创建未经验证的上下文

url = 'https://fanyi.baidu.com/sug';
data = {'kw':'python'}
data = parse.urlencode(data) # 对请求数据进行编码

# 设置header头信息
headers = {
    'Content-Length': len(data),
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36',
    'Content-Type': "application/x-www-form-urlencoded; charset=UTF-8"
}

# 发送请求，爬取信息，使用 bytes函数将数据转换成二进制
req = request.Request(url, data=bytes(data, encoding="utf-8"), headers=headers)
res = request.urlopen(req, context=context)

# 解析结果
str_json = res.read().decode('utf-8') # 此处是字符串

# print(str_json)

myjson = json.loads(str_json) # 通过loads函数转换成字典
print(myjson['data'][0]['v']) # n. 蟒; 蚺蛇;
