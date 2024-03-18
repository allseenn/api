from scrapy.crawler import CrawlerProcess
from scrapy.utils.reactor import install_reactor
from scrapy.utils.log import configure_logging
from scrapy.utils.project import get_project_settings
from jobparser.spiders.hhru import HhruSpider
from jobparser import settings

if __name__ == "__main__":
    configure_logging()
    settings = get_project_settings()
    install_reactor("twisted.internet.asyncioreactor.AsyncioSelectorReactor")
    process = CrawlerProcess(settings)
    process.crawl(HhruSpider)
    process.start()
