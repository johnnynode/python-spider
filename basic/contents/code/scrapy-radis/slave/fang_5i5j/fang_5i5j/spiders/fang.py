# -*- coding: utf-8 -*-
import scrapy
from fang_5i5j.items import FangItem
from scrapy_redis.spiders import RedisSpider

class FangSpider(RedisSpider):
    name = 'fang'
    #allowed_domains = ['fang.5i5j.com']
    #start_urls = ['https://fang.5i5j.com/bj/loupan/']
    redis_key = 'fangspider:start_urls'

    def __init__(self, *args, **kwargs):
        # Dynamically define the allowed domains list.
        domain = kwargs.pop('domain', '')
        self.allowed_domains = filter(None, domain.split(','))
        super(FangSpider, self).__init__(*args, **kwargs)

    def parse(self, response):
        #print(response.status)
        hlist = response.css("li.houst_ctn")
        for vo in hlist:
            item = FangItem()
            item['title'] =  vo.css("span.house_name::text").extract_first()
            # print(item)
            yield item
        #pass
