# -*- coding: utf-8 -*-
import scrapy, time, json
from job.items import CareersItem

class CareersSpider(scrapy.Spider):
    name = 'careers'
    allowed_domains = ['careers.tencent.com']
    pageSize = 10
    p = 1 # 当前页数
    start_urls = ['https://careers.tencent.com/tencentcareer/api/post/Query?keyword=AI&language=zh-cn&area=cn&pageSize='+ str(pageSize) +'&pageIndex=1&timestamp=' + str(int(round(time.time() * 1000)))]

    def parse(self, response):
        #解析当前招聘列表信息的url地址：
        # print('=' * 60)
        obj = json.loads(response.text)
        if obj['Code'] != 200:
            print('list error occur: ' + response.text)
            return
        data = obj['Data']
        count = data['Count'] # 总数
        posts = data['Posts'] # 当前数据
        # print(posts)
        # 开始批量请求【详情页】接口
        for ps in posts:
            pid = ps.get('PostId')
            if pid:
                detail_url = 'https://careers.tencent.com/tencentcareer/api/post/ByPostId?language=zh-cn&timestamp=' + str(int(round(time.time() * 1000))) + '&postId=' + pid
                url = response.urljoin(detail_url)
                yield scrapy.Request(url = url, callback = self.parseNext)


        self.p += 1 # 自增处理
        # 例：如果有32条，每页有10条，那么最多爬取4次
        # 爬取完所有的数据 向上取整 进行比较，符合条件请求下一个列表页的数据
        if -(-count // self.pageSize) >= self.p:
            next_url = 'https://careers.tencent.com/tencentcareer/api/post/Query?keyword=AI&language=zh-cn&area=cn&pageSize='+ str(self.pageSize) +'&pageIndex='+ str(self.p) +'&timestamp=' + str(int(round(time.time() * 1000)))
            url = response.urljoin(next_url)
            yield scrapy.Request(url = url, callback = self.parse)
   
    def parseNext(self, response):
        obj = json.loads(response.text)
        if obj['Code'] != 200:
            print('detail error occur: ' + response.text)
            return
        data = obj['Data']
        item = CareersItem()
        item["name"] = data['RecruitPostName']
        item["location"] = data['LocationName']
        item["cate"] = data['CategoryName']
        item["duty"] = data['Responsibility']
        item["requirement"] = data['Requirement']
        yield item
