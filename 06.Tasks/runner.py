#!/usr/bin/env python
from scrapy.crawler import CrawlerProcess
from scrapy.utils.reactor import install_reactor
from scrapy.utils.log import configure_logging
from scrapy.utils.project import get_project_settings
from splash.spiders.unsplash import UnsplashSpider
import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))

if __name__ == "__main__":
    query = input("Введите тему для поиска: ").replace(' ', '-')
    configure_logging()
    install_reactor("twisted.internet.asyncioreactor.AsyncioSelectorReactor")
    configure_logging
    settings = get_project_settings()
    settings.set('IMAGES_STORE', query)
    settings.set('FEED_EXPORT_FIELDS', ['name', 'photos', 'description', 'date'])
    settings.set('FEEDS', {
                            query+'.csv': {
                                'format': 'csv',
                                'item_export_kwargs': {
                                    'include_headers_line': False,
                                    'delimiter': '\t',  
                                },
                            }})
    process = CrawlerProcess(settings=settings)
    process.crawl(UnsplashSpider, query=query)
    process.start()