import re
from urllib.parse import urljoin

from scrapy import Selector
from scrapy.loader import ItemLoader
from itemloaders.processors import MapCompose, TakeFirst


def avito_user_url(user_id):
    return urljoin("https://avito.ru/", user_id)


class AvitoLoader(ItemLoader):
    default_item_class = dict
    url_out = TakeFirst()
    title_out = TakeFirst()
    price_out = TakeFirst()
    address_out = TakeFirst()
    description_out = TakeFirst()
    author_out = MapCompose(avito_user_url)
