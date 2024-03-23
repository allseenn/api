# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
# импортируем 3 из 6(7) обработчиков
from itemloaders.processors import TakeFirst, MapCompose, Compose

def proccess_name(name):
    name = name[0].strip()
    return name

def proccess_tags(tags):
    try:
        tags = tags[0].strip().replace("xa0", " ").split()
        tags[0] = float(tags[0])
    except:
        pass
    return tags

def proccess_photos(photos):
    return photos.replace("//ndc.", "http://ndc.").replace("w410", "w820").replace("410x590", "820x1180")


class SplashItem(scrapy.Item):
    name = scrapy.Field(input_processor=Compose(proccess_name), output_processor=TakeFirst())
    url = scrapy.Field(output_processor=TakeFirst())
    tags = scrapy.Field(input_processor=Compose(proccess_tags))
    photos = scrapy.Field(input_processor=MapCompose(proccess_photos))
    _id = scrapy.Field()
