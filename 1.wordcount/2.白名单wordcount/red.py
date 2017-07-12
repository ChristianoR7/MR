#!/usr/bin/python

import sys #import一个系统模块sys

def reduer_func(): #定义函数
    current_word = None #空变量
    count_pool = [] #空列表
    sum = 0 #sum的初值为0

    for line in sys.stdin: #遍历系统输入（此系统输入指的是map的输出，即所有相同的单词相邻的行）
        word, val = line.strip().split('\t') #每一行的前面是word，后面是val，进行srrip处理，word和val的距离是一个tab，python中的'\t'表示一个tab的距离

        if current_word == None: #如果改变量为空
            current_word = word #将word赋值给他

        if current_word != word: #如果变量不等于word，表示前一个word已经遍历完了，下面开始计数
            for count in count_pool:
                sum += count
            print "%s\t%s" % (current_word, sum) #求和，并输出当前单词和他的个数
            current_word = word #将下一个单词赋值给current_word变量
            count_pool = [] #清空列表
            sum = 0 #归零sum

        count_pool.append(int(val))#将val的值加入空的列表中，列表中的形式是[1,1,1,1,1]

    for count in count_pool:
        sum += count
    print "%s\t%s" % (current_word, str(sum))#此三行代码是求最底部的那个单词的个数



if __name__ == "__main__":
    module = sys.modules[__name__]
    func = getattr(module, sys.argv[1])
    args = None
    if len(sys.argv) > 1:
        args = sys.argv[2:]
        func(*args)

