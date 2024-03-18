import scrapy
from scrapy.http import HtmlResponse
from jobparser.items import JobparserItem

class HhruSpider(scrapy.Spider):
    name = "hhru"
    allowed_domains = ["hh.ru"]
    start_urls = ["https://hh.ru/search/vacancy?text=python&area=1&hhtmFrom=main&hhtmFromLabel=vacancy_search_line"]

    def parse(self, response: HtmlResponse):
        next_page = response.xpath('//a[@data-qa="pager-next"]/@href').get()
        if next_page:
            yield response.follow(next_page, callback=self.parse, meta={'proxy': 'http://38.162.25.54:3128'})

        links = response.xpath('//a[contains(@href, "hh.ru/vacancy/")]/@href').getall()
        for link in links:
            yield response.follow(link, callback=self.vacancy_parse, meta={'proxy': 'http://38.162.25.54:3128'})
              
    def vacancy_parse(self, response: HtmlResponse):
        name = response.xpath('//h1[@data-qa="vacancy-title"]/text()').get()
        try:
            salary = response.xpath('//div[@data-qa="vacancy-salary"]//text()').getall()
        except:
            salary = ''
        url = response.url
        yield JobparserItem(name=name, salary=salary, url=url)
        
