#!/usr/bin/env python
#-*- coding:utf-8 -*-
# author: Peng Chao
class Dog(object):
	def __init__(self,name):
		self.name = name
	def bulk(self):
		print('%s:wangwang...'%self.name)

d1 = Dog('小张')
d1.bulk()