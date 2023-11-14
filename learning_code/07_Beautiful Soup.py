# _*_ coding: utf-8 _*_
"""
@File       : 07_Beautiful Soup.py
@Author     : Tao Siyuan
@Date       : 2021/12/8
@Desc       :...
"""
import re

from bs4 import BeautifulSoup
html = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title" name="dromouse"><b>The Dormouse's story</b></p>
<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1"><?-- Elsie --></a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>
<p class="story">...</p>
"""

"""1.基本用法"""
soup = BeautifulSoup(html, 'lxml')  # 这个时候就已经进行补全了
# print(soup.prettify())  # 按标准缩进格式输出
# print(soup.title.string)    # 输出title内文本
# # method:chose the node; use string class to get the text

"""2.节点选择器"""
# 1.选择节点: 节点加文本内容，string获取文本内容
# soup = BeautifulSoup(html, 'lxml')
# print(soup.title)
# print(type(soup.title))     # bs4.elemnt.Tag
# print(soup.title.string)
# print(soup.head)
# print(soup.p)

# 2.获取节点名称
# print(soup.title.name)

# 3.获取节点属性attrs
# print(soup.p.attrs)  # 返回的是 ‘属性’: ‘属性值’ 的字典，所有属性
# print(soup.p.attrs['name'])
# print(soup.p['name'])   # 简化版，值得一提的是，如果对应多个属性值，会返回字符串列表
# # 必要时加上类型判断isinstance

# 4.嵌套选择
# print(soup.head.title)
# print(type(soup.head.title))    # still 'bs4.element.Tag'
# print(soup.head.title.string)

# 5.关联选择
# contents属性获取所有直接子节点
# print(soup.p.contents)  # 输出列表，只匹配第一个找到的p
# # children属性获取所有直接子节点，但返回类型是生成器，书本p186
# print(soup.p.children)
# for i, child in enumerate(soup.p.children):
#     print(i, child)
# 若选择子孙节点，则children换成descendants属性
# parent属性获取某个节点的父节点，parents获得所有祖先节点
# next/previous_sibling获取下一个/上一个兄弟元素;next/previous_siblings获取后面/前面所有兄弟节点的生成器

# 6.提取信息
# 对于节点，直接利用string属性，对于上述生成器，则需要list(parents)[0]再进一步选取属性

"""3.方法选择器"""
# 1.find_all(name, attrs, recursive, text, **kwargs)
soup = BeautifulSoup(html, 'lxml')
print(soup.find_all(name='ul'))  # 返回bs4.element.Tag类型的列表
print(soup.find_all(attrs={'id': 'list-1'}))
print(soup.find_all(id='list-1'))   # 简化版，注意引号！！！
print(soup.find_all(class_='element'))  # 注意下划线
print(soup.find_all(text=re.compile('link')))   # 参数可以是正则表达式也可以是字符串，返回的是匹配的整个节点文本组成的列表

# 2.find()返回的是单个元素（第一个匹配的元素）
# 另外还有其他find_xx方法，如parents、parent、next_siblings、previous_siblings等，知识范围不同

"""4.CSS选择器"""
# 只需调用select方法，传入CSS选择器即可，需要熟悉Web开发的CSS选择器
# 这是一个非常强大的选择器，还有pyquery库与其对应，有时间再学





