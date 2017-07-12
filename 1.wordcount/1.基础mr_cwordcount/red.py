#!/usr/local/bin/python

import sys

current_word = None #设置一个none的变量
count_pool = [] #一个空列sum = 0 #求和sum的初值为0

for line in sys.stdin: #从标准输入读数据，这个标准输入指的是map之后按序排，前面是关键字，后面是值的数据，相同的词在一块
	word, val = line.strip().split('\t') #每读一行句子，对其进行分割

	if current_word == None: #这条语句只在第一次时起作用
		current_word = word  #遍历相同的单词

	if current_word != word:#若遍历到这一个不是之前的单词，就将之前所有的单词的计数相加，完成一个单词的统计
		for count in count_pool:
			sum += count
		print "%s\t%s" % (current_word, sum)#当前单词完成数量统计
		current_word = word #指针指向下一个需要统计的单词
		count_pool = [] #列表重新定位空
		sum = 0 #求和从新定为0

	count_pool.append(int(val))#若是相同的单词，每次把val的值放入初始为空的数组当中

for count in count_pool:#这是底部的数据求和的一段代码，如果不加这几行，底部的那个单词的统计就丢失了
	sum += count
print "%s\t%s" % (current_word, str(sum))

