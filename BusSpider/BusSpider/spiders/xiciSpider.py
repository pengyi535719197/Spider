# -*- coding: utf-8 -*-
import scrapy
from BusSpider.items import xicispiderItem

class XicispiderSpider(scrapy.Spider):
    name = "xiciSpider"
    allowed_domains = ["xicidaili.com"]
    start_urls = ['http://www.xicidaili.com/']

    def parse(self, response):

        subSelector = response.xpath('//table[@id="ip_list"]/tr[@class="odd"]')
        for sub in subSelector:
            item = xicispiderItem()
            item['ip'] = sub.xpath("./td[2]/text()").extract()
            item['port'] = sub.xpath("./td[3]/text()").extract()
            yield item
