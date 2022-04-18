import scrapy
from scrapy.pipelines.images import ImagesPipeline
from scrapy.exceptions import DropItem
from scrapy.http.request import Request



class CustomImagesPipeline(ImagesPipeline):

    def get_media_requests(self, item, info):
        i = 1
        for image_url in item['image_urls']:
            filename = '{}_{}.jpg'.format(item['image_name'], i)
            yield scrapy.Request(image_url, meta={'filename': filename})
            i += 1
        return

    def file_path(self, request, response=None, info=None):
        return request.meta['filename']