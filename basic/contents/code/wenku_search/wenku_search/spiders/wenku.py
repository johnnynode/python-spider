# -*- coding: utf-8 -*-
import scrapy


class WenkuSpider(scrapy.Spider):
    name = 'wenku'
    allowed_domains = ['wenku.baidu.com']
    start_urls = ['https://wenku.baidu.com/search?word=python&pn=0']

    def parse(self, response):
        print('=' * 50)
        print(response)
