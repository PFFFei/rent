# -*- coding: utf-8 -*-
import scrapy
from rentSpider.items import RentspiderItem
import re


class HouseSpider(scrapy.Spider):
    name = 'house'
    allowed_domains = ['cd.lianjia.com']
    start_urls = ['https://cd.lianjia.com/ershoufang/']

    def parse(self, response):
        for url in response.xpath('//div[@data-role="ershoufang"]/div/a/@href').extract():
            yield scrapy.Request('https://cd.lianjia.com' + url, callback=self.page)

    def page(self, response):
        page = response.xpath('//div[@class="page-box house-lst-page-box"]/@page-data').extract()
        page = eval(page[0])
        for i in range(1, page['totalPage']):
            yield scrapy.Request(response.url + 'pg{}'.format(i), callback=self.detail)

    def detail(self, response):
        for li in response.xpath('//ul[@class="sellListContent"]/li'):
            item = RentspiderItem()
            item['district'] = response.xpath('//h2[@class="total fl"]/text()').extract()[1].strip("套,二手房")
            item['title'] = li.xpath('.//div[@class="title"]/a/text()').extract()[0]
            detail = li.xpath('.//div[@class="address"]/div/text()').extract()[0].split("|")
            item['bedroom'] = detail[0]
            item['area'] = detail[1]
            item['direction'] = detail[2]
            item['decoration'] = detail[3]
            item['total_price'] = li.xpath('.//div[@class="totalPrice"]/span/text()').extract()[0]
            item['unit_price'] = li.xpath('.//div[@class="unitPrice"]/@data-price').extract()[0]
            yield item
