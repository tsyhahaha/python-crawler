# _*_ coding: utf-8 _*_
"""
@File       : 08_store_data.py
@Author     : Tao Siyuan
@Date       : 2021/12/9
@Desc       :...
"""
import pandas as pd
import csv
import json
import requests
from pyquery import PyQuery as pq

"""1.txt保存"""
# url = 'httpd://www.zhihu.com/explore'
# headers = {
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome' +
#                   '/96.0.4664.45 Safari/537.36'
# }
# try:
#     html = requests.get(url, headers=headers).text
# except requests.ConnectionError as e:
#     print('error')
# doc = pq(html)
# items = doc('.explore-tab .feed-item').items()
# for item in items:
#     question = item.find('h2').text()
#     author = item.find('.author-link-line').text()
#     answer = pq(item.find('.content').html()).text()
#     file = open('explore.txt', 'a', encoding='utf-8')
#     file.write('\n'.join([question, author, answer]))
#     file.write('\n' + '='*50 + '\n')
#     file.close()

"""文件写入简化写法
    with open('explore.txt', 'a', encoding='utf-8') as file:
        file.write('\n'.join([question, author, answer]))
        file.write('\n' + '='*50 + '\n')
        结束时文件自动关闭
"""

"""2.JSON文件存储"""
# 1.字符串,转化为list、dict的json对象(loads method)
str = """
{
    "name": "Bob",
    "gender": "male",
    "birthday": "1992-10-18"
}
"""
# " not '
data = json.loads(str)
print(type(data), data, sep='\n')
# this method can read file.json as txt and transfer to list type or dict type
#
# # 2.list、dict的json对象转化为字符串(dumps method)
# data = [
#     {
#         'name': 'Bob',
#         'gender': 'male',
#         'birthday': '1992-10-18'
#     }
# ]
# with open('data.json', 'w') as file:
#     file.write(json.dumps(data))
# # 需要注意此时存入的格式只是一行字符串而不是缩进的json格式，改进如下：
# with open('data.json', 'w') as file:
#     file.write(json.dumps(data, indent=2))  # 缩进格数为2
# # 如果有中文可能出现乱码，改进如下：
# with open('data.json', 'w') as file:
#     file.write(json.dumps(data, indent=2, ensure_ascii=False))
# #
"""3.CSV文件存储"""
# # 1.写入
# head = ['id', 'name', 'age']
# objects = [
#     ['10001', 'Mike', 20],
#     ['10002', 'Bob', 22],
#     ['10003', 'Jordan', 21]
# ]
# with open('data.csv', 'w') as cf:
#     write = csv.writer(cf, delimiter='\t')
#     write.writerow(head)
#     for item in objects:
#         write.writerow(item)
#     # 这里写入多行可以改为
#     write.writerows(objects)
#
# # 爬虫所得数据一般会用字典表示，则写入方法改为：
#     objects = [
#     {'id': '10001', 'name': 'Mike', 'age': 20},
#     {'id': '10002', 'name': 'Bob', 'age': 22},
#     {'id': '10003', 'name': 'Jordan', 'age': 21}
# ]
#     write = csv.DictWriter(cf, fieldnames=head, delimiter='\t')
#     write.writeheader()
#     write.writerows(objects)
# 2.读出
# with open('data.csv', 'r', encoding='utf-8') as csvfile:
#     reader = csv.reader(csvfile)
#     for row in reader:
#         print(row)
# # 更方便的方法可以调用pandas库
# df = pd.read_csv('data.csv')
# print(df)



