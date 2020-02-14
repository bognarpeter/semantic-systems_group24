# -*- coding: utf-8 -*-
import scrapy
import csv
import json
from scrapy import Request

from semantic.items import PlzItem


class DocfinderStadtname(scrapy.Spider):
    name = 'DocfinderStadtname'
    allowed_domains = ['docfinder.at']

    def start_requests(self):
        with open('plz_list.csv', 'r') as f:
            reader = csv.reader(f)
            plz_list = list(reader)
        
        urls = ['https://www.docfinder.at/search/autosuggest/where?term='+i[0] for i in plz_list]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse, headers={'Accept': 'application/json, text/plain, */*'})
	
    def parse(self, response):
        data = json.loads(response.body_as_unicode())
        
        for entry in data:
            item = PlzItem()
            item['plz'] = entry['text']
            item['name'] = entry['hint']
            item['link'] = entry['value']
            yield item

    def parse_detail(self, response):
        pass