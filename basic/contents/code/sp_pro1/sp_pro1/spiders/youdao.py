# -*- coding: utf-8 -*-
import scrapy,json

class YoudaoSpider(scrapy.Spider):
    name = 'youdao'
    allowed_domains = ['fanyi.youdao.com']
    start_urls = ['http://fanyi.youdao.com/']

    def start_requests(self):
        url = 'http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule'
        keyword = input("请输入要翻译的单词：")
        data = {'i':keyword,'doctype': 'json',}
        # FormRequest 是Scrapy发送POST请求的方法
        yield scrapy.FormRequest(
            url = url,
            formdata = data,
            callback = self.parse
        )

    def parse(self, response):
        res = json.loads(response.body)
        print(res['translateResult'][0][0]['tgt'])
