# -*- coding: utf-8 -*-
"""
Created on Sat Mar 04 09:46:54 2017

@author: Administrator
"""

import scrapy

class BaiduSpider(scrapy.Spider):
    name = "baidu"   # 定义爬虫的名字
    allowed_domains = ["baidu.com"]
    start_urls= [
       "http://www.baidu.com",
    ]
    
    def parse(self, response):
        current_url = response.url #爬取时请求的url
        body = response.body # 返回的html
        unicode_body = response.body_as_unicode() # 返回的html unicode 编码
        filename = response.url.split(".")[-2]
        with open(filename, 'wb') as f:
            f.write(response.body)

        