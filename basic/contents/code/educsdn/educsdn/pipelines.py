# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

import pymysql
from scrapy.exceptions import DropItem
from scrapy.pipelines.images import ImagesPipeline
from scrapy import Request

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

class ImagePipeline(ImagesPipeline):
    '''自定义图片存储类'''

    def get_media_requests(self, item, info):
        '''通过抓取的item对象获取图片信息，并创建Request请求对象添加调度队列，等待调度执行下载'''
        yield Request(item['pic'])

    def file_path(self,request,response=None,info=None):
        '''返回图片下载后保存的名称，没有此方法Scrapy则自动给一个唯一值作为图片名称'''
        url = request.url
        file_name = url.split("/")[-1]
        return file_name

    def item_completed(self, results, item, info):
        ''' 下载完成后的处理方法，其中results内容结构如下说明'''
        image_paths = [x['path'] for ok, x in results if ok]
        if not image_paths:
            raise DropItem("Item contains no images")
        #item['image_paths'] = image_paths
        return item

