# -*- coding: utf-8 -*-
import scrapy


class WenkuSpider(scrapy.Spider):
    name = 'wenku'
    allowed_domains = ['wenku.baidu.com']
    start_urls = ['https://wenku.baidu.com/search?word=python&pn=0','https://wenku.baidu.com/search?word=python&pn=10','https://wenku.baidu.com/search?word=python&pn=20']

    def parse(self, response):
        dllist = response.selector.xpath("//dl")
        #print(len(dllist))
        for dd in dllist:
            print(dd.xpath("./dt/p/a/@title").extract_first())

        print("="*70) #输出一条每个请求后分割线
