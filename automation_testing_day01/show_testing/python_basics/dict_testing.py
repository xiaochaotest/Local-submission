#!/usr/bin/env python
#-*- coding:utf-8 -*-
# author: Peng Chao
dict1 = {'name':'xiaochao','age':24,'address':'chengdu','data':{'id':21,'salary':8000}}
print u'查看字典所具备得功能：',dir(dict1)
print u'查看字典详细的帮助信息：',type(help(dict1))
'''
获取字典中指定的value值
'''
print u'获取name对应的vaule值：\n',dict1['name']
'''获取id对应得valus'''
print dict1['data']['salary']


'''
循环打印字典里的元素，默认循环，打印的是key
'''
for s in dict1:
	print u'循环打印字典里的元素，默认循环，打印的是key值：',s
'''
循环打印字典中的所有值
'''
for key,value in dict1.items():
	print key,":",value

'''
获取字典中所有的key值（注意获取后成一个列表）
'''
print u'获取字典所有的key值：',dict1.keys(),type(dict1.keys())
'''
获取字典中所有的value值（注意获取后成一个列表)
'''
print u'获取字典所有的value值：',dict1.values(),type(dict1.values())
'''
获取字典中所有的键值对
'''
print u'获取字典中所有的键值对：',dict1.items(),type(dict1.items())
'''
判断键值是否在字典中
'''
print u'判断name是否在dict1字典中：',dict1.has_key('name')
'''
利用字典的key生成新的字典
'''
print u'使用fromkeys方法生成新的字典：',dict1.fromkeys(['name','age'],('xiaochao',22)),type(dict1.fromkeys(['name','age',('xiaochao',22)]))

#对字典的内容进行更新
dict1['name'] = u'章额'
print u'更新后字典的内容：',dict1
#在python中，列表元组字典字符串是可以相互转换的
#list列表的转换
list1 = ['name','age','addres']
print u'把列表list1转换为字符串：',str(list1),u'类型为：',type(str(list1))
str = 'xiaochao name sex age'
print u'把字符串str转换为列表：',str.split(' '),u'类型为：',type(str.split(' '))
print u'把列表list1转换为字典：',tuple(list1),u'类型为：',type(tuple(list1))
print u'把列表list1转换为元组：',dict(enumerate(list1)),u'类型为：',type(dict(enumerate(list1)))
#元组的转换
tuple2 = ('android','ios','windows','firfoxos')
print u'把元组tuple2转换为列表：',list(tuple2),u'类型为：',type(list(tuple2))

#print u'把元组tuple2转换为字符串：',str(tuple2),u'类型为：',type(str(tuple2))无法将元组直接转换为字符串
#字典的转换
dicts = {'name':'xiaochao','age':12,'salary':8000}
print u'把字典dicts转换为列表：',list(dicts.items()),u'类型为：',type(dicts.items())
