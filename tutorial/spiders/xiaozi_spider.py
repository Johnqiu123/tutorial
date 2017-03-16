# -*- coding: utf-8 -*-
"""
Created on Sat Mar 04 15:29:04 2017

@author: Administrator
"""

import scrapy

class XiaoZiSpider(scrapy.Spider):
    name = "xiaozi"   # 定义爬虫的名字
    allowed_domains = ["tmall.com"]
    start_urls= [
       "https://detail.tmall.com/item.htm?spm=a230r.1.14.6.0n53Ma&id=527911556039&cm_id=140105335569ed55e27b&abbucket=10"
    ]
    
    def parse(self, response):
        filename = response.url.split("/")[-2]
        with open(filename, 'wb') as f:
            f.write(response.body)