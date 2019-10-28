# -*- coding: utf-8 -*-
import scrapy
from educsdn.items import CoursesItem

class CoursesSpider(scrapy.Spider):
    name = 'courses'
    allowed_domains = ['edu.csdn.net']
    start_urls = ['https://edu.csdn.net/courses/o5329/p1']
    p = 1

    def parse(self, response):
        ''' 解析数据信息 '''
        print(response.url)
        dlist = response.selector.css('div.course_item')
        for dd in dlist:
            # print(dd.css('span.title::text').extract_first())
            item = CoursesItem()
            item['title'] = dd.css("span.title::text").extract_first()
            ''' '''
            # 后期再对数据格式进行处理
            if item['title']:
                item['title'] = item['title'].strip()
            
            item['url'] = dd.css("a::attr(href)").extract_first()
            item['pic'] = dd.css("img::attr(src)").extract_first()
            item['teacher'] = dd.css("span.lecname::text").extract_first()
            item['time'] = dd.re_first('<span class="course_lessons">(.*?)课时</span>')
            item['price'] = dd.re_first("￥([0-9\.]+)")
            #print(item)
            #print('=' * 50)
            yield item # 此处的数据会被送到pipelines中去

        self.p += 1
        # 此处只爬取2页
        if self.p < 2:
            next_url = 'https://edu.csdn.net/courses/o5329/p' + str(self.p)
            url = response.urljoin(next_url)
            yield scrapy.Request(url = url, callback = self.parse)
