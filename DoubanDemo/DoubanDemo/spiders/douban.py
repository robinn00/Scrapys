# -*- coding: utf-8 -*-

import scrapy
from scrapy import log
from .. items import DoubandemoItem

class DoubanSpider(scrapy.Spider):
    name = 'douban'
    allowed_domains = ['movie.douban.com']
    start_urls = ['https://movie.douban.com/review/best/']

    def parse(self, response):
        import sys
        reload(sys)
        sys.setdefaultencoding("utf-8")
        for sel in response.xpath("//div[@class='main-bd']"):
            title = sel.xpath("h2/a/text()").extract()
            content = sel.xpath("div[@class='review-short']//div[@class='short-content']//text()").extract()

            dbitem = DoubandemoItem()
            dbitem["title"] = title[0].strip()
            dbitem["content"] = content[0].strip()
            yield  dbitem