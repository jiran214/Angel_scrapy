import requests
import scrapy
from itemadapter import ItemAdapter
import pymongo
# from scrapy.pipelines.images import ImagesPipeline
# import requests

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

        try:
            collection.update_one({'name': item['name']}, {'$set': dict(item)}, True)  # company 重复则更新
            spider.logger.info('%s插入或更新数据' % item['name'])
        except Exception as e:
            spider.logger.error('%s管道-插入或更新错误-%s' % spider.name,e)
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

            except Exception as e:
                spider.logger.error('%s图片请求错误-%s' % spider.name,e)

            item['logo']=resp

        return item
