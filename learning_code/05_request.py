# _*_ encoding: utf-8 _*_
"""
@File       : 05_request库.py
@Author     : Tao Siyuan
@Date       : 2021/12/1
@Desc       :...
"""
import requests
import re
from requests.packages import urllib3
from requests.auth import HTTPBasicAuth
from requests import Request, Session

"""1.初步使用requests"""
# 简单实现get请求
# r = requests.get('https://www.baidu.com/')
# print(type(r))        # 'requests.models.Response'
# print(r.status_code)    # 状态码
# print(type(r.text))   # 'str'
# print(r.text)           # 内容
# print(r.cookies)        # Cookies
# get 方法与 urlopen 方法类似

# 简单实现POST，PUT，DELETE请求
# r = requests.post('http://httpbin.org/post')
# r = requests.put('http://httpbin.org/put')
# r = requests.delete('http://httpbin.org/get')
# r = requests.options('http://httpbin.org/get')

"""2.GET请求"""
# 1.简单请求
# r = requests.get('http://httpbin.org//get')
# print(r.text)

# 2.添加额外信息，链接的name、age等
# 不太聪明的做法：r = requests.get('http://httpbin.org/get?name=germey&age=22')
# data = {
#     'name': 'getmey',
#     'age': 22
# }
# r = requests.get('http://httpbin.org/get', params=data)
# print(r.text)
# 发现返回值中args中有参数，表明链接构造成功
# 在此基础上，可以调用json方法，将返回的r.text('str')转变为字典类型，前提是内容为JSON格式

# 3.抓取网页
# headers = {
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36'
# }
# r = requests.get('http://www.zhihu.com/explore', headers=headers)
# pattern = re.compile('explore-feed.*?question_link.*?>(.*?)</a>', re.S)
# titles = re.findall(pattern, r.text)
# print(titles)

# 4.抓取二进制内容
# 图片、音频、视频实际上都是二进制组成的文件，由于特定的存储格式与解析，才能看到这些东西
# headers = {
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36'
# }
# try:
#     r = requests.get('http://cscore.buaa.edu.cn/favicon.png', headers=headers)
#     print(r.text)
#     print(r.content)
# except requests.exceptions.RequestException as e:
#     print(e)
# with open('favicon.ico', 'wb') as f:
#     f.write(r.content)

"""4.POST请求"""
# data = {'name': 'germey', 'age': '22'}
# r = requests.post('http://httpbin.org/post', data=data)
# print(r.text)

"""5.响应"""
# 介绍属性和方法来获取除响应内容外的其他信息
# headers = {
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36'
# }
# r = requests.get('http://www.jianshu.com', headers=headers)
# print(type(r.status_code), r.status_code)
# print(type(r.headers), r.headers)
# print(type(r.cookies), r.cookies)
# print(type(r.url), r.url)
# print(type(r.history), r.history)
# 可以通过返回码和内置成功返回码的比较，来保证请求的正常响应，否则终止
# 更多的标准码参见141面
# exit() if not r.status_code == requests.codes.okay else print('Request Successfully')

"""6.高级用法"""

# 1.文件上传
# requests可以模拟提交一些数据，上传文件
# files = {'file': open('favicon.ico', 'rb')}
# r = requests.post("http://httpbin.org/post", files=files)
# print(r.text)

# 2.Cookies
# 1-获取cookies
# 既可以爬取，也可以直接查看然后复制粘贴
# r = requests.get('https://www.baidu.com')
# print(r.cookies)
# for key, value in r.cookies.items():
#     print(key, "=", value)
# 2-设置cookies参数——自行构造RequestsCookieJar对象
# 见144页构造与分割方法构造cookies

# 3.会话维持
# 不必打开众多页面，只需打开一个，进行多次访问
"""错误示例"""
# requests.get('http://httpbin.org/cookies/set/number/123456789')
# r = requests.get('http://httpbin.org/cookies')
# print(r.text)
"""正确示例"""
# s = requests.Session()
# s.get('http://httpbin.org/cookies/set/number/123456789')
# r = s.get('http://httpbin.org/cookies')
# print(r.text)

# 4.SSL证书验证
# 但是会警告说最好给他指定证书，我们可以设置忽略警告。
# urllib3.disable_warnings()
# response = requests.get('https://www.12306.cn', verify=False)
# print(response.status_code)
# # 当然也可以我们自己指定本地证书，可以是的那个文件（包含密钥和证书）或者一个包含两个文件路径的元组
# response = requests.get('https://www.12306.cn', cert=('/path/server.crt', '/path/key'))
# # 这要求本地有crt和key文件，并且指定路径。此时本地私有证书key必须是解密状态，否则无效

# 5.代理设置
# proxies参数，自行设置代理
# proxies = {
#     "http": "socks5://user:password@host:port",
#     "https": "socks5://user:password@host:port",
# }
# requests.get("hiips://www.taobao.com", proxies=proxies)

# 6.超时设置
# 可以直接设置timeout，也可以传入一个元组分别设置连接和读取的timeout
# r = requests.get("https://www.taobao.com", timeout=0.01)
# print(r.status_code)

# 7.身份认证(p137)
# r = requests.get('https://netboost.co/pricing', auth=HTTPBasicAuth('143370176', 'tsytsy2001112'))
# print(r.status_code)
# print(r.text)
# 其他认证方式还有OAuth1认证方法，参考书本138面

# 8.Prepared Request
url = 'http://httpbin.org/post'
data = {
    'name': 'germey'
}
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome' +
                  '/96.0.4664.45 Safari/537.36'
}
s = Session()
req = Request('POST', url, data=data, headers=headers)
prepped = s.prepare_request(req)
r = s.send(prepped)
print(r.text)





