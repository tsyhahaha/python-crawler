# _*_ encoding: utf-8 _*_
from bs4 import BeautifulSoup
import requests
import re
import csv
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome' +
                  '/96.0.4664.45 Safari/537.36',
    'cookie': 'X_CACHE_KEY=ece8f41487b17b62eb072ada68433bb7; '
              'UM_distinctid=17da2ab69ac5fa-023f8786775b9b-978153c-144000-17da2ab69adda0; '
              'CNZZDATA1256768662=285564836-1639110366-%7C1639110366; '
              'Hm_lvt_4b9133806590c56da829d6827862ce2b=1639111683; '
              'Hm_lpvt_4b9133806590c56da829d6827862ce2b=1639111683; '
              '__gads=ID=37a9d01367780ab2-22ba90bd66cf0000:T=1639111682:RT=1639111682:S=ALNI_MYFZ-q'
              '-baHuXQj6TNee9qyd9SbWkw '
}

"""爬取第一个网站，GDP"""
url = 'https://www.shijiejingji.net/world/global/2019/206540.html'
html = requests.get(url, headers=headers)
html.encoding = 'utf-8'
html = html.text
soup = BeautifulSoup(html, 'lxml')
data_head = str(soup.table.thead.tr)
pattern = re.compile(r'<th scope="col">\s*(.*?)\s*</th>')
head_list = re.findall(pattern, data_head)
# print(head_list)
data_contents = soup.table.tbody.contents[:200]
data_list = []
pattern = re.compile(r'<td>\s*(.*?)\s*</td>')
for item in data_contents:
    temp_list = []
    str_item = str(item)
    new = re.findall(pattern, str_item)
    if new:
        temp_list.append(new)
    if temp_list:
        data_list.extend(temp_list)
# print(data_list)
with open('GDP.csv', 'w', newline='') as gdp:
    write = csv.writer(gdp, delimiter=',')
    write.writerow(head_list)
    write.writerows(data_list)

# """爬取第二个网站，地域面积与人口总数"""
url = 'http://www.chamiji.com/countryrank'
html = requests.get(url, headers=headers)
html.encoding = 'utf-8'
html = html.text
soup = BeautifulSoup(html, 'lxml')
# print(html)
head_list = ['名称', '总人口（万）', '面积（万）', '区域', '排名']
data = soup.tbody.contents[:200]
data_list = []
pattern_name = re.compile(r'<a href=.*?>(.*?)</a>')
pattern = re.compile(r'<td class=.*?>(.*?)</td>')
for item in data:
    temp_list = []
    name = re.findall(pattern_name, str(item))
    contents = re.findall(pattern, str(item))
    temp_list.extend(name)
    temp_list.extend(contents)
    if temp_list:
        data_list.append(temp_list)
with open('pp.csv', 'w', newline='') as pp:
    write = csv.writer(pp, delimiter=',')
    write.writerow(head_list)
    write.writerows(data_list)


def draw1(array, lable=None):
    name = array[:, 0]
    P = array[:, 1]
    plt.xticks(rotation=90)
    plt.rcParams['font.sans-serif'] = ['SimHei']
    plt.rcParams['axes.unicode_minus'] = False
    plt.bar(x=name, height=P, label=lable, color='steelblue', alpha=0.8)
    plt.ylabel('人口/万', fontsize=14)
    plt.title(lable, fontsize=14)
    plt.show()


def atoi(a):
    return eval(a.replace(',', '').replace('$', ''))


def atoi1(a):
    a = a.replace(',', '')
    pattern = re.compile(r'^(\d*\.?\d*).*?')
    data = eval(re.findall(pattern, a)[0])
    pattern = re.compile(r'\d*\.?\d*(.*?)$')
    weight = re.findall(pattern, a)
    if weight[0] == '万亿':
        data *= 10000
    return data


def draw2(array, lable=None):
    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)
    name = array[:, 1]
    money_per = list(map(atoi, list(array[:, 4])))
    plt.xticks(rotation=90)
    plt.rcParams['font.sans-serif'] = ['SimHei']
    plt.rcParams['axes.unicode_minus'] = False
    ax.bar(x=name, height=money_per, label=lable, color='steelblue', alpha=0.8)
    plt.ylabel("人均GDP/美元", fontsize=14)
    plt.title(lable, fontsize=14)
    plt.show()


