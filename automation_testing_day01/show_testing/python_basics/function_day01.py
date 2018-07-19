#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Peng Chao

'''
1.函数
	函数的定义
	函数形式参数
	函数默认参数
	一个函数，参数有指定了默认次数，但是调用的时候都有实际参数，那么最终结果
	是按实际参数来的
	函数中形式参数与默认参数的混合应用
	函数的返回值
	函数的调用
	函数的参数是函数
	global的应用--函数应用全局变量
'''
def add(a=3,b=7):
	'''指定形式参数的默认参数'''
	print u'指定形式参数的默认参数结果是：',a+b
#调用add方法
add()
'''
函数中形式参数与默认参数的混合应用：
注意：当形式参数与默认参数混合应用的时候，形式参数在前，默认参数在后

'''
def add1(a,b=8):
	print (a*b)
add1(4)#传参给a
'''
函数的返回值
函数的返回值，是为了给另一个函数提供参数而已
'''

def login():
	return 'Thanks your Do'
def myOrder(session):
	if session == 'Thanks your Do':
		print 'login success'
		return True
	else:
		print 'Don\'t login!'
		return False
myOrder(login())