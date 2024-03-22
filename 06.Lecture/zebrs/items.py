# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from itemloaders.processors import TakeFirst, MapCompose, Compose

def proccess_price(price):
    return float(price.strip().replace(',', '').replace(' ', '_'))

def process_folder(folder):
    folder = folder.replace(' ', '_').replace('|', 'I').replace('*', 'X').replace(',', '').replace('\'', '') \
        .replace('\"', '').replace('(', '').replace(')', '').replace('!', '').replace('?', '').replace(':', '') \
        .replace(';', '').replace('&', '').replace('/', '').replace('\\', '').replace('=', '').replace('+', 'plus')
    return '<a href=./images/'+folder+'>images</a><br>'

class ZebrsItem(scrapy.Item):
    name = scrapy.Field()
    price = scrapy.Field(input_processor=MapCompose(proccess_price))
    image_urls = scrapy.Field()
    images = scrapy.Field()
    folder = scrapy.Field(input_processor=MapCompose(process_folder))
    