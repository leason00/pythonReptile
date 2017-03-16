#!/usr/bin/python
# -*- coding: utf-8 -*-

class UrlManager(object):
    def __init__(self):
        pass

    # 添加新的单个url，只添加不在新旧集合中的url
    def creat_url(self, id):
        book_id = id + 1
        url = "https://book.douban.com/subject/"+str(book_id)+"/"
        return url, book_id