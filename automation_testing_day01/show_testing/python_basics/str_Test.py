#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Peng Chao
import selenium
import sys
'''
1.str的操作
2.元组，列表，字典的操作
'''

'''
在单引号里面又包含了单引号的处理
'''
name1 = u'xiaochao,"你好"，\'你在成都好吗？\''
print name1
def add():
	'''
	None
	:return:
	'''
name = u'小超'
age = 24
address = u'成都'
print u'我在%s,今年我%s岁，我的名字是%s'%(address,age,name)
print u'我今年{1}岁了，我叫{0}，在四川{2}'.format(name,age,address)
print u'我叫{name},我今年{age}岁了，我在{address}'.format(name=name,age=age,address=address)
'''字符串和unicode类型互转'''
str1 = 'hello'
print u'现在的类型是：',type(str1)
#字符串转为unicode用decode()
str2 = str1.decode('gbk')
print u'str2的类型是：',type(str2)
#unicode类型转为str
str3 = str2.encode('utf-8')
print u'str3的类型是：',type(str3)
#将字符串转成int类型
src = '45'
src1 = int(src)#浮点类型float(src)
print u'将字符串强转为int类型：',type(src1)

'''字符串的操作'''
cont = 'hell word'
print u'获取w在字符串中是第几位：',cont.index('w')#索引均是从0开始
print cont.index('l')
print u'将字符串转成大写：',cont.upper()
cont.upper()
print u'取消字符串中的空格：',cont.strip()
cont.strip()
print u'判断字符串是否是数字：',cont.isdigit()
cont.isdigit()
print u'判断字符串是否是以h开头：',cont.startswith('h')
cont.startswith('h')
print u'判断字符串是否是以d结尾：',cont.endswith('d')
#cont.endswith()
print u'寻找字符串中的元素：',cont.find('o')
cont.find('s')
print u'替换字符串中的元素：',cont.replace('word','China')
cont.replace('word','name')
print u'字符串的拆分：',cont.split(' ')#字符串拆分处理以后就是列表
cont.split(' ')
print u'首字母变大写：',cont.capitalize()
cont.capitalize()
print u'内容居中：',cont.center(30,'=')
#cont.center(30,'==')
cont1 = 'Hello\t999'
print u'处理table键：',cont1.expandtabs()
print u'是否是字母和数字：',cont.isalnum()
print u'是否是字母：',cont.isalpha()
print u'判断是否是数字：',cont.isdigit()
print u'是否小写：',cont.islower()
print u'是否有空格：',cont.isspace()
print u'是否是大写：',cont.isupper()
#判断标题-->首字母大写，可以理解为大写
print u'首字母是否大写:',cont.istitle()
#join连接字符串
s1 = ['appium','selenium','android','ios']
print '连接字符串:', '***'.join(s1)
#使用.join（）把列表转为字符串
print '把列表转成字符串：',','.join(s1)
#字符串转为列表
a = 'a b c'
print a.split(" ")
#移除空白
a1 = '  abc'
print '移除空白:',a1.lstrip()
#移除左侧空白
print '移除左侧空白：',a1.lstrip()
#移除右侧空白
st = 'hell   '
print '移除右侧空白：',st.rstrip()
#字符串转小写
print cont.lower()
#分割字符串，分割之后就是元组
ss1 = 'xiaochao is python'
print u'分割字符串，分割之后就是元组：',ss1.partition('is')
#替换字符串
print u'替换字符串：',ss1.replace("xiaochao",'admin')
#rfind()从右向左找
print ss1.find('xiaochao')

#bytes可以将字符串转换成字节
# strs1 = u'小超'
# print u'字符串转成字节：',strs1.bytes(strs1)

print '****列表的操作*****'
'''
字符串中内置的数据类型
元组：tuple
列表：list
字典：dict
'''
list1 = [10,24,5,31,0,9]
print u'打印列表：',list1
# print dir(list1)#通过dir方法查看内置了哪些方法
# print type(help(list1))#help()帮助信息
u'''实现列表的追加'''
list1.append(28)
print list1
#实现把想要插入的数据放到想要的位置
print u'查看0在列表中出现了几次：',list1.count(0)
print u'查看元素在列表中是第几位：',list1.index(5)
print u'查看列表中第6位元素是什么：',list1[6]
#查看列表中的所有内容
for s in list1:
	print u'查看列表中所有的元素内容：', s
#依据位置插入元素
list1.insert(3,'dont')
#删除指定的列表元素
list1.remove('dont')
#修改列表中的内容
list1[0]='android'
print u'查看更新后的列表内容：',list1
#扩展列表
list2 = ['a','b','c,','d']
list1.extend(list2)
print u'查看扩展以后的列表内容：',list1
#列表反转
list1.reverse()
#列表的排序
list1.sort()
#删除指定位置的列表
del list1[0]

'''
pop()默认删除最后一位并且把删除的元素打印出来
'''
list2 = [11,51,21,4,'g',47,1,0,99]
print list2.pop(1)
'''
remove()删除想要删除的元素
'''
list2.remove('g')
print list2

'''
reverse()字符串反转
'''
list2.reverse()
print list2
'''
sort()列表中的元素按从小到大排序
'''
list2.sort()
print list2

print u'****元组*****'
'''
元组
1.元组是不可变的
2.元组中的数据是可变的；元组中通常代表一行数据，而元组中的数据代表不同的数据项
'''
tuple1 = (15,2,50,'abc',["username","password"],{"name":"xiaochao"})
print u'获取元素在元组中出现了几次:',tuple1.count(50)
print u'获取元素在元组中的索引：',tuple1.index(50)
'''
把元组中name对应的小超改为小超
'''
tru = 'admin'
tuple1[5]['name'] = tru
print tuple1

#取出元组中具体的值
print u'取出元组中具体的值：',tuple1[3]

#取出元组最后一位元素
print u'取出元组中最后一个元素的值：',tuple1[len(tuple1)-1]
#切片在元组中的使用
print u'切片在元组中的使用：',tuple1[0:4]
#使用循环的方式，取出元组中所有的值
for item in tuple1:
	print u'循环获取元组中的所有值：', item
#获取元组中的某个元素在元组中的个数
print u'获取元组中某个元素的个数：',tuple1.count('xiaochao')
#修改元组嵌套在元组中的列表内容
print u'元组中的内容：', tuple1
tuple1[5]['username']='admin'
print u'元组中的字典被修改后的内容L：',tuple1,u'类型为：',type(tuple1)
#5.24日到元组