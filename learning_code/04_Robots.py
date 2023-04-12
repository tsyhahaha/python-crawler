# coding=utf-8

"""robots协议——网路爬虫排除标准
从中我们可以得知，那些页面可以抓取，哪些页面不能抓取"""

# robotparser
# 使用robotparser模块来解析robots.txt
# 具体构造方法与实例方法，见原书121页
# from urllib.robotparser import RobotFileParser
#
# rp = RobotFileParser()
# rp.set_url('http://www.jianshu.com/robots.txt')
# rp.read()
# print(rp.can_fetch('*', 'http://www.jianshu.com/p/b67554025d7d'))
# print(rp.can_fetch('*', 'http://www.jianshu.com/search?q=python&page=1&type=collections'))
# # 好像这个例子现在变了，第一个也不可以被抓取

# 使用parse()方法执行读取和分析
from urllib.robotparser import RobotFileParser
from urllib.request import urlopen
from urllib import error
rp =RobotFileParser()
try:
    rp.parse(urlopen('http://www.jianshu.com/robots.txt').read().decode('utf-8').split('\n'))
except error.URLError as e:
    print(e.code, e.reason)
# 事实上，robots.txt已经不能爬取了
print(rp.can_fetch('*', 'http://www.jianshu.com/p/b67554025d7d'))
print(rp.can_fetch('*', 'http://www.jianshu.com/search?q=python&page=1&type=collections'))




