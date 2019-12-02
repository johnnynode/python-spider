# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy

class CoursesItem(scrapy.Item):
    '''
    课程信息item类
    '''
    # define the fields for your item here like:
    # 课程标题、课程地址、图片、授课老师，视频时长、价格
    title = scrapy.Field()
    url = scrapy.Field()
    pic = scrapy.Field()
    teacher = scrapy.Field()
    time = scrapy.Field()
    price = scrapy.Field()
    
    def parse(self, response):
        pass