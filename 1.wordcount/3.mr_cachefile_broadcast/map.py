#!/usr/bin/python

import sys


def read_local_file_func(f): #定义一个名字为read_local_file_func的函数
    word_set = set() #定义一个集合名为word_set
    file_in = open(f, 'r')#打开文件f，并且开始读
    for line in file_in: #遍历该文件
        word = line.strip() #将每一行进行strip处理并赋值给word
        word_set.add(word) #将处理后的word添加到word_set集合中去
    return word_set #返回word_set的值


def mapper_func(white_list_fd):#定义一个名字为mapper_func的函数，传入的参数是white_list_fd
    word_set = read_local_file_func(white_list_fd)#调用read_local_file_func函数，并将其返回的值给集合word_set

    for line in sys.stdin: #遍历从标准输入输出的数据
        ss = line.strip().split(' ') #对每一行进行strip处理并用空格分隔，然后赋值给元组ss
        for s in ss: #遍历该元组ss
            word = s.strip() #将每一个单词进行strip处理并赋值给word
            if word != "" and (word in word_set): #如果单词非空且与word_set中(即白名单中)的单词一致
                print "%s\t%s" % (s, 1) #输出该单词，并在他后面计数为1



if __name__ == "__main__":
    module = sys.modules[__name__]
    func = getattr(module, sys.argv[1])
    args = None
    if len(sys.argv) > 1:
        args = sys.argv[2:]
    func(*args)

