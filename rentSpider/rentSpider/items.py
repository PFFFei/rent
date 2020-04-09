# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy

# class RentspiderItem(scrapy.Item):
#     pass


from scrapy_djangoitem import DjangoItem
from rentAnalysis.models import Rent


class RentspiderItem(DjangoItem):
    django_model = Rent
