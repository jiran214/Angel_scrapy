# Define here the models for your spider middleware
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/spider-middleware.html

from scrapy import signals

# useful for handling different item types with a single interface
from itemadapter import is_item, ItemAdapter
from scrapy.http import HtmlResponse


class FuckCloudflare:
    def process_response(self, request, response, spider):
        url = request.url
        headers = {
            'referer': url,
            'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36 Edg/105.0.1343.53",
            'cookie': 'ajs_anonymous_id=c74b35cf-132a-45bf-95d4-19afef65f7df; _ga=GA1.2.1714380603.1664534851; _hjSessionUser_1444722=eyJpZCI6ImIxMjYwY2YwLTEwMjctNWM1YS1hMjRhLWQ2OGU2YTk2NzU5NSIsImNyZWF0ZWQiOjE2NjQ1MzQ4NTI1NTgsImV4aXN0aW5nIjp0cnVlfQ==; _gid=GA1.2.31759059.1664722470; _gcl_au=1.1.656541638.1664722470; _angellist=f1d61f63e988358752bddb6077c10d0c; logged_in=true; ajs_user_id=15271168; __stripe_mid=9ede5fa4-2c84-4380-aba1-34de104637a23a3556; iterableEndUserId=593848579@qq.com; iterableEmailCampaignId=1189667; iterableTemplateId=1661410; iterableMessageId=88d05de18e6845f99f5b3d5c1143bdc8; __cf_bm=KobHp9mwJHbnArFF0K.cmQb8BoOLEHBpWsHynvtJ3_Q-1664784617-0-Ab3ww/A7NgDszScSmXA23eFp45X2nX1JmIJpIY+VqUOToVAf09952nVUcfgreMU1v6oMDzS+lNr/Iiy4PIPjdwI=; _hjIncludedInSessionSample=0; _hjSession_1444722=eyJpZCI6IjE2ODdlY2Y2LWVlNjMtNDk3ZS05NzMyLTE3ZTY2MDAxMDExMyIsImNyZWF0ZWQiOjE2NjQ3ODQ2MjI3MTcsImluU2FtcGxlIjpmYWxzZX0=; _hjAbsoluteSessionInProgress=0; _gat=1; _hjCachedUserAttributes=eyJhdHRyaWJ1dGVzIjp7ImFsaXN0X3ByZXZpb3VzbHlfaW52aXRlZCI6ZmFsc2UsImNhbmRpZGF0ZV9kZXNpcmVkX3NhbGFyeV9jdXJyZW5jeSI6IlVTRCIsImNhbmRpZGF0ZV9pbnRlcmVzdGVkX2xvY2F0aW9ucyI6W10sImNhbmRpZGF0ZV9sYXN0X2FjdGl2ZV9hdCI6IjIwMjItMTAtMDNUMDg6MTA6MjAuMDAwWiIsImNhbmRpZGF0ZV9sb2NhdGlvbl90YWdzIjpbIkh1emhvdSJdLCJjYW5kaWRhdGVfcHJpbWFyeV9yb2xlIjoiU29mdHdhcmUgRW5naW5lZXIiLCJjYW5kaWRhdGVfcXVhbGl0eSI6ImluY29tcGxldGVfY2FuZGlkYXRlIiwiY2FuZGlkYXRlX3JlbW90ZV93b3JrX3ByZWZlcmVuY2UiOmZhbHNlLCJjYW5kaWRhdGVfcm9sZV90YWdzIjpbIlNvZnR3YXJlIEVuZ2luZWVyIl0sImNyZWF0ZWRfYXQiOiIyMDIyLTEwLTAyVDE0OjU1OjM5LjAwMFoiLCJlbGlnaWJsZV9mb3JfYWxfZWxpdGUiOmZhbHNlLCJlbWFpbCI6IjU5Mzg0ODU3OUBxcS5jb20iLCJlbWFpbF9zdGF0dXMiOiJhY3RpdmUiLCJmaXJzdF9uYW1lIjoi5bWH54S2IiwiaXNfYWRtaW4iOmZhbHNlLCJpc19hbmdlbCI6ZmFsc2UsImlzX2NhbmRpZGF0ZV9zdWNjZXNzIjp0cnVlLCJpc19mb3VuZGVyIjpmYWxzZSwiaXNfZ3AiOmZhbHNlLCJpc19scCI6ZmFsc2UsImlzX3BjbiI6ZmFsc2UsImpvYl9zZWFyY2hfc3RhdHVzIjoib3BlbiIsImxhc3RfbG9naW5fYXQiOiIyMDIyLTEwLTAyVDE0OjU1OjQwLjAwMFoiLCJsYXN0X25hbWUiOiLltYfnhLYiLCJuYW1lIjoi5bWH54S2IiwicHJpbWFyeV9sb2NhdGlvbiI6Ikh1emhvdSIsInByb2ZpbGVfdXJsIjoiaHR0cHM6Ly9hbmdlbC5jby81OTM4NDg1NzkiLCJ5ZWFyc19leHBlcmllbmNlX2luX3ByaW1hcnlfcm9sZSI6MH0sInVzZXJJZCI6IjE1MjcxMTY4In0=; datadome=U8u9qtpP96pJvJsFRiPzZ5sw2kocXG5mUqhSOKwdrjcY3vNQWSRrUuoXbAfyqUUwP2oBuQbZHdjdYPFanGp4NtE_Limrbq.Oj.83SMmEAehJonPV9xBC.3eoyGJx11k'
        }
        if response.status == 403:
            if spider.name == 'company': # 这里是我个人的处理 因为一个中间件可能给多个爬虫使用 在这做一下区分
                rsp = spider.browser.get(url,
                                        # proxies={'http': 'http://127.0.0.1:7890', # 这里的代理主要是爬取外国网站做的处理
                                        #          'https': 'http://127.0.0.1:7890'},
                                        headers=headers)
                print(rsp.text)
                return HtmlResponse(url=url,
                                    body=rsp.text,
                                    encoding="utf-8",
                                    request=request)
        return response

