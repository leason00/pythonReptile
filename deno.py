#!/usr/bin/python
# -*- coding: utf-8 -*-
import urllib2
import urllib
import cookielib

url = 'https://book.douban.com/subject/26910001/'
user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
values = {'username': 'cqc',  'password': 'XXXX'}
headers = {'User-Agent': user_agent}
data = urllib.urlencode(values)
request = urllib2.Request(url, data, headers)
try:
    response = urllib2.urlopen(request)
    page = response.read()
    print page
except urllib2.URLError, e:
    print e.code
    if hasattr(e, "reason"):
        print e.reason
else:
    print "OK"