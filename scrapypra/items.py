# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ScrapypraItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    images = Field()
    image_urls = Field()
    image_name = Field()
    image_paths = Field()
