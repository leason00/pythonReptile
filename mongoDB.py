#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
import pymongo
from pyExcelerator import *

reload(sys)
sys.setdefaultencoding('utf-8')


class MongoDB(object):
    def __init__(self):
        client = pymongo.MongoClient('x.x.x.x', 27017)  # 连接服务器
        db = client.leason  # 选择数据库
        db.authenticate("leason", "123456")
        self.bookCol = db.book  # 选择集合book


    def collect_data(self, creatBookId, data):
        data['_id'] = creatBookId
        self.bookCol.insert(data)
