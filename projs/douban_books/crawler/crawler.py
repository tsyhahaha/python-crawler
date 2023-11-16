# _*_ coding: utf-8 _*_
import os
import json
import codecs
from requests.packages import urllib3
import requests
import re
from bs4 import BeautifulSoup
from lxml import etree
import time
import random
import hashlib
import numpy as np


urllib3.disable_warnings()


class bookshell(object):
    """
    用于寻找链接，与数据存储无关
    """
    def __init__(self, name, href=None, addr=None):
        self.name = name
        self.href = href
        self.addr = addr
        self.children = []

    def addchild(self, child):
        self.children.append(child)
        return


class book(object):
    def __init__(self, bookname):
        self.name = '《' + bookname + '》'
        self.author = ''
        self.translator = None
        self.publish = ''
        self.time = ''
        self.point = ''
        self.price = ''
        self.href = ''
        self.brief = ''
        self.short = ''
        self.long = ''
        self.author_bref = ''
        self.tags = []

    def getinfo(self):
        dic = {}
        dic['name'] = self.name
        dic['author'] = self.author
        dic['translator'] = self.translator
        dic['publish'] = self.publish
        dic['time'] = self.time
        dic['point'] = self.point
        dic['price'] = self.price
        dic['href'] = self.href
        dic['brief'] = self.brief
        dic['short'] = self.short
        dic['long'] = self.long
        dic['author_bref'] = self.author_bref
        dic['tags'] = self.tags
        return dic

    def __str__(self):
        """
        name,author,price,point,bref,tags,href
        :return:
        """
        infor = '{' + 'name:' + self.name + \
                ', author:' + self.author + \
                (', translator:' + self.translator if self.translator else '') + \
                ', publish:' + self.publish + \
                ', time' + self.time + \
                ', point:' + self.point + \
                ', price:' + self.price + \
                ', brief:' + self.brief + \
                ', author_brief:' + self.author_bref + \
                ', href:' + self.href + \
                ', tags:' + str(self.tags) + '}' + \
                ', short:' + self.short
                # ', long:' + self.long
        return infor



def get_ua():
    first_num = random.randint(55, 76)
    third_num = random.randint(0, 3800)
    fourth_num = random.randint(0, 140)
    os_type = [
        '(Windows NT 6.1; WOW64)', '(Windows NT 10.0; WOW64)', '(X11; Linux x86_64)',
        '(Macintosh; Intel Mac OS X 10_14_5)'
    ]
    chrome_version = 'Chrome/{}.0.{}.{}'.format(first_num, third_num, fourth_num)

    ua = ' '.join(['Mozilla/5.0', random.choice(os_type), 'AppleWebKit/537.36',
                   '(KHTML, like Gecko)', chrome_version, 'Safari/537.36']
                  )
    return ua


headers = {
        'User-Agent': get_ua(),
        'Connection': 'close'
}


def getips():
    urlbase = 'https://www.kuaidaili.com/free/inha/'
    right_pro = []
    ips = []
    for i in range(4, 5):
        url = urlbase + str(i) + '/'
        html = requests.get(url, headers=headers).text
        pattern = re.compile(r'<td data-title="IP">(.*?)</td>')
        page_ip = re.findall(pattern, html)
        ips.extend(page_ip)
    i = 0
    while i < len(ips):
        test = 'http://' + ips[i]
        proxy = {'http': test}
        try:
            response = requests.get('https://www.baidu.com', headers=headers, proxies=proxy, timeout=2)
            if response.status_code == 200:
                print('有效ip:', test)
                right_pro.append(test)
        except:
            print('无效ip:', test)
        i += 1
    return right_pro

ip = getips()
proxy = {
    'http': random.choice(ip)
}


