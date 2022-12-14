import scrapy
# import cloudscraper

from angel_scrapy.items import CompanyScrapyItem


class CompanySpider(scrapy.Spider):
    name = 'company'

    # browser = cloudscraper.create_scraper()
    headers = {
        'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36 Edg/105.0.1343.53",
    }

    def start_requests(self):
        cookie = {
            'cookies': "_ga=GA1.2.1714380603.1664534851; _hjSessionUser_1444722=eyJpZCI6ImIxMjYwY2YwLTEwMjctNWM1YS1hMjRhLWQ2OGU2YTk2NzU5NSIsImNyZWF0ZWQiOjE2NjQ1MzQ4NTI1NTgsImV4aXN0aW5nIjp0cnVlfQ==; _gid=GA1.2.31759059.1664722470; _gcl_au=1.1.656541638.1664722470; __stripe_mid=9ede5fa4-2c84-4380-aba1-34de104637a23a3556; iterableEndUserId=593848579@qq.com; iterableEmailCampaignId=1189667; iterableTemplateId=1661410; iterableMessageId=88d05de18e6845f99f5b3d5c1143bdc8; _angellist=e13633e721df47f02545c4aab7fe34c1; ajs_user_id=15271168; ajs_anonymous_id=c74b35cf-132a-45bf-95d4-19afef65f7df; _hjSession_1444722=eyJpZCI6IjQ1NjNkY2I1LTcwYTAtNDY0Zi1iYWM5LTQwZWY2MjhkMWNjYyIsImNyZWF0ZWQiOjE2NjQ3OTQ3NTU3MjUsImluU2FtcGxlIjpmYWxzZX0=; _hjAbsoluteSessionInProgress=0; __stripe_sid=c332a32a-bff6-4819-9ad8-497092c454783be30d; __cf_bm=rE29j0lgchqPffHdEU_qrHVR5FfVVmKhnmGM8Vpoll4-1664806325-0-AQp+cz6lOmaXW2/Nn2LEEzHU9cccJ5aRKec4ioflkJBsEI9tSLRt/D2t+l7yhFIkzY/wHbS0FDcGFSOIC9IY0Y8=; _hjIncludedInSessionSample=0; datadome=0Q_TOQegSPHASNKBWGMDqo1k6c4G0T~jd6wk-QemFI_Pj4ADNFGVQmrWz7T4kEN6-eMN78V44faGFbYfSfELu1.71em0ne2910Z~2t4XBf1mJx2Q4N~EVR2a5QvuuLB; _gat=1"}
        keyword = ['matillion', 'grubmarket', 'reliaquest', 'singlestore', 'bluevoyant', 'fourkites', 'jupiterone',
                   'immuta', 'databricks', 'rivigo', 'nuvemshop', 'patsnap', 'scalapay', 'nexii', 'petcircle',
                   'unstoppabledomains', 'timescale', 'omadahealth', 'leadsquared', 'carebridgehealth']
        base_url = "https://angel.co/search?q=%s&type=companies"

        for k in keyword:
            yield scrapy.Request(url=base_url % k, headers=self.headers, cookies=cookie, callback=self.search_parse,
                                 meta={'keyword': k})

    def search_parse(self, response):
        """
        ????????????????????????????????????????????????????????????????????????
        """
        MAX_MATCH = 1  # ????????????????????????????????????
        keyword = response.meta['keyword']

        # xpath??????????????????
        hrefs = response.xpath('//div[@class="result-pic"]/a/@href').getall()
        cookie = {
            'cookies': '_ga=GA1.2.1714380603.1664534851; _hjSessionUser_1444722=eyJpZCI6ImIxMjYwY2YwLTEwMjctNWM1YS1hMjRhLWQ2OGU2YTk2NzU5NSIsImNyZWF0ZWQiOjE2NjQ1MzQ4NTI1NTgsImV4aXN0aW5nIjp0cnVlfQ==; _gid=GA1.2.31759059.1664722470; _gcl_au=1.1.656541638.1664722470; __stripe_mid=9ede5fa4-2c84-4380-aba1-34de104637a23a3556; iterableEndUserId=593848579@qq.com; iterableEmailCampaignId=1189667; iterableTemplateId=1661410; iterableMessageId=88d05de18e6845f99f5b3d5c1143bdc8; _angellist=e13633e721df47f02545c4aab7fe34c1; ajs_user_id=15271168; ajs_anonymous_id=c74b35cf-132a-45bf-95d4-19afef65f7df; _hjSession_1444722=eyJpZCI6IjQ1NjNkY2I1LTcwYTAtNDY0Zi1iYWM5LTQwZWY2MjhkMWNjYyIsImNyZWF0ZWQiOjE2NjQ3OTQ3NTU3MjUsImluU2FtcGxlIjpmYWxzZX0=; _hjAbsoluteSessionInProgress=0; __stripe_sid=c332a32a-bff6-4819-9ad8-497092c454783be30d; __cf_bm=rE29j0lgchqPffHdEU_qrHVR5FfVVmKhnmGM8Vpoll4-1664806325-0-AQp+cz6lOmaXW2/Nn2LEEzHU9cccJ5aRKec4ioflkJBsEI9tSLRt/D2t+l7yhFIkzY/wHbS0FDcGFSOIC9IY0Y8=; _gat=1; _hjIncludedInSessionSample=0; datadome=.0d_E3pGiGO0BKDxNpiNnIEAZhdHJ20dd2IFkkQEaKaVxhalkVTMF8lbUkVb02PmWglQ1hSgge9_m0-7ZzXHHlJC-nNBs8Wo5EE2wFj2Iwr~3j0IJBsINJ0DY56KrwRf'}
        if hrefs:
            # ???????????????????????????

            if len(hrefs) == 1:
                self.logger.info('%s???????????????company' % keyword)
                yield scrapy.Request(url=hrefs[0], headers=self.headers, cookies=cookie, callback=self.company_parse)
            else:
                self.logger.info('%s???????????????%d???company' % (keyword, len(hrefs)))
                for h in hrefs[:MAX_MATCH]:
                    yield scrapy.Request(url=h, headers=self.headers, cookies=cookie, callback=self.company_parse)

        else:
            self.logger.warn('%s????????????????????????company' % keyword)
            # redis ?????? ?????????????????????
            PATH = 'D:/mypro/scrpay_pro/angel/angel_scrapy/log/waitKeyword.txt'
            with open(file= PATH , mode='a') as f:
                f.write(keyword+';')
                f.close()

    def company_parse(self, response):
        div = response.xpath('//div[@class="styles_wrapper__J5pNi"]')

        # 1.logo
        logo = div.xpath(
            '//div[@class="inline-flex flex-row items-center relative border border-gray-400 bg-gray-100 rounded-md h-18 w-18"]/img/@src').get()
        # 2.name
        name = div.xpath(
            '//a[@class="styles_component__UCLp3 styles_defaultLink__eZMqw styles_anchor__Zq69Z"]/text()').get()
        # 3.des
        des = div.xpath('//div[@class="styles_name__qn8jG"]/h2/text()').get()
        # 4.title
        overview = div.xpath('//div[@class="styles_content__XhI8z"]/header/text()').get()
        # content
        content = div.xpath('//div[@class="styles_component__481pO"]/div/text()').get()
        if content:
            overview = overview + '\n' + content

        # ???????????????
        about = div.xpath('./aside/div/div[1]/dl')
        # 5.website
        website = about.xpath('//li[@class="styles_websiteLink___Rnfc"]/a/@href').get()
        # 6.Locations
        locations = about.xpath('./dt[2]/ul/li/text()').getall()
        # 7.Company size
        company_size = about.xpath('./dt[3]/text()').get()
        # 8.Total raised
        total_raised = about.xpath('./dt[4]/text()').get()
        # 9.Company type
        company_type = about.xpath('./dt[@class="styles_tags__y_J8v"]/preceding-sibling::*[2]/span/text()').getall()
        # 10.Market
        market = about.xpath('//dt[@class="styles_tags__y_J8v"]/span/text()').getall()

        # ??????
        company_item = CompanyScrapyItem()

        company_item['logo'] = logo
        company_item['name'] = name
        company_item['des'] = des
        company_item['overview'] = overview
        company_item['website'] = website
        company_item['locations'] = locations
        company_item['company_size'] = company_size
        company_item['total_raised'] = total_raised
        company_item['company_type'] = company_type
        company_item['market'] = market

        print('logo:', logo,
              '\nname:', name,
              '\ndes:', des,
              '\noverview:', overview,
              '\nwebsite:', website,
              '\nLocations:', locations,
              '\ncompany_size:', company_size,
              '\ntotal_raised:', total_raised,
              '\ncompany_type:', company_type,
              '\nmarket:', market, )

        yield company_item


