# python-crawler

本仓库包含 python 爬虫的基础演示代码的 jupyter notebook 以及一些爬虫项目。本仓库只作为 python 爬虫的入门参考，如想要详细学习 python 爬虫，请参考：

* [Python3 网络爬虫学习教程](https://cuiqingcai.com/17777.html)
* Github: [learn_python3_spider](https://github.com/wistbean/learn_python3_spider#learn_python3_spider)

## Learning Code

### 1、base knowledge

* Urllib: 最简单的爬虫 python 库
* Error: 利用 urllib.error 中定义的类来进行错误处理
* Parser: 利用 urllib.parser 来解析 url 以及组装 url
* Robots: 通过 Robots 协议了解某个站点下哪些网页可以爬取，哪些不可以爬取
* Requests: 利用 requests 库更灵活与方便的爬取网页
* XPath: 使用 XPath 从爬取到的网页中获取你想要的内容
* Beautiful_Soup: 一个（极其）方便提取网页内容的库
* Store: 如何组织和存储从网页爬取的信息

### 2、other methods

* Ajax: 爬取 js 渲染的网页、异步加载的网页内容
* Selenium: 直接模拟人类与网页交互与信息提取
* Scrapy: 一个爬虫框架

## douban_books
本项目为 2020 年 buaa 高工数据结构大作业的爬虫项目

* 爬取豆瓣图书网站：https://book.douban.com/。
* 利用 Hash 索引存储书本信息，利用余弦相似度匹配搜索。
* 构建简单的 GUI 完成图书信息检索(可能对 pyside2、pyqt5 版本有要求)

**反爬方法实现：**

* 随机设置User-Agent头
* 设置 IP 池（动态 IP）
* 请求延时设置

