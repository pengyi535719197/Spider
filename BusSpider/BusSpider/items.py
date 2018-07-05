# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class BusspiderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()



    province = scrapy.Field()
    city = scrapy.Field()
    city_url = scrapy.Field()
    more_line_url = scrapy.Field()
    bus_line_url = scrapy.Field()
    bus_line = scrapy.Field()
    bus_start_station = scrapy.Field()
    bus_end_station = scrapy.Field()
    bus_stationNames = scrapy.Field()

class xicispiderItem(scrapy.Item):
    ip = scrapy.Field()
    port = scrapy.Field()
