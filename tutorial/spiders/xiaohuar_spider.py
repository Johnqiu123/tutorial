# -*- coding: utf-8 -*-
"""
Created on Sat Mar 04 14:56:52 2017

@author: Administrator
"""
import scrapy
import re
import urllib
import os

class XiaoHuarSpider(scrapy.Spider):
    name = "xiaohuar"   # 定义爬虫的名字
    allowed_domains = ["xiaohuar.com"]
    start_urls= [
       "http://www.xiaohuar.com/list-1-1.html",
    ]
    
    def parse(self, response):
        # 分析页面
        # 找到页面中符合规则的内容(校花图片)，保存
        # 找到所有的a标签，再访问其他标签，一层一层的搞下去
#        filename = "xiaohuar"
#        with open(filename, 'wb') as f:
#            f.write(response.body)
    
        print response.url
        # 如果url是http://www.xiaohuar.com/list-1-\d+.html
        # 如果url能够匹配到需要爬取得url，即本站url
        if re.match(r'http://www.xiaohuar.com/list-1-\d+.html',response.url): 
            print "dd"
            # select中填写查询目标，按scrapy查询语法书写
            items = response.xpath('//div[@class="item_list infinite_scroll"]/div')
            print len(items)
            for i in range(len(items)):
                # 查询所有img标签的src属性，即获取校花图片地址
                print i
                src = response.xpath('//div[@class="item_list infinite_scroll"]/div[%d]//div[@class="img"]/a/img/@src' % i).extract()              
                print src
                
                # 获取span的文本内容，即校花姓名
                name = response.xpath('//div[@class="item_list infinite_scroll"]/div\
                [%d]//div[@class="img"]/span/text()' % i).extract()
                print name
                # 校花学校
                school = response.xpath('//div[@class="item_list infinite_scroll"]/div\
                [%d]//div[@class="img"]/div[@class="btns"]/a/text()' % i).extract()
                print school
                if school: print school[0]
                
                if src:
                    ab_src = "http://www.xiaohuar.com" + src[0] # 相对路径拼接  
                    print ab_src
                    # 文件名，编码方式utf-8
                    file_name = "%s_%s.jpg" % (school[0],name[0])
                    print file_name
                    file_path = os.path.join("pic",file_name)
                    print file_path
                    urllib.urlretrieve(ab_src,file_path)
#                    print "ue"
#            all_urls = reponse.xpath()