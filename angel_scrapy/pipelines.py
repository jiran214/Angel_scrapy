# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import scrapy
from itemadapter import ItemAdapter

import pymongo
# from scrapy.pipelines.images import ImagesPipeline
import requests

class AngelPipeline:
    """
    存储数据到mongodb
    """
    def __init__(self):
        pass
    def open_spider(self, spider):
        host = spider.settings['MONGODB_HOST']
        port = spider.settings['MONGODB_PORT']
        db_name = spider.settings['MONGODB_NAME']
        client = pymongo.MongoClient(host=host, port=port)
        self.db = client[db_name]

    def process_item(self, item, spider):

        collection = self.db[item.collection]
        # collection.insert_one(dict(item))
        collection.update({'name': item['name']}, {'$set': dict(item)}, True)  # company 重复则更新
        print(item['name'],'插入数据')
        return item

class ImagePipeline():
    """
    图片url转为二进制数据
    """
    def process_item(self, item, spider):
        if spider.name == 'company':
            image_url=item['logo']
            try:
                resp=requests.request(url=image_url,method='get').content
                # print(resp)
            except Exception as e:
                print(e)

            item['logo']=resp

        return item
