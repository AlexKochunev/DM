import os
from scrapy.crawler import CrawlerProcess
from scrapy.settings import Settings

from lesson7.instagram.spiders.instagram import InstagramSpider


if __name__ == "__main__":
    crawler_settings = Settings()
    crawler_settings.setmodule("instagram.settings")
    crawler_proc = CrawlerProcess(settings=crawler_settings)
    tags = ["python", "programming"]
    crawler_proc.crawl(
        InstagramSpider,
        login='',
        password='#PWD_INSTAGRAM_BROWSER:10:1619456071:ATVQANMZL5iddoQk3OtgKwluOfYZRaV9YBKzOBl45e4v9CszcJbBN8pw9K8KocypLHsNlgJ1d+d6hggGowsi/0MbF8h0sOHMb+/vZxslpNCT3zZNd1kL0uPFDbn/+TGCrOYAmKqc/ZR5Uhhh',
        tags=tags,
    )
    crawler_proc.start()
