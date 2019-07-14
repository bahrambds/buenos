import scrapy
import psycopg2
import unicodedata
from ..items import buenosItem


class spiderComputer(scrapy.Spider):
    name = 'computer'
    start_urls = []
    list_urls = []
    conn = psycopg2.connect("dbname=article-database user=bb")
    cur = conn.cursor()
    cur.execute("select url from tech where content is null and source_name = 'Computerhoy.com';")
    all_tupled_urls = cur.fetchall()
    conn.close()
    for i in all_tupled_urls:
        list_urls.append(list(i))
    for i in list_urls:
        start_urls.append(i[0])


    def __init__(self): # Constructor for our class
        # Since we did our own constructor we need to call the parents constructor
        scrapy.Spider.__init__(self)
        self.base_name = None

    def parse(self, response):
        items = buenosItem()
        
        items['href'] = response.xpath('//*[@rel="canonical"]/@href').get()
        items['content']  = response.xpath('string(//*[@class="block-roba-list"])').get().replace("'","`").replace(u'\u2013','\n').replace(u'\u00f3','ó').replace(u'\u00e9','é').replace(u'\u00e1','á').replace(u'\u201c','"').replace(u'\u00f1','ñ').replace(u'\u201d','"').replace(u'\u00fa','ú').replace(u'\u20ac','%').replace(u'\u00ed','í').replace(u'\u00a0','\n\n').replace(u'\u00bf','¿').replace(u'\u2014','\n').replace(u'\u00a1','\n\n').replace(u'\u2026','\n').replace(u'\u00ba', '\n')
        yield items
    
    
