import requests
import json

def fanyi(kw):
    url = 'https://fanyi.baidu.com/sug';
    data = {'kw': kw}
    # 设置header头信息 头信息可以不加
    headers = {
        'Content-Length': len(data),
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36',
        'Content-Type': "application/x-www-form-urlencoded; charset=UTF-8"
    }
    # 发送请求，爬取信息
    res = requests.post(url, data = data)
    # 解析结果
    str_json = res.content.decode('utf-8')
    # print(str_json)
    myjson = json.loads(str_json)
    print(myjson['data'][0]['v']) # n. 蟒; 蚺蛇;

if __name__ == '__main__':
    while True:
        kw = input('请输入要翻译的词：')
        if kw == 'q':
            break
        fanyi(kw)