#!/usr/bin/python
# -*- coding: utf-8 -*-
import urllib2
from time import sleep
import random
from random import Random
import winsound


class HtmlDownloader(object):

    def __init__(self):
        pass

    def random_str(self,randomlength=11):
        str = ''
        chars = 'AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz0123456789'
        length = len(chars) - 1
        random = Random()
        for i in range(randomlength):
            str += chars[random.randint(0, length)]
        return str

    def downloadConf(self, url):
        Header = 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:40.0) Gecko/20100101 Firefox/40.0'  # 浏览器头描述
        try:
            request = urllib2.Request(url)
            request.add_header('User-Agent', Header)
            request.add_header('Cookie', 'bid='+self.random_str())
            response = urllib2.urlopen(request)
            page = response.read().decode('utf-8')
            return page
        except urllib2.URLError, e:
            if hasattr(e, "code"):
                print e.code
            if hasattr(e, "reason"):
                print e.reason
            if e.code == 403:
                winsound.Beep(600, 1000)  # 蜂鸣发出警告，音量600， 时常1000ms
                return 403
            if e.code == 404:
                winsound.Beep(600, 300)  # 蜂鸣发出警告，音量600， 时常300ms
                sleep(0.1)
                winsound.Beep(600, 300)  # 蜂鸣发出警告，音量600， 时常300ms
                return 404

    def download(self, url):
        times = 1
        if url is None:
            return None
        while True:
            html_page = self.downloadConf(url)
            if html_page == 404:  # 404错误，返回404，然后将url放入404Urls
                return 404
            elif html_page == 403:  # 如果出现403等错误，等待后继续爬取
                sleeptime = random.randint(20, 30) * times  # 递增等待时间
                print 'sleeping %d times...' % times
                times += 1
                sleep(sleeptime)
            else:
                return html_page

if __name__ == "__main__":
    pass
    # HtmlDownloader().random_str()
    # HtmlDownloader().download('https://book.douban.com/subject/26945561/')