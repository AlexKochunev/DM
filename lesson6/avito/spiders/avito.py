import scrapy
from lesson6.avito.spiders.xpaths import AVITO_PAGE_XPATH, AVITO_LOT_XPATH
from lesson6.avito.loaders import AvitoLoader


class AvitoSpider(scrapy.Spider):
    name = 'avito'
    allowed_domains = ['avito.ru']
    start_urls = ['https://www.avito.ru/krasnodar/kvartiry/prodam?cd=1']
    handle_httpstatus_list = [403]

    def _get_follow_xpath(self, response, xpath, callback):
        for url in response.xpath(xpath):
            yield response.follow(url, callback=callback)

    def parse(self, response):
        callbacks = {"pagination": self.parse, "lot": self.lot_parse}
        for key, xpath in AVITO_PAGE_XPATH.items():
            yield from self._get_follow_xpath(response, xpath, callbacks[key])

    def lot_parse(self, response):
        print(1)
        loader = AvitoLoader(response=response)
        loader.add_value("url", response.url)
        for key, xpath in AVITO_LOT_XPATH.items():
            loader.add_xpath(key, xpath)
        yield loader.load_item()

