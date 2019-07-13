import scrapy
import psycopg2
import unicodedata
from ..items import longspiderItem
import itertools
from datetime import datetime

class spyd3rMuyint(scrapy.Spider):
    name = 'spymuyint'
    start_urls=[]
    for i in range(10):
        start_urls.append(f'https://www.muyinteresante.es/tecnologia/{i}')

    def __init__(self): # Constructor for our class
        # Since we did our own constructor we need to call the parents constructor
        scrapy.Spider.__init__(self)
        self.base_name = None

    
    def parse(self, response):
        for href in response.xpath('//*[@class="list--image--link article"]/@href').getall():
            url = f'https://www.muyinteresante.es/{href}'
            yield response.follow(url, self.parse_muyint)


    def parse_muyint(self, response):
        items = longspiderItem()

        items['source_name'] = response.xpath('//*[@rel="canonical"]/@href').get().split('www.')[1].split('.es')[0]
        items['description'] = response.xpath('string(//*[@class="article--summary"])').get()
        longcontent = []
        for i in range(20):
            longcontent.append(response.xpath(f'string(//*[@id="paragraph_{i}"])').getall()) 
        content = ' '.join(str(e) for e in longcontent)
        
        clean_content = content.replace("'","").replace(", ['']", "").replace('[','').replace(']','')
        
        items['content'] = clean_content
        items['title'] = response.xpath('string(//*[@class="article--title"])').get()
        items['url'] = response.xpath('//*[@property="og:url"]/@content').get()
        items['img_url'] = response.xpath('//*[@class="imgContent pull-center"]/@src').get()
        items['author'] = response.xpath('//*[@rel="author"]/@title').get()
        a = response.xpath('//*[@class="article--date--time d-none d-sm-block"]/@datetime').get()
        if a is None:
            items['date-published'] = datetime.now().isoformat()
        else:
            items['date-published'] =  datetime.strptime(a, '%d/%m/%Y').isoformat()
        
        yield items
    


    
  