# -*- coding: utf-8 -*-
import scrapy
import csv

from scrapy import Request
from scrapy import Selector


from semantic.items import SemanticItem


class DocfinderspiderSpider(scrapy.Spider):
    name = 'DocfinderSpider'
    allowed_domains = ['docfinder.at']
    
    def start_requests(self):
        #with open('plz_link.csv', 'r') as f:
        #with open('link_mit_st.csv', 'r') as f:
        #    reader = csv.reader(f)
        #    plz_list = list(reader)
        #arzt = ["anaesthesist", "lungenfacharzt", "kieferchirurgie", "allgemeinchirurg", "angiologe", "endokrinologe-diabetologe", "hno-arzt", "nephrologe", "intensivmediziner", "kardiologe", "gastroenterologe-hepatologe", "haematologe-onkologe", "internist", "psychiater", "kinderarzt", "rheumatologe", "radiologe", "haematologe-onkologe-radioonkologe", "augenarzt", "hautarzt", "plastischer-chirurg", "praktischer-arzt", "zahnarzt", "neurochirurg", "neurologe", "neuropathologe", "urologe", "frauenarzt", "orthopaede", "orthopaede-traumatologe"]
        arzt = ["pharmakologe-toxikologe", "transfusionsmediziner", "nuklearmediziner","immunologe", "herzchirurg", "gerichtsmediziner", "arbeitsmediziner","tropenmediziner", "infektiologe", "strahlentherapeut-radioonkologe", "kinderneurologe", "proktologe"]
        
        urls = ['https://www.docfinder.at/suche/'+j+'?whereType=country' for j in arzt]
        #urls = ['https://www.docfinder.at/suche/'+j+'/'+i[0] for i in plz_list for j in arzt]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        links = response.css("div.search-results > a::attr('href')").getall()
        links = [response.urljoin(link) for link in links]
        for link in links:
            yield Request(url=link, callback=self.parse_detail)
            
        next_url = response.css("div.card.pagination a.icon-right::attr('href')").get()
        next_url = response.urljoin(next_url)

        yield Request(url=next_url, callback=self.parse)

    def parse_detail(self, response):
        item = SemanticItem()
        item['name'] = response.css("div.base-info h1 ::text").get()
        try:
            item['bewertung'] = response.css("div.df-rating.df-rating-desktop-large ::text").get().strip()
            item['anz_bewertung'] = response.css("span.count ::text").get().strip("()")
        except AttributeError:
            item['bewertung'] = None
            item['anz_bewertung'] = None
        linkHtml = response.css("span.phone-number ::attr('data-full')").get()
        n = Selector(text=linkHtml)
        item['tel'] = n.css("a::text").get()
        item['adresse'] = response.css("div.address span ::text").get().strip()
        item['fach'] = response.css("div.professions span ::text").getall()
        item['krankenkassen'] = response.css("div.insurances.hidden-md-down ul.item-list li ::text").getall()
        item['ausbildung'] = response.css("div.med-areas.one-hidden-md-down ul.item-list li ::text").getall()
        item['zertifikate'] = response.css("div.diplomas.hidden-md-down ul.item-list li ::text").getall()
        weekdays = response.css("div.opening-hours.hidden-md-down ul.days li.day")
        days = ['mo', 'di', 'mi', 'do', 'fr', 'sa', 'so']
        for i, day in enumerate(days):
            try:
                item[day] = weekdays[i].css(".times > ::text").getall()
            except IndexError:
                item[day] = None
        
        yield item
