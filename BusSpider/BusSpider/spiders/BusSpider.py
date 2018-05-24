import scrapy
from BusSpider.items import BusspiderItem
from scrapy.http import Request


class BusSpider(scrapy.Spider):

    name = 'BusSpider'
    allowed_domains = ['8684.cn']
    start_urls = ['http://www.8684.cn/']

    def parse(self, response):
        city_list = response.xpath("/html/body/div[7]/div[4]/div[2]")
        print(city_list)
        for city in city_list:

            item = BusspiderItem()

            item['city'] = city.xpath("./a/text()").extract()[0]
            item['city_url'] = city.xpath("./a/@href").extract()[0]
            yield item