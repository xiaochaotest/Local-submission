#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Peng Chao
'''
1.注册，将注册的信息写入txt文件中
2.登陆，读取txt中的注册信息，符合就登陆成功


'''
import sys
def name():
	'''获取用户的用户名'''
	username = raw_input('请输入你的用户名：')
	return username
def password():
	'''获取用户的登陆密码'''
	password = raw_input('请输入你的登陆密码：')
	return password
#注册.把用户输入的注册信息存到test.txt文件中
def register(username,password):
	temp = username+'|'+password
	'''把注册的用户名和密码写入test.txt文件'''
	with open('test.txt','w') as f:
		f.write(temp)
#用户登陆系统
def login():
	f = open('test.txt','r')
	#print f.read(),type(f.read())
	list1 = f.read().split('|')
	username = raw_input('请输入用户名：\n')
	password = raw_input('请输入登陆密码：\n')
	if username == list1[0] and password == list1[1]:
		#print u'登陆成功'
		return True
	else:
		#print u'登陆失败'
		return False

#打印出登陆成功的信息
def getUserInfo():
	f = open('test.txt','r')
	list1 = f.read().split('|')
	return u'恭喜{0},成功登陆系统'.format(list1[0])
#'''退出系统'''
def exit():
	sys.exit(1)

if __name__ == '__main__':
	while True:
		t = int(raw_input('1.注册，2.登陆，3.退出系统\n'))
		if t == 1:
			register(name(),password())
		elif t == 2:
			s = login()
			if s == True:
				print getUserInfo()
			else:
				print '登陆失败！'
		elif t == 3:
			exit()
		else:
			break
