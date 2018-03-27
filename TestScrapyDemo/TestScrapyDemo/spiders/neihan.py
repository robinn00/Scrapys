# -*- coding: utf-8 -*-
import scrapy


class NeihanSpider(scrapy.Spider):
    name = 'neihan'
    allowed_domains = ['http://neihanshequ.com/']
    start_urls = ['http://http://neihanshequ.com//']

    def parse(self, response):
        pass