# 1.数据分析：分析不同洲的国家总人口与面积的关系
data = pd.read_csv('pp.csv', encoding='gbk')
# print(data)
Asia = data.loc[data['区域'] == '亚洲']
# print(Asia)
Amer = data.loc[(data['区域'] == '北美洲') | (data['区域'] == '南美洲')]
Europe = data.loc[data['区域'] == '欧洲']
Oceania = data.loc[data['区域'] == '大洋洲']
Africa = data.loc[data['区域'] == '非洲']
# # 下面是数据可视化部分
fig = plt.figure()
Asia_pp = fig.add_subplot(1, 1, 1)
draw1(np.array(Asia), '亚洲人口分布')
draw1(np.array(Amer), '美洲人口分布')
draw1(np.array(Europe), '欧洲人口分布')
draw1(np.array(Oceania), '大洋洲人口分布')
draw1(np.array(Africa), '非洲人口分布')


# 2.数据分析：分析不同洲国家的GDP
data = pd.read_csv('GDP.csv', encoding='gbk')
# print(data)
data = np.array(data)
Asia_gdp = np.empty((0, 6))
Amer_gdp = np.empty((0, 6))
Europe_gdp = np.empty((0, 6))
Oceania_gdp = np.empty((0, 6))
Africa_gdp = np.empty((0, 6))
name = data[:, 1]
for i in range(1, 101):
    if name[i-1] in list(np.array(Asia)[:, 0]):
        row = data[i-1, :]
        Asia_gdp = np.row_stack((Asia_gdp, row))
    elif name[i-1] in list(np.array(Amer)[:, 0]):
        row = data[i-1, :]
        Amer_gdp = np.row_stack((Amer_gdp, row))
    elif name[i-1] in list(np.array(Europe)[:, 0]):
        row = data[i-1, :]
        Europe_gdp = np.row_stack((Europe_gdp, row))
    elif name[i-1] in list(np.array(Oceania)[:, 0]):
        row = data[i-1, :]
        Oceania_gdp = np.row_stack((Oceania_gdp, row))
    elif name[i-1] in list(np.array(Africa)[:, 0]):
        row = data[i-1, :]
        Africa_gdp = np.row_stack((Africa_gdp, row))

# print(Asia_gdp)
draw2(Asia_gdp, '亚洲人均GDP分布')
draw2(Amer_gdp, '美洲人均GDP分布')
draw2(Europe_gdp, '欧洲人均GDP分布')
draw2(Africa_gdp, '非洲人均GDP分布')

# 3.数据分析：人口与GDP的关系
pp_data = np.array(pd.read_csv('pp.csv', encoding='gbk'))
gdp_data = np.array(pd.read_csv('GDP.csv', encoding='gbk'))
objects_pre = np.empty((0, 5))
name = pp_data[:, 0]
gdp = gdp_data[:, 2]
gdp_per = gdp_data[:, 4]
for i in range(1, 101):
    if name[i-1] in gdp_data[:, 1]:
        row = pp_data[i-1, :]
        objects_pre = np.row_stack((objects_pre, row))
name_pp = objects_pre[:, 0]
name_gdp = gdp_data[:, 1]
space_colonm = np.empty((len(name_pp), 0))
objects = np.column_stack((objects_pre, space_colonm))
for i in range(len(objects)):
    j = list(name_gdp).index(name_pp[i])
    objects[i][3] = gdp[j]
    objects[i][4] = gdp_per[j]
print(objects)

# 所用数据
x = objects[:, 0][:32]
money = list(map(atoi1, list(objects[:, 3])))[:32]   # gdp总值
money_per = list(map(atoi, list(objects[:, 4])))[:32]   # gdp/person
P = list(objects[:, 1])[:32]
# 画图部分
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
plt.xticks(rotation=90)
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False
ax.bar(x=x, height=money, label='总人口与GDP的关系', color='steelblue', alpha=0.8)
plt.title(u'各国GDP总值')
plt.ylabel("GDP/亿美元", fontsize=14)
plt.show()

fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
plt.xticks(rotation=90)
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False
ax.bar(x=x, height=money_per, label='总人口与人均GDP的关系', color='steelblue', alpha=0.8)
ax.set_xlabel("人均GDP/美元", color='g')
plt.title(u'各国人均GDP')
plt.ylabel("GDP per person", fontsize=14)
plt.show()

fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
plt.xticks(rotation=90)
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False
ax.bar(x=x, height=P, label='各国总人口', color='steelblue', alpha=0.8)
ax.set_xlabel("人均GDP/$", color='g')
plt.title(u'各国人口数比较')
plt.ylabel("人口/万", fontsize=14)
plt.show()

fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
plt.plot(P, money, linewidth=2)
plt.title("人口与GDP总值的关系", fontsize=14)
plt.xlabel("人口/万", fontsize=14)
plt.ylabel("GDP/亿美元", fontsize=14)
plt.show()







