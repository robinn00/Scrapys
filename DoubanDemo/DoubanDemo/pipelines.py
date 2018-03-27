# -*- coding: utf-8 -*-

# Define your item pipelines here
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import json
from scrapy.exceptions import DropItem

class DoubandemotojsonPipeline(object):
    def __init__(self):
        self.file = open("db.jl","wb")

    def process_item(self, item, spider):
        line = json.dumps(dict(item))+"\n"
        self.file.write(line)
        return item


class DoubandemotonullPipeline(object):
    def process_item(self, item, spider):
        if item["content"]:
            return item
        else:
            raise DropItem("Duplicate item found: %s" % item)