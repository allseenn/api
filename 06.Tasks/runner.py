from scrapy.crawler import CrawlerProcess
from scrapy.utils.reactor import install_reactor
from scrapy.utils.log import configure_logging
from scrapy.utils.project import get_project_settings
from splash.spiders.unsplash import UnsplashSpider
import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))

if __name__ == "__main__":

    configure_logging()
    install_reactor("twisted.internet.asyncioreactor.AsyncioSelectorReactor")
    configure_logging
    process = CrawlerProcess(get_project_settings())
    #query = input("Введите тему для поиска: ")
    process.crawl(UnsplashSpider, query='Cobra')
    process.start()