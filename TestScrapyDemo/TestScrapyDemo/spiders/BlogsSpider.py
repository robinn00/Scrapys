#!/usr/bin/python
# _*_coding:utf-8 _*_
# author: robinn

import scrapy
import logging
from .. items import TestscrapydemoItem


class BologsSpider(scrapy.Spider):
    name = "blogs"
    allowed_domains = ["cnblogs.com"]
    start_urls = [
        "https://news.cnblogs.com/"
    ]

    def parse(self, response):
        # filename = response.url.split("/")[-1]
        # with open(filename, 'wb') as f:
        #     f.write(response.body)
        import sys
        reload(sys)
        sys.setdefaultencoding('utf-8')
        with open("blogs.txt", "w") as f:
            for sel in response.xpath("//*[@id='news_list']/div[@class='news_block']/div[@class='content']"):
                title = sel.xpath("h2[@class='news_entry']/a/text()").extract()
                contents = sel.xpath("div[@class='entry_summary']/text()").extract()
                f.write(title[0].strip()+"\n")
                f.write(contents[1].strip()+"\n")
                f.write("\n")

                title = title[0].strip()
                contents = contents[1].strip()

                print(title)
                print(contents)
                item = TestscrapydemoItem()
                item["title"] = title
                item["contents"] = contents
                yield item

    # def close(spider, reason):
    #     print("closeing....")
    #
    # def log(self, message, level=logging.DEBUG, **kw):
    #     pass
    #
    # def start_requests(self):
    #     print("start_requests........")
    #
    # def make_requests_from_url(self, url):
    #     print(url)