class AngelScrapySpiderMiddleware:
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the spider middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_spider_input(self, response, spider):
        # Called for each response that goes through the spider
        # middleware and into the spider.

        # Should return None or raise an exception.
        return None

    def process_spider_output(self, response, result, spider):
        # Called with the results returned from the Spider, after
        # it has processed the response.

        # Must return an iterable of Request, or item objects.
        for i in result:
            yield i

    def process_spider_exception(self, response, exception, spider):
        # Called when a spider or process_spider_input() method
        # (from other spider middleware) raises an exception.

        # Should return either None or an iterable of Request or item objects.
        pass

    def process_start_requests(self, start_requests, spider):
        # Called with the start requests of the spider, and works
        # similarly to the process_spider_output() method, except
        # that it doesn’t have a response associated.

        # Must return only requests (not items).
        for r in start_requests:
            yield r

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)


class AngelScrapyDownloaderMiddleware:
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the downloader middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_request(self, request, spider):
        # Called for each request that goes through the downloader
        # middleware.

        # Must either:
        # - return None: continue processing this request
        # - or return a Response object
        # - or return a Request object
        # - or raise IgnoreRequest: process_exception() methods of
        #   installed downloader middleware will be called
        return None

    def process_response(self, request, response, spider):
        # Called with the response returned from the downloader.

        # Must either;
        # - return a Response object
        # - return a Request object
        # - or raise IgnoreRequest
        return response

    def process_exception(self, request, exception, spider):
        # Called when a download handler or a process_request()
        # (from other downloader middleware) raises an exception.

        # Must either:
        # - return None: continue processing this exception
        # - return a Response object: stops process_exception() chain
        # - return a Request object: stops process_exception() chain
        pass

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)
