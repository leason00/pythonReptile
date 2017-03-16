#!/usr/bin/python
# -*- coding: utf-8 -*-
import url_manager, html_downloader, html_parser, mongoDB
import time
import random

class SpiderMain(object):
    def __init__(self):
        self.urls = url_manager.UrlManager()  # url管理器
        self.downloader = html_downloader.HtmlDownloader()  # html网页下载器
        self.parser = html_parser.HtmlParser()  # html分析器
        self.mongodb = mongoDB.MongoDB()  # 数据库操作器

    def craw(self, rootId):
        count = 1
        creatUrl, creatBookId = self.urls.creat_url(rootId)
        while count < 100000:
            creatUrl, creatBookId = self.urls.creat_url(creatBookId)
            print count
            html_page = self.downloader.download(creatUrl)
            if html_page == 404:  # 某些页面一直是404,无法爬取
                print creatUrl + '404'
            else:
                print creatUrl + '200'
                try:
                    new_urls, new_data = self.parser.parse(creatUrl, html_page)  # 分析html，返回urls和data
                    if new_urls == False:
                        pass
                    else:
                        self.mongodb.collect_data(creatBookId, new_data)
                except Exception, e:
                    print e

            time.sleep(random.uniform(0.1, 0.3))
            count += 1


if __name__ == "__main__":
    rootId = 1477423  # 起始地址为《代码大全》
    # rootId = 26909999  # 起始地址为《代码大全》
    obj_spider = SpiderMain()
    obj_spider.craw(rootId)
