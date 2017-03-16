#!/usr/bin/python
# -*- coding: utf-8 -*-
import re
from bs4 import BeautifulSoup

class HtmlParser(object):
    def __init__(self):
        pass

    def parse(self, url, page):
        res_data = {}
        res_data['url'] = url
        if url is None or page is None:
            return
        test = re.findall( re.compile('<div.*?nav-logo">.*?<a.*?>(.*?)</a>',re.S), page)
        if test[0] != '豆瓣读书':
            print 'not book'
            return False, False
        else:
            try: #舍弃页面信息不完全的url
                soup = BeautifulSoup(page, 'html.parser', from_encoding='utf-8')
                #url
                res_data['url'] = url
                #<span property="v:itemreviewed">代码大全</span>
                res_data['bookName'] = soup.find('span', property='v:itemreviewed').string
                #<strong class="ll rating_num " property="v:average"> 9.3 </strong>
                res_data['score'] = soup.find('strong', class_='ll rating_num ').string
                res_data['bg_url'] = soup.find('a', class_='nbg').attrs["href"]
                '''
                <div id="info" class="">
                <span>
                  <span class="pl"> 作者</span>:
                  <a class="" href="/search/Steve%20McConnell">Steve McConnell</a>
                </span><br>
                <span class="pl">出版社:</span> 电子工业出版社<br>
                <span class="pl">出版年:</span> 2007-8<br>
                <span class="pl">页数:</span> 138<br>
                <span class="pl">定价:</span> 15.00元<br>
                <span class="pl">ISBN:</span> 9787115281586 #前面有一个空格
                </div>
                '''
                info = soup.find('div', id='info')
                res_data['author'] = info.find(text=' 作者').next_element.next_element.string
                res_data['publisher'] = info.find(text='出版社:').next_element
                res_data['time'] = info.find(text='出版年:').next_element
                res_data['price'] = info.find(text='定价:').next_element
                res_data['ISBN'] = info.find(text='ISBN:').next_element.strip()
                res_data['intro'] = soup.find('div', class_='intro').find('p').string
                print res_data['bookName']
                return url, res_data
            except:
                print 'invalid data'
                return False, False

if __name__ == "__main__":
    pass
    # # url = 'https://book.douban.com/subject/26910001/'
    # url = 'https://book.douban.com/subject/1477390/'
    # html_parser = HtmlParser()
    # html_parser.parse(url, 200)