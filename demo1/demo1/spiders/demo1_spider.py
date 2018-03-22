#!/usr/bin/python
# _*_coding:utf-8 _*_
# author: robinn

import scrapy

class Demo1Spider(scrapy.Spider):
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
                cnt = sel.xpath("div[@class='entry_summary']/text()").extract()
                f.write(title[0].strip()+"\n")
                f.write(cnt[1].strip()+"\n")
                f.write("\n")
                print(title[0].strip())
                print(cnt[1].strip())