# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class TencentItem(scrapy.Item):
    # define the fields for your item here like:
    # 职位名称
    position_name = scrapy.Field()
    # 职位等级
    position_level = scrapy.Field()
    # 职位地区
    position_localtion = scrapy.Field()
    # 职位部门
    position_department = scrapy.Field()
    # 职位发布日期
    position_updatetime = scrapy.Field()
    # 职位描述
    position_description = scrapy.Field()


class CommandItem(scrapy.Item):
    url = scrapy.Field()
    text = scrapy.Field()
    status = scrapy.Field()
    timestamp = scrapy.Field()
    html_id = scrapy.Field()


