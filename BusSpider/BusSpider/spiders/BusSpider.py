import scrapy
from BusSpider.items import BusspiderItem
from scrapy.http import Request


class BusSpider(scrapy.Spider):

    name = 'BusSpider'
    allowed_domains = ['bus.mapbar.com']
    start_urls = ['http://bus.mapbar.com/city/change/']


    def parse(self, response):
        # item = BusspiderItem()
        # item['city'] = response.xpath('/html/body/div/table[2]/tr[3]/td//a/text()').extract()
        # item['city_url'] = response.xpath("/html/body/div/table[2]/tr[3]/td//a/@href").extract()
        # yield  item


        city_list = response.xpath("/html/body/div/table[2]//tr//td/a")
        for city in city_list:
            item = BusspiderItem()
            # item['province'] = city.xpath("/html/body/div/table[2]//tr/th/text()").extract()
            item['city'] = city.xpath("./text()").extract()[0]
            item['city_url'] = city.xpath("./@href").extract()[0]
            # for city in citys:
            #     item['city'] = city
            # for url in city_urls:
            #     item['city_url'] = url

            # yield item

            # for city in province.xpath("//td"):
            #     item['city'] = city.xpath("./a/text()").extract()
            #     item['city_url'] = city.xpath("./a/@href").extract()
            #     yield item
            yield scrapy.Request(item['city_url'], meta={'item': item}, callback=self.more_line_url)


    def more_line_url(self, response):
        item = response.meta['item']

        item['more_line_url'] = response.xpath("/html/body/div[1]/div[3]/div/div[1]/div[2]/ul/li[3]/a[@class='more']/@href").extract()

        yield  item