def getpagebooks(link):
    """
    本方法将爬取书类的页面，返回100本书链接组成的列表
    :param link: 类别的地址，也就是基地址，加上参数可以限定页数
    :return: None
    """
    print(link)
    hrefs = []
    names = []
    num = 0
    while num < 100:
        shamt = '?start=' + str(num)
        num = int(num) + 20
        url = link + shamt
        try:
            html = requests.get(url, headers=headers, proxies=proxy)
            if html.status_code != 200:
                print('fail to get this page!')
            html = html.text
            time.sleep(random.random() * 3)
            html = etree.HTML(html)
            items = html.xpath('//li[@class="subject-item"]/div[@class="pic"]//a[1]/@href')
            hrefs.extend(items)
            names.extend(html.xpath('//li[@class="subject-item"]/div[@class="info"]/h2/a/@title'))
        except:
            print('failed to get this page!')
    return names, hrefs


def getBookData(href):
    """
    对于每一本书，我们需要将其信息存储到本地
    这些信息通过链接内容都可以获得
    :param href: 链接
    :param folder: 目的文件夹
    :return:
    """
    url = href
    try:
        html = requests.get(url, headers=headers, timeout=10, proxies=proxy, verify=False).text
        soup = BeautifulSoup(html, 'lxml')
        # name
        name = soup.title.string
        abook = book(name)
        # href
        abook.href = url
        # author price time publish translator
        info = soup.find_all(id="info")
        if info:
            info1 = info[0].text.replace(' ', '')
            pattern_author = re.compile(u'作者:\n{0,100}(.*?)\n')
            pattern_price = re.compile(u'定价:\n{0,100}(.*?)\n')
            pattern_time = re.compile(u'出版年:\n{0,100}(.*?)\n')
            pattern_publish = re.compile(u'出版社:\n{0,100}(.*?)\n')
            pattern_translator = re.compile(u'译者:\n{0,100}(.*?)\n')
            abook.author = re.findall(pattern_author, info1).pop()
            abook.price = re.findall(pattern_price, info1).pop()
            abook.time = re.findall(pattern_time, info1).pop()
            abook.publish = re.findall(pattern_publish, info1).pop()
            translator = re.findall(pattern_translator, info1)
            if translator:
                abook.translator = translator.pop()
        # point
        if soup.strong:
            abook.point = soup.strong.string
        # brief
        brief = ''
        aim = soup.find_all(attrs={"class": "indent", "id": "link-report"})[0]
        html_aim = etree.HTML(str(aim))
        lence = len(html_aim.xpath('//div[@class="intro"]'))
        if lence == 1:
            intro = html_aim.xpath('//div[@class="intro"]')[0]
        else:
            intro = html_aim.xpath('//div[@class="intro"]')[1]
        phs = intro.xpath('//p/text()')
        for ph in phs:
            if brief == '':
                brief += ph
            else:
                brief += '\n' + ph
        abook.brief = brief
        # author_brief
        author_brief = ''
        aim = soup.find_all(attrs={"class": "indent"})[2]
        html_aim = etree.HTML(str(aim))
        lence = len(html_aim.xpath('//div[@class="intro"]'))
        if lence == 1:
            intro = html_aim.xpath('//div[@class="intro"]')[0]
        else:
            intro = html_aim.xpath('//div[@class="intro"]')[1]
        phs = intro.xpath('//p/text()')
        for ph in phs:
            if author_brief == '':
                author_brief += ph
            else:
                author_brief += '\n' + ph
        abook.author_bref = author_brief
        # tags
        pattern_tags = re.compile(r'<a class="  tag" href="/tag/\S*?">(.*?)</a>')
        abook.tags = re.findall(pattern_tags, html)
        print('book:', abook.name, ' information-collected')
        # short text
        short_list = soup.find_all(class_="comment-content")
        if short_list:
            pattern1 = re.compile(r'<span class="hide-item full">(.*?)</span>')
            pattern2 = re.compile(r'<span class="short">(.*?)</span>')
            for i in range(len(short_list)):
                if short_list[i].contents is not None:
                    for temp in short_list[i].contents:
                        temp = str(temp)
                        if re.search(pattern1, temp):
                            short_list[i] = re.findall(pattern1, temp)[0]
                        elif re.search(pattern2, temp):
                            short_list[i] = re.findall(pattern2, temp)[0]
                        else:
                            continue
            for item in short_list:
                abook.short += str(item) + '\n'
    except Exception as e:
        print(f'{type(e)}: failed to get this book!', )
        abook = None
    return abook


