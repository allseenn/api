# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from itemloaders.processors import TakeFirst, MapCompose, Compose

def proccess_name(value):
    return value

def proccess_price(value):
    try:
        value = value[0].strip().replace("xa0", " ").split()
        value[0] = float(value[0])
    except:
        pass
    return value

def proccess_photos(value):
    return value.replace("//ndc.", "http://ndc.").replace("w410", "w820").replace("410x590", "820x1180")

class BookparserItem(scrapy.Item):
    name = scrapy.Field(input_processor=Compose(proccess_name), output_processor=TakeFirst())
    url = scrapy.Field(output_processor=TakeFirst())
    price = scrapy.Field(input_processor=Compose(proccess_price))
    photos = scrapy.Field(input_processor=MapCompose(proccess_photos))
    _id = scrapy.Field()
