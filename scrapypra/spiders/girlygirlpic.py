
import scrapy
import json

from scrapy.http.request import Request


class GirlygirlpicSpider(scrapy.Spider):
    name = 'girlygirlpic'

    #from最终页面download images
    def start_requests(self):
        
        url = "https://en.girlygirlpic.com/ax/"

        payload = {
            "album_id": "6s1w6dc"
        }
        headers = {
            'authority': 'en.girlygirlpic.com',
            'accept': '*/*',
            'accept-language': 'zh-CN,zh;q=0.9',
            'content-type': 'application/json',
            'cookie': '_ga=GA1.1.260901069.1650075980; _user_language=En; _ga_1T7ZPY6GGW=GS1.1.1650105311.4.1.1650106636.0; sb_main_3954c4e9eb36a3ec329b506677cf5f13=1; sb_count_3954c4e9eb36a3ec329b506677cf5f13=1; zone-cap-4420168=1; _clck=1uakkkb|1|f0p|0; _clsk=1ejejkg|1650178406405|1|1|l.clarity.ms/collect; _user_language=En',
            'origin': 'https://en.girlygirlpic.com',
            'referer': 'https://en.girlygirlpic.com/a/6s1w6dc',
            'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="100", "Google Chrome";v="100"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"macOS"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.88 Safari/537.36',
            'x-requested-with': 'XMLHttpRequest'
        }
        yield Request(url,self.parse,headers=headers,method="POST",body=json.dumps(payload))
        

    def parse(self, response):
        #图片地址
        img=response.xpath('//div[@class="figure-link-w"]/a/@href').getall()
        
        yield {
           'image_urls':img
        }
        