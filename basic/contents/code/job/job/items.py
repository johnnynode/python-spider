# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class JobItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass

class CareersItem(scrapy.Item):
    '''
       人事招聘信息封装类
       （职位id号，名称、位置、类别、要求、职责和要求）
    '''
    table = "careers"  #表名
    id = scrapy.Field() 
    name = scrapy.Field()
    location = scrapy.Field()
    cate = scrapy.Field()
    duty = scrapy.Field()
    requirement = scrapy.Field()
