# -*- coding: utf-8 -*-
import scrapy
from ..items import FirsttestItem

class MyspiderSpider(scrapy.Spider):
    name = 'myspider'
    allowed_domains = ['baidu.com']
    start_urls = ['http://www.baidu.com/']

    def parse(self, response):
        test_item = FirsttestItem()
        #test_item['name']=response.status
        #test_item['name'] = response.encoding
        #response.encoding = 'gbk'
        test_item['name'] = response.text
        return test_item