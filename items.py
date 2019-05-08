# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class LuoxiaItem(scrapy.Item):
    # define the fields for your item here like:
     dirlevel1 = scrapy.Field()
     dirlevel2 = scrapy.Field()
     title = scrapy.Field()
     content = scrapy.Field()
     pass
