# coding = utf-8


"""异常处理：urllib的error模块"""

# 1.URLEError类
# 打开一个不存在的网页
# from urllib import request, error
# try:
#     response = request.urlopen("https://cuiqingcai.com/index.htm")
# except error.URLError as e:
#     print(e.reason)

# 2.HTTPError类
# 具有三个属性：code状态码，reason错误原因，headers请求头
# from urllib import request, error
# try:
#     response = request.urlopen('https://cuiqingcai.com/index.htm')
# except error.HTTPError as e:
#     print(e.reason, e.code, e.headers, sep='\n')
# 优化：URLError是HTTPError的父类，所以可以先捕获子类的错误，再捕获父类的错误

# 3.reason返回类的情况
import socket
import urllib.request
import urllib.error
try:
    response = urllib.request.urlopen('https://www.baidu.com', timeout=0.01)
except urllib.error.URLError as e:
    print(type(e.reason))
    if isinstance(e.reason, socket.timeout):
        print('Time Out')
