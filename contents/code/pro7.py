from requests.exceptions import RequestException
from pyquery import PyQuery as pq
import requests
import time,json

def getPage(url):
    '''爬取指定url页面信息'''
    try:
        #定义请求头信息
        headers = {
            'User-Agent':'User-Agent:Mozilla/5.0(WindowsNT6.1;rv:2.0.1)Gecko/20100101Firefox/4.0.1'
        }
        # 执行爬取
        res = requests.get(url,headers=headers)
        #判断响应状态,并响应爬取内容
        if res.status_code == 200:
            return res.text
        else:
            return None
    except RequestException:
        return None

def parsePage(content):
    '''解析爬取网页中的内容，并返回字段结果'''
    # print(content)
    # =========使用pyquery解析==================
    # 解析HTML文档
    doc = pq(content)
    #获取网页中所有标签并遍历输出标签名
    items = doc("div.item")
    #遍历封装数据并返回
    for item in items.items():
        yield {
            'index':item.find("div.pic em").text(),
            'image':item.find("div.pic img").attr('src'),
            'title':item.find("div.hd span.title").text(),
            'actor':item.find("div.bd p:eq(0)").text(),
            'score':item.find("div.bd div.star span.rating_num").text(),
        }

def writeFile(content):
    '''执行文件追加写操作'''
    #print(content)
    with open("./result.txt",'a',encoding='utf-8') as f:
        f.write(json.dumps(content,ensure_ascii=False) + "\n")
        #json.dumps 序列化时对中文默认使用的ascii编码.想输出真正的中文需要指定ensure_ascii=False

def main(offset):
    ''' 主程序函数，负责调度执行爬虫处理 '''
    url = 'https://movie.douban.com/top250?start=' + str(offset)
    #print(url)
    html = getPage(url)
    #判断是否爬取到数据，并调用解析函数
    if html:
        for item in parsePage(html):
            writeFile(item)

# 判断当前执行是否为主程序运行，并遍历调用主函数爬取数据
if __name__ == '__main__':
    for i in range(10):
        main(offset=i*25)
        time.sleep(1)