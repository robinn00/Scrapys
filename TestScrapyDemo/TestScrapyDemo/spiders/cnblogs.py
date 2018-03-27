# -*- coding: utf-8 -*-
import scrapy


class CnblogsSpider(scrapy.Spider):
    name = 'cnblogs'
    allowed_domains = ['https://www.cnblogs.com/']
    start_urls = ['http://https://www.cnblogs.com//']

    def parse(self, response):
        pass
