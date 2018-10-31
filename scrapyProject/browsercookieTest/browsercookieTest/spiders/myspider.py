# -*- coding: utf-8 -*-
import scrapy


class MyspiderSpider(scrapy.Spider):
    name = 'myspider'
    allowed_domains = ['zhihu.com']
    start_urls = ['https://www.zhihu.com/people/edit']

    def start_requests(self):
        yield scrapy.Request(url=self.start_urls[0], meta={'cookiejar': 'chrome'}, callback=self.parse)

    def parse(self, response):
        #print(response.text)
        print(response.encoding)
        print(response.status)
        #name = response.css('span.FullnameField-name::text').extract_first()
        #print(response.text)
        name = response.xpath('//span[@class="FullnameField-name"]/text()').extract_first()
        print(name)
