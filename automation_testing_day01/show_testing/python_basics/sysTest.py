#!/usr/bin/env python
#-*- coding:utf-8 -*-
# author: Peng Chao
import os
import sys

# print dir(sys)
# print type(help(sys))
# if sys.argv[0] == 'sleep':
# 	print 'sleep'
# else:
# 	print 'hi'
#
# f=os.path.dirname(__file__)
# print f
#获取python得版本号
print u'获取python得版本号：',sys.version
#获取python运行得平台
print u'获取python当前运行得平台：',sys.platform
#获取python得路径
for item in sys.path:
	print item
'''
模块在项目中能看到，但就是提示不存在
1.liunx环境要特殊处理
2.把项目目录迁移到另外一个目录
3.你下载了别人得代码
处理方式，直接将这个模块加到python->lib目录下面
'''
#获取当前文件得路径
dirs = os.path.dirname(__file__)
print u'当前文件目录：',dirs
#获取当前文件目录的上级目录
dir_order=os.path.dirname(os.path.dirname(__file__))
print u'获取当前文件所在目录的上级目录：',dir_order
#路径拼接
login_order = os.path.join(dir_order,'homework')
print u'路径的拼接：',login_order
#将homework添加到path目录
sys.path.append(login_order)

# for item in sys.path:
# 	print item

