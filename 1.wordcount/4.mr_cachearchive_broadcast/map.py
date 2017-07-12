#!/usr/bin/python
#之前代码是处理一个文件的，而现在的代码是处理多个文件（通过压缩的方式上传）
import os
import sys
import gzip


def get_file_handler(f): #打开相应的文件
    file_in = open(f, 'r')
    return file_in

def get_cachefile_handlers(f): #系统自动解压压缩文件
    f_handlers_list = [] #空列表
    if os.path.isdir(f): #判断f是否为一个目录，即解压完之后的所得到的文件的那个目录
        for fd in os.listdir(f): #对该解压文件的目录进行遍历，该目录中有所有的文件
            f_handlers_list.append(get_file_handler(f + '/' + fd)) #打开遍历后得到的文件，并放入该数组中
    return f_handlers_list #返回该数组，该数组中有所有解压后的文件


def read_local_file_func(f):
    word_set = set() #定义一个集合名字是 word_set
    for cachefile in get_cachefile_handlers(f): #遍历所有压缩文件
        for line in cachefile: #遍历其中一个压缩文件的每一行
            word = line.strip() #每读一行的单词赋值给word
            word_set.add(word) #将单词放到word_set集合里面去
    return word_set #返回word_set的值，此时set结构体里包含了白名单的一些信息


def mapper_func(white_list_fd): #map函数的入口，文件通过参数的形式传入
    word_set = read_local_file_func(white_list_fd) #用函数打开文件，该文件是一个压缩文件

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

