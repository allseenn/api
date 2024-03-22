from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from scrapy.loader import ItemLoader
from zebrs.items import ZebrsItem
from itemloaders.processors import MapCompose
# from scrapy.loader.processors import MapCompose
from urllib.parse import urljoin

class ZebrsImagesSpider(CrawlSpider):
    name = "zebrs_images"
    allowed_domains = ["www.zebrs.com"]
    start_urls = ["https://www.zebrs.com/categories/smart-watch"]

    rules = (
        Rule(LinkExtractor(restrict_xpaths=['//div[@class="position-relative teaser-item-div"]']), callback="parse_item", follow=True),
        Rule(LinkExtractor(restrict_xpaths=['//a[@rel="next"]']))
    )

    def parse_item(self, response):
        loader = ItemLoader(item=ZebrsItem(), response=response)
        loader.default_input_processor = MapCompose(str.strip) 
        loader.add_xpath('name', '//h1/text()')
        loader.add_xpath('folder', '//h1/text()')
        price_text_danger = response.xpath('//div[@class="me-2 product-price text-danger"]/text()').get()

        if price_text_danger:
            loader.add_xpath('price', '//div[@class="me-2 product-price text-danger"]/text()')
        else:
            loader.add_xpath('price', '//div[@class="me-2 product-price"]/text()')

        # loader.add_xpath('image_urls', '//div[@class="col-md-6 col-lg-4"]/a/img/@src')
        relative_image_urls = response.xpath('//div[@class="text-center d-none d-sm-block dsktp-zoomer"]/ul/li/img/@src').getall()
        absolute_image_urls = [urljoin('https://'+ self.allowed_domains[0], img_url) for img_url in relative_image_urls]
        loader.add_value('image_urls', absolute_image_urls)

        yield loader.load_item()

