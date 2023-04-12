# coding = utf-8
"""解析链接：parse模块"""

# 1.urlparseurl
# API:string, scheme='', allow_fragments=True
# 利用标准的URL格式：scheme协议，netloc域名，
# path访问路径，params参数，query查询条件，#后是锚点
# from urllib.parse import urlparse
# result = urlparse('http://www.baidu.com/index.html;user?id=5#comment')
# print(type(result), result, sep='\n')

# 2.urlunparse
# API:可迭代对象，包含7个元素
# from urllib.parse import urlunparse
# data = ['http', 'www.baidu.com', 'index.html','user', 'a=6', 'comment']
# print(urlunparse(data))

# 3.urlsplit
# API:与urlparse一致，但是不解析params，只返回5个结果
# from urllib.parse import urlsplit
# result = urlsplit('http://ww.baidu.com/index.html;user?id=5#comment')
# print(result)

# 4.urlunsplit
# from urllib.parse import urlunsplit
# data = ['http', 'www.baidu.com', 'index.html', 'a=6', 'comment']
# print(urlunsplit(data))

# 5.urljoin
# API:base_url对新链接缺失scheme, netloc, path的部分进行补充
# from urllib.parse import urljoin
# print(urljoin('http://www.baidu.com', 'FAQ.html'))
# print(urljoin('http://www.baidu.com', 'https://cuiqingcai.com/FAQ.html'))
# print(urljoin('http://www.baidu.com/about.html', 'https://cuiqingcai.com/index.php'))
# print(urljoin('www.baidu.com', '?category=2#comment'))

# 6.urlencode
# 用来构造GET请求参数，将字典序列化为GET请求
# from urllib.parse import urlencode
# params = {
#     'name': 'germey',
#     'age': 22
# }
# base_url = 'http://www.baidu.com?'
# url = base_url+urlencode(params)
# print(url)

# 7.parse_qs
# 将一串GET请求参数转回字典
# from urllib.parse import parse_qs
# query = 'name=germey&age=22'
# print(parse_qs(query))

# 8.parse_qsl
# 将参数转化为元组组成的列表，与parse_qs作用一致，只是输出形式不一样

# 9.quote
# 将内容转化为URL编码的格式，譬如讲中文参数转化，防止乱码
# from urllib.parse import quote
# keyword = '参数'
# url = 'https://www.baidu.com/s?wd='+quote(keyword)
# print(url)

# 10.unquote
# 进行URL解码
from urllib.parse import unquote
url = 'https://www.baidu.com/s?wd=%E5%8F%82%E6%95%B0'
print(unquote(url))



