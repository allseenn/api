import scrapy

class CountriesSpider(scrapy.Spider):
    name = "countries"
    allowed_domains = ["tradingeconomics.com"]
    start_urls = ["https://tradingeconomics.com/country-list/inflation-rate?continent=world"]

    def parse(self, response):
        countries = response.xpath("//td/a")
        for country in countries:
            name = country.xpath(".//text()").get().strip()
            link = country.xpath(".//@href").get()
            yield response.follow(url=link, callback=self.parse_country, meta={"name": name})


    def parse_country(self, response):
        rows = response.xpath("//tr[contains(@class, 'datatable-row')]")
        for row in rows:
            related = row.xpath(".//td[1]/a/text()").get().strip()
            #title_link = row.xpath(".//td[1]/a/@href").get()
            last = float(row.xpath(".//td[2]/text()").get().strip())
            try:
                previous = float(response.xpath(".//td[3]/text()").get().strip())
            except:
                previous = response.xpath(".//td[3]/text()").get().strip()
        yield {
                "name": response.request.meta["name"],
                "related": related,
                "last": last,
                "previous": previous
            }

