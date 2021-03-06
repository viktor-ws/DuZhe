# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import codecs
import json


class DuzhePipeline(object):
    def __init__(self):
        self.file = codecs.open('chinese.json', 'w', encoding='utf-8')
        self.file.write('[')

    def process_item(self, item, spider):
        line = json.dumps(dict(item), ensure_ascii=False) + ",\n\n"
        self.file.write(line)
        return item

    def close_spider(self, spider):
        position = self.file.tell()
        self.file.write(']')
        self.file.close()