def new_folder(path):
    """
    创建新的文件夹
    :param path:
    :return:
    """
    folder = os.path.exists(path)
    if not folder:  # 如果不存在该路径文件夹
        os.makedirs(path)
        print('new folder' + path + 'is setted')
    else:
        return


def addrcheck(addr):
    nope = ['?', '？',  '、', '\\', '/', '*', '<', '>', '|', ':']
    for item in nope:
        if item in addr:
            addr = addr.replace(item, '')
    return addr


def crawl_books(books_save_folder='./douban_books', addr_file='./addrs.txt'):
    url = 'https://book.douban.com/'
    s = requests.session()
    response = s.get(url, headers=headers, proxies=proxy, verify=False)
    if response.status_code != 200:
        print('code =', response.status_code, ', failed parse!')
        exit()
    else:
        print('code =', response.status_code, ', successfully parse')
    text = response.content.decode('utf-8')
    pattern = re.compile(r'<li class="tag_title">\s*(.*?)\s*</li>')
    tags_names = re.findall(pattern, text)
    path_books = books_save_folder
    new_folder(path_books)
    # 构建一个书本的链接树
    douban = bookshell('douban_books', 'https://book.douban.com/', path_books)
    soup = BeautifulSoup(text, 'lxml')
    books_list = soup.find_all(name='ul', class_="clearfix")[:6]
    for item in books_list:
        temp = BeautifulSoup(str(item), 'lxml')
        name = temp.li.string.strip()
        temp_shell = bookshell(name)
        douban.addchild(temp_shell)
        children = temp.find_all(class_="tag")
        # print(children)
        for item_in in children:
            name = item_in.string
            href = douban.href[:-1] + item_in.attrs['href']
            temp_in_shell = bookshell(name, href)
            temp_shell.addchild(temp_in_shell)
        temp_shell.children = temp_shell.children[:-1]  # 去除‘更多’栏

    # 接下来是依次按类爬取，类-》面-》书, 继续构建链接树
    a = codecs.open(addr_file, 'w+', encoding='utf-8', errors='ignore')

    for categorys in douban.children:
        for category in categorys.children:
            names, hrefs = getpagebooks(category.href)
            time.sleep((random.random() + 1) * 2)
            print(names, hrefs)
            for i in range(len(names)):
                abook = bookshell(names[i], hrefs[i])
                category.addchild(abook)
    # 所有链接树至此完毕：豆瓣->分类->在分类->每一类的100本书，所有链接在此
    for categorys in douban.children:
        addr1 = os.path.join(path_books, categorys.name)  # 第一次分类的类别
        categorys.addr = addr1
        print(addr1)
        new_folder(addr1)
        for category in categorys.children:
            addr2 = os.path.join(addr1, category.name)  # 第二次分类的类别
            category.addr = addr2
            print(addr2)
            new_folder(addr2)
            for a_book in category.children:
                jsonname = a_book.name + '.json'
                jsonname = addrcheck(jsonname)
                book_addr = os.path.join(addr2, jsonname)
                try:
                    with codecs.open(book_addr, 'w+', encoding='utf-8', errors='ignore') as file:
                        abook = getBookData(a_book.href)  # 返回book类
                        if abook is not None:
                            book_info = abook.getinfo()
                            if len(book_info) > 0:
                                json.dump(abook.getinfo(), file, indent=2, ensure_ascii=False)
                                print(book_addr, 'is written')
                                a_book.addr = book_addr
                                a.write(a_book.name + ' ' + os.path.abspath(a_book.addr) + '\n')
                except:
                    print('name :', a_book.name, 'is not allowed')
    a.close()

if __name__=='__main__':
    crawl_books(books_save_folder='/mnt/f/python-crawler/projs/douban_books/data/douban_books', addr_file='/mnt/f/python-crawler/projs/douban_books/data/addrs.txt')
















