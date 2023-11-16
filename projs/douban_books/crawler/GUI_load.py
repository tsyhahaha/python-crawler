# _*_ coding: utf-8 _*_
import re
import os
import json
from PySide2.QtWidgets import QApplication
from PySide2.QtUiTools import QUiLoader
import numpy as np
import jieba
import hashlib

from process import process


House = [None]*10000

class Node(object):
    def __init__(self, hashnum, key, value):
        self.next = None
        self.element = [hashnum, key, value]

    def addnext(self, node):
        self.next = node


def text(addr):
    if os.path.exists(addr):
        with open(addr, 'r', encoding='utf-8') as file:
            content = file.read()
            if len(content) == 0:
                return 'no more infomation'
            else:
                dic = json.loads(content)
                text = dic['author'] + ' ' + dic['publish'] + ' ' + dic['time'] + '\n' + dic['brief']
                return text
    else:
        return addr


def Hash(key):
    m = hashlib.md5()
    m.update(key.encode('utf-8'))
    hex_num = m.hexdigest()
    sum = str(bin(int(hex_num, 16)))[-13:]
    return str(hex_num), int(sum, 2)


def find(filename):
    hashnum, index = Hash(filename)
    cur = House[index]
    if cur is not None:
        while cur.element[0] != str(hashnum):
            cur = cur.next
            if cur is None:
                return 'no more comprehensive infomation!'
        return cur.element[2]
    else:
        return 'no more comprehensive infomation!'


def store(key, addr):
    if addr is None:
        return
    else:
        hashnum, index = Hash(key)
        node = Node(hashnum, key, addr)
        if House[index] is None:
            House[index] = node
        else:
            cur = House[index]
            while cur.next is not None:
                cur = cur.next
            cur.next = node
    return index, node.element


def pro(lst):
    aim = []
    for item in lst:
        if item not in aim:
            aim.append(item)
    return aim


def search(words, vocab, filename, table):
    result_pre = {}
    result = []
    result_t1 = []
    for i in range(len(filename)):
        result_pre[filename[i]] = 0
    for word in words:
        for name in filename:
            if word in name:
                result_t1.append((name, text(find(name))))
        try:
            x = vocab.index(word)
        except:
            x = None
        if x:
            filepoints = table[:, x]
            for j in range(len(filepoints)):
                result_pre[filename[j]] += filepoints[j]
    for item in sorted(result_pre.items(), key=lambda x: x[1]):
        if item[1] != 0:
            result.append((item[0], text(find(item[0]))))  # 返回排好序的filename
        else:
            break
    for item in result:
        if item in result_t1:
            result.remove(item)
    result_t1.reverse()
    for item in result_t1:
        result.insert(0, item)
    for i in range(1, len(result)-1):
        if result[-i] == result[-i-1]:
            result.pop(-i)
    return pro(result)


class Stats:
    def __init__(self, vocab=None, filename=None, table=None):
        # 从文件中加载UI定义

        # 从 UI 定义中动态 创建一个相应的窗口对象
        # 注意：里面的控件对象也成为窗口对象的属性了
        # 比如 self.ui.button , self.ui.textEdit
        self.ui = QUiLoader().load('GUI.ui')
        self.ui.searchButton.clicked.connect(self.handleCalc)
        self.vocab = vocab
        self.filename = filename
        self.table = table

    def handleCalc(self):
        info = self.ui.wordsget.toPlainText()
        pattern = re.compile(r'[\u4e00-\u9fa5]+')
        words = ''.join(re.findall(pattern, info))
        word_list = jieba.lcut_for_search(words)
        result = search(word_list, vocab=self.vocab, filename=self.filename, table=self.table)
        try:
            self.ui.result.clear()
            rank = 0
            for item in result:
                self.ui.result.append('{0}.'.format(rank) + str(item[0])+'\n\t'+str(item[1])+'\n')
                rank += 1
            self.ui.result.append('add more words to find enough infomation~~~')
        except:
            self.ui.result.append('Failed search~~~\nPlease change the words')

def load_app(addrs_file, vocab, filename, table):
    a = open(addrs_file, 'r', encoding='utf-8')
    addrs = a.readlines()
    for line in addrs:
        line = line.replace('\n', '').split(' ')
        name = line[0]
        addr = line[1]
        if os.path.exists(addr):
            if os.path.getsize(addr) == 0 and os.path.exists("a.txt"):
                os.remove(addr)
            else:
                store(name, addr)

    app = QApplication([])
    stats = Stats(vocab, filename, table)
    stats.ui.show()
    app.exec_()

    
if __name__=='__main__':
    # vocab = np.load('vocab.npy', allow_pickle=True).tolist()
    # filename = np.load('filekeys.npy', allow_pickle=True).tolist()
    # table = np.load('TFIDF-table.npy', allow_pickle=True)
    vocab, filename, table = process(
        stopward_file='/mnt/f/python-crawler/projs/douban_books/data/stopword.txt', 
        addrs_file='/mnt/f/python-crawler/projs/douban_books/data/addrs.txt',
    )
    load_app(
        '/mnt/f/python-crawler/projs/douban_books/data/addrs.txt',
        vocab, filename, table
    )
