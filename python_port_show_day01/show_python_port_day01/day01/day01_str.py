#!/usr/bin/env python
#-*- coding:utf-8 -*-
# author: Peng Chao
'''
dict和list不同点：
dict：
1.查找和插入的速度极快，不会随意随着key的增加而变慢
2.需要占用大量的内存，内存浪费多
list：
1.查找和插入的时间随着元素的增加而增加
2.占用空间小，浪费内存很少
dict用空间来换取时间

'''

#再单引号里面又包含了单引号的处理
# name = 'xiaochao,"url",\'Good\''
# print name
# #使用双引号
# name1 = "xiaochao,'beudrun"
# print u'使用双引号：',name1
# #使用三引号
# name2 = '''xioachao'''
# print u'使用三引号：',name2
'''
Ctrl+/:注释
'''
# name = 'xiaochao'
# age = 23
# address = u'成都'
# print u'我的名字是:{0},年龄:{1}，城市:{2}'.format(name,age,address)
# print u'我的名字是：{name},年龄是：{age},所在城市是：{address}'.format(name=name,age=age,address=address)
# print u'我的名字是:%s,我年龄：%s,我在：%s'%(name,age,address)
#
# u'''unicode如何转换成字符串类型'''
# str1 = u'小超'
# print type(str1)
# str2 = str1.encode('utf-8')
# print type(str2)
# u'''字符串转换成unicode类型'''
# str3 = 'hello word'
# print type(str3)
# str4 = str3.decode('gbk')
# print type(str4)
# int1 = '23'
# print type(int1)
# int2 = int(int1)
# print u'字符串强转为int类型',int2
# print type(int2)
# u'''字符串强转为float类型'''
# int3 = '23.41'
# print type(int3)
# int4 = float(int3)
# print type(int4)
# usr = 'hello word'
# u'''获取o在字符串中是第几位'''
# print u'获取o在字符串中是第几位',usr.index('o')
# print u'把字符串转成大写',usr.upper()
# print u'取消字符串的空格',usr.strip()
# print u'判断字符串中是否是数字',usr.isdigit()
# print u'判断字符是否是以字母h开头',usr.startswith('h')
# print u'判断字符串是否以字母d结尾',usr.endswith('d')
# print u'字符串寻找',usr.find('o')
# print u'字符串替换',usr.replace('word','xiaochao')
# print u'字符串拆分',usr.split(' ')
# u'''内置的数据类型：tuple：元组 list：列表 dict：字典'''
# list1 = [1,32,31,12,3,19,23]
# print dir(list1)#dir()查看内置方法
# print type(help(list1))#help()帮助
# '''append()实现列表的追加'''
# list1.append(24)
# print list1
# '''insert(x,x)实现想要插入的数据放到想要的位置'''
# list1.insert(5,14)
# print list1
# '''count()测试某元素在列表中出现了几次'''
# print list1.count(12)
# '''index()查看元素在列表中是第几位'''
# print list1.index(12)
# '''list[x]查看列表中第几位上的元素是什么'''
# print list1[4]
# '''pop()删除最后一位元素并打印出来'''
# print list1.pop()
# print list1
# '''remove()删除想要删除的元素'''
# list1.remove(23)
# print list1
# list2 = [1,3,4,6,6,12,42,14,41,23,25]
# '''reverse()反转'''
# list2.reverse()
# print list2
# '''sort()列表中的元素按数字从小到大的顺序排序'''
# list2.sort()
# print list2
'''元组
1.元组是不可变的
2.元组中的数据是可变的，元组通常代表一行数据，而元组中的数据代表不同的数据项
'''
# tuple1 = (1,11,12,23,25,53,23,["name",'age'],{'name':'xiaochao'})
# '''count()获取在元组中出现了几次'''
# print tuple1.count(23)
# #print tuple1
# '''index()获取元素在元组中的索引'''
# print tuple1.index(12)
# '''修改元组中的元素'''
# tuple1[8]['name']='admin'
# print tuple1
# print 2<1 or 2>1#or是或运算，只要其中有一个为true结果就是true
# print 2>1 and 4>9#and是与运算，只有所有的都为true结果才为true
# print not 3>5#not运算是非运算，把true变成false，false变为true
# print None#空值，不能理解为0，它是特殊得空值
# user = 'what is yong'
# print user.__len__()#查看字符串长度
# listUser = [1,'de',23]
# print len(listUser)
# '''if条件判断'''
# age = 12
# if age >= 18:
# 	print u'成年人'
# else:
# 	print u'未成年'
#
# if age >= 18:
# 	print u'your age is:',age
# elif age <= 18:
# 	print u'your age is:',age
# else:
# 	print u'not age'
#
# '''
# 需求：
# 小明身高1.75，体重80.5kg
# 用BMI公式（体重除以身高的平方），算出小明的BMI指数
# '''
# height = 1.75
# weight = 80.5
# bmi = weight/(height*height)
# if bmi > 18.5:
# 	print u'过轻'
# elif 25>bmi > 18.5:
# 	print u'正常'
# elif 28 >bmi> 28:
# 	print u'过重'
# elif 32 >bmi> 28:
# 	print u'肥胖'
# else:
# 	print u'严重肥胖'
#
# '''循环'''
# names = ['job','Tom','arrsmy','xiaochao','admin']
# for name in names:
# 	print u'循环打印names列表中的元素：\n',name
#
# 	sum = 0
# 	for a in [1,2,5,4,7,8,9,100]:
# 		sum += a
# 	print sum
#
# 	list = (range(100))
# 	for x in list:
# 		sum += x
# 	print u'累加结果是：',sum
#
# 	'''wile循环'''
# 	sum1 = 0
# 	n = 99
# 	while n > 0:
# 		sum1 += n
# 		n = n-2
# 	print sum1
#
# 	L = ['Bart','Lisa','Adam']
# 	for a in L:
# 		print a
#
# count = 1
# while count <= 100:
# 	if count > 10:
# 		break#跳出循环
# 	print count
# 	count += 1
# print u'退出了循环'

'''
continue跳出当前这次循环
'''
# d = 0
# while d < 10:
# 	d += 1
# 	if d % 2 == 0:
# 		continue
# 	print d
'''dictionary字典'''
#列表
list1 = [1,'d',42,'fes',90,'dew']
#字典
d = {'Michae':'24','Tom':'12','Tracy':'10'}
print d['Tom']
d['salary'] = 7500
print d
print 'Tom' in d#判断Tom是否存在
print d.get('tom',-1)
