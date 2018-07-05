# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import time
import json
import codecs


class BusspiderPipeline(object):
    def process_item(self, item, spider):
        if spider.name == 'BusSpider':
            filename = 'buses.txt'
            with codecs.open(filename, 'a', encoding='utf8') as fp:
                line = json.dumps(dict(item), ensure_ascii=False) + '\n'
                fp.write(line)
        elif spider.name == 'xiciSpider':
            filename = 'ip.json'
            with codecs.open(filename, 'a', encoding='utf8') as fp:
                line = json.dumps(dict(item) , ensure_ascii=False) + '\n'
                fp.write(line)
        return item

# class xicispiderPipeline(object):
#     def process_item(self, item, spider):
#         filename = 'ip.json'
#         with codecs.open(filename, 'a', encoding='utf8') as fp:
#             line = json.dumps(dict(item) , ensure_ascii=False) + '\n'
#             fp.write(line)
#         return item