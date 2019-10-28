# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

import pymysql
from scrapy.exceptions import DropItem

class EducsdnPipeline(object):
    ''' 此处 '''
    def process_item(self, item, spider):
        # 处理数据
        if item['title']:
            item['title'] = item['title'].strip()
        # 用于判断是否丢弃
        dropFlag = (item['teacher'] == None) or (item['title'] == None) or (item['price'] == None) or (item['url'] == None) or (item['pic'] == None)
        if dropFlag:
            raise DropItem('this item is dropped!')
        else:
            return item

class MysqlPipeline(object):
    ''' 用于操作数据库的类 '''
    def __init__(self, host, user, password, database, port):
        self.host = host
        self.user = user
        self.password = password
        self.database = database
        self.port = port

    # 依赖注入
    @classmethod
    def from_crawler(cls, crawler):
        return cls(
            host = crawler.settings.get('MYSQL_HOST'),
            user = crawler.settings.get('MYSQL_USER'),
            password = crawler.settings.get('MYSQL_PASS'),
            database = crawler.settings.get('MYSQL_DATABASE'),
            port = crawler.settings.get('MYSQL_PORT'),
        )

    def open_spider(self, spider):
        ''' 连接数据库 '''
        self.db = pymysql.connect(self.host,self.user,self.password,self.database,charset='utf8',port=self.port)
        self.cursor = self.db.cursor()
    
    def process_item(self, item, spider):
        ''' 执行数据表的写入操作 '''
        sql = "insert into courses(title, url, pic, teacher, time, price) values('%s','%s','%s','%s','%s','%s')"%(item['title'],item['url'],item['pic'],item['teacher'],str(item['time']),str(item['price']))
        self.cursor.execute(sql)
        self.db.commit()
        return item
    
    def close_spider(self, spider):
        self.db.close()

