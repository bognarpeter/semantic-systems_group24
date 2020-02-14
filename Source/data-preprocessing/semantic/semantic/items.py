# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class SemanticItem(scrapy.Item):
    # define the fields for your item here like:
    name = scrapy.Field()
    fach = scrapy.Field()
    tel = scrapy.Field()
    adresse = scrapy.Field()
    bewertung = scrapy.Field()
    anz_bewertung = scrapy.Field()
    krankenkassen = scrapy.Field()
    #zeit = scrapy.Field()
    ausbildung = scrapy.Field()
    zertifikate = scrapy.Field()
    mo = scrapy.Field()
    di = scrapy.Field()
    mi = scrapy.Field()
    do = scrapy.Field()
    fr = scrapy.Field()
    sa = scrapy.Field()
    so = scrapy.Field()

class PlzItem(scrapy.Item):
    plz = scrapy.Field()
    name = scrapy.Field()
    link = scrapy.Field()