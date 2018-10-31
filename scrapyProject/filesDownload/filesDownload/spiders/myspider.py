# -*- coding: utf-8 -*-
import scrapy
from ..items import FilesdownloadItem

class MyspiderSpider(scrapy.Spider):
    name = 'myspider'
    allowed_domains = ['matplotlib.org']
    start_urls = ['https://matplotlib.org/examples/index.html']

    def parse(self, response):
        url_parts = response.css("li.toctree-l2 a::attr(href)").extract()
        for u in url_parts:
            url = response.urljoin(u)
            #print(url)
            yield scrapy.Request(url=url, callback=self.parse_file)

    def parse_file(self, response):
        file_item = FilesdownloadItem()
        url_part = response.css("a.reference.external::attr(href)").extract_first()
        file_item['file_urls'] = [response.urljoin(url_part)]
        #print(file_item['files_urls'])
        return file_item
