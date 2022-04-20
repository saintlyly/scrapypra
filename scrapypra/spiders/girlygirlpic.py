
import scrapy
import json

from scrapy.http.request import Request
from scrapy.selector import Selector


class GirlygirlpicSpider(scrapy.Spider):
    name = 'girlygirlpic'
    
    
    def start_requests(self):
     
        url = "https://en.girlygirlpic.com/api/getcountryalbumslist"

        payload = {
            "action": "load_infinite_content",
            #paged分页
            "next_params": "paged=1&posts_per_page=10&post_status=publish&category__in=0",
            "layout_type": "v3",
            "template_type": "",
            "page_id": "pid407",
            "random_index": 0,
            "model_id": "",
            "company_id": "",
            "tag_id": "",
            "country_id": "6imhhs2",
            "type_tag": "Company",
            "search_keys_tag": ""
        }
        headers = {
            'authority': 'en.girlygirlpic.com',
            'accept': 'application/json, text/javascript, */*; q=0.01',
            'accept-language': 'zh-CN,zh;q=0.9',
            'content-type': 'application/json',
            'cookie': '_ga=GA1.1.260901069.1650075980; _user_language=En; _clck=1uakkkb|1|f0p|0; dom3ic8zudi28v8lr6fgphwffqoz0j6c=84e367bc-743f-4486-802c-9f82594cbc42%3A1%3A1; _ga_1T7ZPY6GGW=GS1.1.1650188587.6.0.1650188587.0; zone-cap-4420168=1; _clsk=ds1d3k|1650188667916|1|1|b.clarity.ms/collect; _user_language=En',
            'origin': 'https://en.girlygirlpic.com',
            # 'referer': 'https://en.girlygirlpic.com/l/6imhhs2',
            'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="100", "Google Chrome";v="100"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"macOS"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.88 Safari/537.36',
            'x-requested-with': 'XMLHttpRequest'
        }

        if payload['next_params'] is not None:
            #注意传入payload使用的方法
            yield Request(url,self.getpageurl,headers=headers,method="POST",body=json.dumps(payload))
        
    def getpageurl(self,response):
        jsonresponse=response.json()
        #response 为json 格式 需要构建选择器 再进一步选择
        selector = Selector(text=jsonresponse['new_posts'], type="html")
        #页面中所有model链接
        data_url=selector.xpath('//div[@class="figure-link-w no-ads"]/a/@href').getall()
        # print(data)
        for single_modal_url in data_url:
            
            url = "https://en.girlygirlpic.com/ax/"
            
            payloadid=single_modal_url.split('/')[-1]
            
            payload = {
                
                "album_id": payloadid
            }
            headers = {
                'authority': 'en.girlygirlpic.com',
                'accept': '*/*',
                'accept-language': 'zh-CN,zh;q=0.9',
                'content-type': 'application/json',
                'cookie': '_ga=GA1.1.260901069.1650075980; _user_language=En; _ga_1T7ZPY6GGW=GS1.1.1650105311.4.1.1650106636.0; sb_main_3954c4e9eb36a3ec329b506677cf5f13=1; sb_count_3954c4e9eb36a3ec329b506677cf5f13=1; zone-cap-4420168=1; _clck=1uakkkb|1|f0p|0; _clsk=1ejejkg|1650178406405|1|1|l.clarity.ms/collect; _user_language=En',
                'origin': 'https://en.girlygirlpic.com',
                # 'referer': 'https://en.girlygirlpic.com/a/6s1w6dc',
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
    
    #下载图片        
    def parse(self, response):
        #print(response.body)
          
        #图片地址
        img_src=response.xpath('//div[@class="figure-link-w"]/a/figure/picture/source/img/@data-src').getall()
          #图片名称
        name=response.xpath('//div[@class="figure-link-w"]/a/figure/picture/source/img/@alt').getall()
        name2=str(name)[1:20]
        name1=str(name)[40:60]
        image_name=name2+name1

    
        yield {
          'image_urls':img_src,
          'image_name':image_name
        }
   