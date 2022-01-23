# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import json
import pymongo


class TencentPipeline:
    def __init__(self, host, port, db_name, user, pwd, collection):
        self.content_uri="mongodb://{}:{}@{}:{}/?authSource={}&readPreference=primary".format(user, pwd, host, port, db_name)
        self.client = pymongo.MongoClient(self.content_uri)
        self.db = self.client[db_name]
        self.collection = self.db[collection]

    @classmethod
    def from_crawler(cls, crawler):
        db_info = crawler.settings.get('DB_SETTINGS')
        db_params = db_info.get('db1')
        return cls(
            host=db_params.get('host'),
            port=db_params.get('port'),
            db_name=db_params.get('db_name'),
            user=db_params.get('user'),
            pwd=db_params.get('pwd'),
            collection=db_params.get('collection')
        )

    def save_html(self, html_id, html):
        path = "I:\\Scrapy_Demo\\Tencent\\Tencent\\Html\\"
        fileName = html_id+".html"
        with open(path+fileName, 'w', encoding='utf-8') as fp:
            fp.write(html)

    def process_item(self, item, spider):
        result = dict(item)
        html = item.get('text')
        html_id = item.get('html_id')
        status = item.get('status')
        if status == 200:
            self.save_html(html_id, html)
        try:
            self.collection.insert_one(result)
            print("数据写入成功！")
        except Exception as e:
            print("数据写入异常："+str(e))

        return item

    def close_spider(self, spider):
        self.client.close()

