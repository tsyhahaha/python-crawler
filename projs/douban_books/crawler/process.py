# _*_ coding: utf-8 _*_
import numpy as np
import hashlib
import re
import jieba
import math
import os


def Hash(key):
    m = hashlib.md5()
    m.update(key)
    hex_value = m.hexdigest()
    sum = str(bin(int(hex_value, 16)))[-13:]
    index = int(sum, 2)
    return hex_value, index


class Node(object):
    def __init__(self, hashnum, key, value):
        Node.element = [hashnum, key, value]
        Node.next = None

    def addnext(self, node):
        self.next = node


vocab = []
file_wordlist = {}


def tf(aim_table, words, docs):
    """
    返回文件与单词对应的TF值表
    :param aim_table:
    :param words:
    :param docs: 文件的单词表汇总，字典类型
    :return:
    """
    names = list(docs.keys())
    for i in range(len(names)):
        for word in docs[names[i]]:
            c = words.index(word)
            aim_table[i][c] += 1
        if docs[names[i]]:
            aim_table[i] = aim_table[i]/len(docs[names[i]])
    return aim_table


def idf(table):
    """
    计算每一列的IFD值与原来的TF矩阵相乘
    :param table: 已经记录TF值的矩阵
    :return:
    """
    D = table.shape[0]
    for c in range(table.shape[1]):     # 对每一列分析，每一列只有一个idf值
        tf = table[:, c]
        Dw = np.count_nonzero(tf) + 1
        idf = math.log(D/Dw)
        table[:, c] = table[:, c] * idf
    return table

def process(stopward_file='../data/stopword.txt', addrs_file='../data/addrs.txt'):
    with open(stopward_file, 'r', encoding='utf-8') as s:
        stopwords = s.read().split('\n')
    with open(addrs_file, 'r', encoding='utf-8') as a:
        # addrs.txt里面全都是已经写入本地的文件
        lines = a.readlines()
        for line in lines:
            line = line.replace('\n', '').split(' ')
            name = line[0]
            addr = line[1]
            if os.path.exists(addr):
                with open(addr, 'r', encoding='utf-8') as f:
                    bookinfo = f.read()
                    pattern = re.compile(r'[\u4e00-\u9fa5]+', re.S)
                    text = ''.join(re.findall(pattern, bookinfo))     # re.S将整个文本当做整体进行匹配
                    word_list = jieba.lcut_for_search(text)
                    i = 0
                    while i <= len(word_list)-1:
                        if word_list[i] in stopwords:
                            word_list.pop(i)
                        elif word_list[i] not in vocab:
                            vocab.append(word_list[i])
                            i += 1
                        else:
                            i += 1
                if word_list:
                    file_wordlist[name] = word_list
                    # print(name, word_list)
            else:
                print(name, addr, 'is non-existed!')
    # 至此，单词总表与文件单词列表字典已完全建立
    table = np.zeros(shape=[len(file_wordlist), len(vocab)])
    table = tf(table, vocab, file_wordlist)
    table = idf(table)

    return np.array(vocab), np.array(list(file_wordlist.keys())), table

if __name__=='__main__':
    process(
        stopward_file='/mnt/f/python-crawler/projs/douban_books/data/stopword.txt', 
        addrs_file='/mnt/f/python-crawler/projs/douban_books/data/addrs.txt',
    )
