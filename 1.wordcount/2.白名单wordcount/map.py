#!/usr/bin/python

import sys


def read_local_file_func(f):#该函数的作用就是打开白名单里面的单词，并且将其放入集合word_set中去
    word_set = set() #定义一个集合名字是 word_set
    file_in = open(f, 'r') #打开文件并开始读文件,'r'是读模式
    for line in file_in: #循环打开的这个文件
        word = line.strip() #每读一行是一个单词，并对其进行头尾符号处理，Python strip() 方法用于移除字符串头尾指定的字符（默认为空格）。
        word_set.add(word) #将单词放到word_set集合里面去
    return word_set #返回word_set的值，此时set结构体里包含了白名单的一些信息


def mapper_func(white_list_fd):
    word_set = read_local_file_func(white_list_fd)

    for line in sys.stdin: #从标准输入读数据，通过循环的方式，每次从标准输入读数据
        ss = line.strip().split(' ') #line.strip表示对格式的头尾进行处理（发现隐藏的符号），然后split对每行单词用空格进行分割，这样这个单词就变成了一个数组ss
        for s in ss: #对该数组进行遍历，这样s就是每一个单词
            word = s.strip()
            if word != "" and (word in word_set): #单词非空且在白名单里面
                print "%s\t%s" % (s, 1) #输出白名单里面的word，其他不在白名单中的单词并不会输出



if __name__ == "__main__": #程序的开端，这几行相当于框架
    module = sys.modules[__name__]
    func = getattr(module, sys.argv[1])
    args = None
    if len(sys.argv) > 1:
        args = sys.argv[2:]
    func(*args)

