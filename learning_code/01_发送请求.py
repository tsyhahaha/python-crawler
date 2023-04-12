# coding: utf-8
import urllib.request
import urllib.parse
import urllib.error
from urllib.request import HTTPPasswordMgrWithDefaultRealm, HTTPBasicAuthHandler, build_opener
from urllib.request import ProxyHandler
import http.cookiejar

# request模块

'''1.urlopen'''

"""获取python官网源代码"""
# response = urllib.request.urlopen('https://www.python.org')
# print(response.read().decode('utf-8'))
# print(response.status)
# print(response.getheaders())
# # 注意后面的s
# print(response.getheader('Server'))

"""data参数，如果添加则为post方式"""
# 好像翻车了， 可能是headers或者Agent的问题
# data = bytes(urllib.parse.urlencode({'word': 'hello'}), encoding='utf-8')
# response = urllib.request.urlopen('http: //httpbin.org/post', data=data)
# print(response.read())

"""timeout参数，超出这个时间抛出异常try out来处理"""
# try:
#     response = urllib.request.urlopen('http://httpbin.org/get', timeout=0.01)
# except urllib.error.URLError as e:
#     print(e.reason)

'''2.Request'''

"""Request类用法"""
# request = urllib.request.Request('https://python.org')
# response = urllib.request.urlopen(request)
# print(response.read().decode('utf-8'))

"""Request的构造"""
# 好像又翻车了，不过不知道原因是什么
# url = 'http://httpbin.org/post'
# headers = {
#     'User-Agent': 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)',
#     'Host': 'httpbin.org'
# }
# dict = {
#     'name': 'Germen'
# }
# data = bytes(urllib.parse.urlencode(dict), encoding='utf-8')
# req = urllib.request.Request(url=url, data=data, headers=headers, method='GET')
# response = urllib.request.urlopen(req)
# print(req.read().decode('utf-8'))

"""headers的add_header构造"""
# req = urllib.request.Request(url=url, data=data, method='POST')
# req.add_header('User-Agent', 'Mozilla/4.0(compatible; MSIE 5.5; Windows NT)')

"""3.高级用法"""

"""处理验证：请求需要输入账号密码等的网页"""
from urllib.request import HTTPPasswordMgrWithDefaultRealm, HTTPBasicAuthHandler, build_opener
#
# username = 'username'
# password = 'password'
# url = 'http://localhost:5000/'
# p = HTTPPasswordMgrWithDefaultRealm()   # p为对象
# p.add_password(None, url, username, password)   # 添加用户名和密码
# auth_handler = HTTPBasicAuthHandler(p)  # 实例化对象， 参数为p，建立处理验证的Handler
# opener = build_opener(auth_handler)  # 构建opener
#
# try:
#     result = opener.open(url)   # 调用open完成验证
#     html = result.read().decode('utf-8')
#     print(html)
# except URLError as e:
#     print(e.reason)

"""使用代理，在本地添加代理"""
# proxy_handler = ProxyHandler({
#     'http': 'http://127.0.0.1:9743',    # 本地搭建代理并运行在9743端口上
#     'https': 'https://127.0.0.1:9743'
# })
# opener = build_opener(proxy_handler)    # 利用handler构造Opener
# try:
#     response = opener.open('https://www.baidu.com')
#     print(response.read().decode('utf-8'))
# except urllib.error.URLError as e:
#     print(e.reason)

"""Cookies的获取与读取"""

# 直接输出
# cookie = http.cookiejar.CookieJar()     # 创建对象
# handler = urllib.request.HTTPCookieProcessor(cookie)    # 构造handler
# opener = urllib.request.build_opener(handler)
# response = opener.open('http://www.baidu.com')
# for item in cookie:
#     print(item.name+"="+item.value)

# 输出为文件格式
# filename = 'cookies.txt'
# cookie = http.cookiejar.MozillaCookieJar(filename)
# handler = urllib.request.HTTPCookieProcessor(cookie)
# opener = urllib.request.build_opener(handler)
# response = opener.open('http://www.baidu.com')
# cookie.save(ignore_discard=True, ignore_expires=True)
# 如果想保存成LWP格式的文件，则声明时采用# cookie = http.cookiejar.LWPCookieJar(filename)

# 读取本地Cookies文件
# cookie = http.cookiejar.MozillaCookieJar()
# cookie.load('cookies.txt', ignore_discard=True, ignore_expires=True)
# handler = urllib.request.HTTPCookieProcessor(cookie)
# opener = urllib.request.build_opener(handler)
# response = opener.open('http://www.baidu.com')
# print(response.read().decode('utf-8'))






