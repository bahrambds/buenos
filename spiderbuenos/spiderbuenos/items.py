# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class buenosItem(scrapy.Field):

    href = scrapy.Field()
    content = scrapy.Field()


class spiderItem(scrapy.Field):

    img_url = scrapy.Field()
    url = scrapy.Field()
    title = scrapy.Field()
    content = scrapy.Field()
    source_name = scrapy.Field()

class longspiderItem(scrapy.Field):

    img_url = scrapy.Field()
    url = scrapy.Field()
    title = scrapy.Field()
    content = scrapy.Field()
    source_name = scrapy.Field()
    description = scrapy.Field()
    author = scrapy.Field()
    date_published = scrapy.Field()
