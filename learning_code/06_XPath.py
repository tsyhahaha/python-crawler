# _*_ coding: utf-8 _*_
"""
@File       : 06_XPath.py
@Author     : Tao Siyuan
@Date       : 2021/12/7
@Desc       :...
"""
from lxml import etree
text = """
<div>
<ul>
<li class="item-0"><a href="link1.html">first item</a></li>
<li class="item-1"><a href="link2.html">second item</a></li>
<li class="item-inactive"><a href="link3.html">third item</a></li>
<li class="item-1"><a href="link4.html">fourth item</a></li>
<li class ="item-0"><a href="links html">fifth item</a>
</ul>
</div>
"""

"""1.所有节点"""
# html = etree.parse('./test.html', etree.HTMLParser())
# result = html.xpath('//*')
# print(result)
# result = html.xpath('//li')
# print(result)
# print(result[0])

"""2.子节点"""
# /用于获得直接子节点
# html = etree.parse('./test.html', etree.HTMLParser())
# result = html.xpath('//li/a')
# print(result)

"""3.父节点"""
# html = etree.parse('./test.html', etree.HTMLParser())
# result = html.xpath('//a[@href="link4.html"]/../@class')
# print(result) # 或将..换成parent::*

"""4.属性匹配"""
# html = etree.parse('./test.html', etree.HTMLParser())
# result = html.xpath('//li[@class="item-0"]')
# print(result)

"""5.文本获取"""
html = etree.parse('./test.html', etree.HTMLParser())
result = html.xpath('//li[@class="item-0"]//text()')    # 所有子孙节点的文本
print(result)   # 会包含换行符等特殊字符
result = html.xpath('//li[@class="item-0"]/a/text()')   # a节点中的文本
print(result)   # 可以保证获取结果是整洁的

"""6.属性获取"""
# @即可获取，至此我们学会了如何获取节点间文本和节点内属性
# html = etree.parse('./test.html', etree.HTMLParser())
# result = html.xpath('//li/a/@href')
# print(result)

"""7.属性多值匹配"""
# 针对节点属性可能有多个值
# text = """
# <li class="li li-first"><a href="link.html">first item</a></li>
# """
# html = etree.HTML(text)
# result = html.xpath('//li[@class="li"]/a/text()')
# print(result)   # 无输出
# result = html.xpath('//li[contains(@class, "li")]/a/text()')
# print(result)   # 正确输出------contains(@属性名称，属性值)

"""8.多属性匹配"""
# 根据多个属性确定一个节点，用and连接
# text = """
# <li class="li li-first" name="item"><a href="link.html">first item</a></li>
# """
# html = etree.HTML(text)
# result = html.xpath('//li[contains(@class, "li") and @name="item"]/a/text()')
# print(result)   # 注意@符号，任何属性都必须有
# # 类似and的xpath运算符，参见书本165面

"""9.按序选择"""
# html = etree.parse('./test.html', etree.HTMLParser())
# result = html.xpath('//li[1]/a/text()')     # 第一个li节点
# print(result)
# result = html.xpath('//li[last()]/a/text()')    # 最后一个li节点
# print(result)
# result = html.xpath('//li[position()<3]/a/text()')  # 位置小于3的节点
# print(result)
# result = html.xpath('//li[last()-2]/a/text()')  # 倒数第三个节点，不能用-3
# print(result)

"""10.节点轴选择"""
# html = etree.HTML(text)
# result = html.xpath('//li[1]/ancestor::*')  # 获取所有祖先节点，需要跟::，*表示节点选择器匹配所有节点
# print(result)
# result = html.xpath('//li[1]/ancestor::div')    # 节点选择器为div
# print(result)
# result = html.xpath('//li[1]/attribute::*')     # 调用attribute轴，获取所有属性值，*表示获取节点所有属性
# print(result)
# result = html.xpath('//li[1]/child::a[@href="link1.html"]') # child获取直接子节点，::后跟节点选择器
# print(result)
# result = html.xpath('//li[1]/descendant::span')  # descendant轴获取所有子孙节点
# print(result)
# result = html.xpath('//li[1]/following::*[2]')   # following轴获取当前节点之后的所有节点
# print(result)
# result = html.xpath('//li[1]/following-sibling::*')  # 当前节点之后所有同级节点
# print(result)