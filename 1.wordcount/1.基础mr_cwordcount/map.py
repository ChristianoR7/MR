#!/usr/local/bin/python

import sys #import一个系统模块，这个系统模块有.stdin方法

for line in sys.stdin: #从标准输入读数据，通过循环的方式，每次从标准输入读数据
	ss = line.strip().split(' ') #line.strip表示对格式的头尾进行处理（发现隐藏的符号），然后split对每行单词用空格进行分割，这样这个单词就变成了一个数组ss
	for s in ss: #对该数组进行遍历，这样s就是每一个单词
		if s.strip() != "":#如果这个单词不为空，为有效单词
			print "%s\t%s" % (s, 1)#见到一个单词追加一个1，/t是分隔符，然后打印出来
