import scrapy
from BusSpider.items import BusspiderItem
from scrapy.http import Request
import re


class BusSpider(scrapy.Spider):
    name = 'BusSpider'
    allowed_domains = ['bus.mapbar.com']
    start_urls = ['http://bus.mapbar.com/city/change/']

    def parse(self, response):
        city_list = response.xpath("/html/body/div/table[2]//tr//td/a")
        for city in city_list:
            item = BusspiderItem()
            item['city'] = city.xpath("./text()").extract()[0]
            item['city_url'] = city.xpath("./@href").extract()[0]
            item['more_line_url'] = item['city_url'] + "xianlu/"
            yield scrapy.Request(item['more_line_url'], meta={'item': item}, callback=self.bus_line_url)

    def bus_line_url(self, response):

        item = response.meta['item']
        bus_line_urls = response.css("dl.ChinaTxt > dd > a::attr(href)").extract()
        for bus_line_url in bus_line_urls:
            item['bus_line_url'] = bus_line_url
            yield scrapy.Request(item['bus_line_url'], meta={'item': item}, callback=self.bus_station)

        # item['more_line_url'] = response.xpath(
        #     "//div[@class='gray']/div[@class='w960 margin0auto']/div[@class='cityWrap']/div[@class='busno'][1]/ul/li[3]/a[@class='more']/@href").extract()

        # yield item


    def bus_station(self,response):
        item = response.meta['item']

        item['province'] = re.findall(r'province=(.*);city'
                                     , str(response.css("head > meta[name=location]::attr(content)").extract()[0]))[0]

        item['bus_line'] = str(response.css("head > title:nth-child(1)::text").extract()[0]).split("_")[0]
        item['bus_start_station'] = response.css("#startStation::attr(value)").extract()[0]
        item['bus_end_station'] = response.css("#endStation::attr(value)").extract()[0]
        item['bus_stationNames'] = response.css("#stationNames::attr(value)").extract()
        yield item

