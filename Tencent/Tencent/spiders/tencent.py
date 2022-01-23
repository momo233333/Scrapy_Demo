import scrapy
from Tencent.items import TencentItem,CommandItem
import json
import chardet
import datetime
import hashlib


class TencentSpider(scrapy.Spider):
    name = 'tencent'
    # allowed_domains = ['careers.tencent.com']
    base_url = 'https://careers.tencent.com/tencentcareer/api/post/Query?pageIndex={}&pageSize=10&language=zh-cn&area=cn'
    url_list = ["https://www.baidu.com", 'https://www.huawei.com', 'https://cn.bing.com/']

    offset = 1
    start_urls = url_list

    def parse(self, response):
        # item = TencentItem()
        item = CommandItem()
        url = response.url
        status = response.status
        text = response.text
        timestamp = datetime.datetime.now().strftime("%Y%m%d%H%M%S%f")
        md5_decoder = hashlib.md5()
        md5_decoder.update(timestamp.encode("utf-8"))
        html_id = md5_decoder.hexdigest()
        item['url'] = url
        item['status'] = status
        item['text'] = text
        item['timestamp'] = timestamp
        item['html_id'] = html_id
        yield item

        # print(results)
        # node_list = results['Data']['Posts']
        # for node in node_list:
        #     # 职位名称
        #     item['position_name'] = node.get('RecruitPostName')
        #     # 职位等级
        #     item['position_level'] = node.get('BGName')
        #     # 职位地区
        #     item['position_localtion'] = node.get('LocationName')
        #     # 职位部门
        #     item['position_department'] = node.get('CategoryName')
        #     # 职位发布日期
        #     item['position_updatetime'] = node.get('LastUpdateTime')
        #     # 职位描述
        #     item['position_description'] = node.get('Responsibility')
        #     yield item
