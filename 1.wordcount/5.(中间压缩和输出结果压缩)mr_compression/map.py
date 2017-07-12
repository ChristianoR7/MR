#!/usr/bin/python

import os
import sys
import gzip


def get_file_handler(f):
    file_in = open(f, 'r')
    return file_in

def get_cachefile_handlers(f):
    f_handlers_list = [] #空列表
    if os.path.isdir(f): # #判断f是否为一个目录，即解压完之后的所得到的文件的那个目录
        for fd in os.listdir(f): #遍历该目录中的所有文件
            f_handlers_list.append(get_file_handler(f + '/' + fd)) #将文件打开并读然后放入列表中
    return f_handlers_list #返回列表


def read_local_file_func(f):
    word_set = set()
    for cachefile in get_cachefile_handlers(f): #遍历所有的压缩文件
        for line in cachefile: #遍历某一个压缩文件
            word = line.strip()
            word_set.add(word)
    return word_set


def mapper_func(white_list_fd):
    word_set = read_local_file_func(white_list_fd)

    for line in sys.stdin:
        ss = line.strip().split(' ')
        for s in ss:
            word = s.strip()
            if word != "" and (word in word_set):
                print "%s\t%s" % (s, 1)



if __name__ == "__main__":
    module = sys.modules[__name__]
    func = getattr(module, sys.argv[1])
    args = None
    if len(sys.argv) > 1:
        args = sys.argv[2:]
    func(*args)

