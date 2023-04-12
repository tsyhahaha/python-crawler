# _*_ coding: utf-8 _*_
"""
@File       : 09_Ajax.py
@Author     : Tao Siyuan
@Date       : 2021/12/9
@Desc       :...
"""
"""微博ajax前十面内容爬取"""
from urllib.parse import urlencode
import requests
from pyquery import PyQuery as pq
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait



base_url = 'https://m.weibo.cn/api/container/getIndex?'
# add the headers
headers = {
    'Host': 'm.weibo.cn',
    'Referer': 'https://m.weibo.cn/u/2830678474',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome' +
                  '/96.0.4664.45 Safari/537.36',
    'X_Reqested-With': 'XMLHttpRequest',
}


def get_page(page):
    """transfer the params; each page need different params"""
    params = {
        'type': 'uid',
        'value': '2830678474',
        'containerid': '1076032830678474',
        'page': page,
    }
    url = base_url + urlencode(params)  # make the url structure
    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            return response.json()
    except requests.ConnectionError as e:
        print('Error', e.args)


