# -*- coding: utf-8 -*-

import scrapy
from scrapy.linkextractor import LinkExtractor
from .. items import LinkdemoItem

class LinktestSpider(scrapy.Spider):
    name = 'linktest'
    allowed_domains = ['www.gaosiedu.com']
    start_urls = ['http://www.gaosiedu.com/gsschool/']


    def parse(self, response):
        link = LinkExtractor(restrict_xpaths="//ul[@class='cont_xiaoqu']//li")
        links = link.extract_links(response)
        for link_line in links:
            print(link_line.url,link_line.text)
            item = LinkdemoItem()
            item["url"] = link_line.url
            item["text"] = link_line.text
            yield item