# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy

class CompanyScrapyItem(scrapy.Item):
    # define the fields for your item here like:
    collection = 'angel_company'
    logo = scrapy.Field()
    name = scrapy.Field()
    des = scrapy.Field()
    overview = scrapy.Field()
    website = scrapy.Field()
    locations = scrapy.Field()
    company_size = scrapy.Field()
    total_raised = scrapy.Field()
    company_type = scrapy.Field()
    market = scrapy.Field()
    pass

class AngelScrapyItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass
