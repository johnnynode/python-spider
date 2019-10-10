# -*- coding: utf-8 -*-
import scrapy
from sp_pro1.items import FangItem

class FangSpider(scrapy.Spider):
    name = 'fang' # 爬虫的唯一标识
    allowed_domains = ['fang.5i5j.com'] # 爬虫的允许域名
    start_urls = ['https://fang.5i5j.com/bj/loupan/']

    def parse(self, response):
        # print(response.status)
        print('*' * 70)
        hlist = response.css("li.houst_ctn")
        for vo in hlist:
            item = FangItem()
            item['title'] =  vo.css("span.house_name::text").extract_first()
            #item['address'] =  vo.css("span.addressName::text").extract_first()
            #item['time'] =  vo.re("<span>(.*?)开盘</span>")[0]
            #item['clicks'] =  vo.re("<span><i>([0-9]+)</i>浏览</span>")[0]
            #item['price'] =  vo.css("i.fontS24::text").extract_first()
            print(item)
            # yield item
        print('over ' + '>' * 60)
