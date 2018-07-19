#!/usr/bin/env python
#-*- coding:utf-8 -*-
# author: Peng Chao
import os
import selenium
# print dir(os)
# print type(help(os))

# print u'获取当前文件的路径(方式一)',os.getcwd()
# print u'获取当前文件的路径（方式二）',os.path.dirname(__file__)
# print u'获取当前目录的上一级路径',os.path.dirname(os.path.dirname(__file__))
#获取当前文件的上级路径
base_dir = os.path.dirname(os.path.dirname(__file__))
print '获取当前文件目录的上级目录：',base_dir
# print os.path.join(base_dir,'fou','log')
#打开fou目录下的log文件
f=open(os.path.join(base_dir,'fou','log'),'r')
#读取log文件的内容
print f.read()

s=open(os.path.join(base_dir,'fou','fort'),'r')
print '读取fou目录下的fort文件中的内容:',s.read()

#system括号里的内容相当于命令行里的命令
# print os.system('ping -t 192.168.0.11')
#mkdir()创建文件夹
# print os.mkdir('c:/log')
