AVITO_PAGE_XPATH = {
    "pagination": '//a[@class="pagination-page"]//@href',
    "lot": '//div[@data-marker="item"]//a[@itemprop="url"]/@href',
}

AVITO_LOT_XPATH = {
    "title": '//span[@class="title-info-title-text"]/text()',
    "price": '//span[@class="js-item-price"]/text()',
    "address": '//span[@class="item-address__string"]/text()',
    "description": '//div[@class="item-description-text"]/text()',
    "author": '//a[contains(@class,"seller-info-avatar")]/@href',
}
