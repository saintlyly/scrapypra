import scrapy


class GirlygirlpicSpider(scrapy.Spider):
    name = 'girlygirlpic'
    allowed_domains = ['l']
    start_urls = ['http://l/']

    def parse(self, response):
        pass
