#!/usr/bin/env python
#-*- coding:utf-8 -*-
# author: Peng Chao
'''
set集合
set集合是一个无序并且不重复的元素集合，他的关键字是set
依照之前的思维方式，我们定义一个set集合，来看他的类所具备的功能以及对象功能的详细信息，这样的目的很简单，很多时候我们不可能把字典，列表，元组，set集合类的方法都记得那么清楚，但是使用的时候，我们可以通过dir()
和help()来获取他的详细信息，来实现所要实现的东西
'''
s = set()
# print u'set对象类的功能为：',dir(s)
# print u'set对象的详细信息：',help(type(s))
#集合插入数据
s.add('xiaochao')
print u'插入数据后集合的内容：',s,type(s)
#把列表转换为集合
list1 = [11,21,51,45,36,4]
print u'列表list1转换为集合后：',set(list1),type(set(list1))
#查看b集合存在，a集合不存在的情况
b = {1,2,25,36,6}
a = {5,87,9,1,88}
print u'查看b集合存在，a集合不存在的内容：',b.difference(a)
print u'移除指定的集合,不存在不会出现错误:',b.discard('xiaochao')
print u'查看集合a，b都存在的值：',a.intersection(b)
#没有交集，返回true，存在交集返回false
print u'判断集合a，b是否存在交集：',a.isdisjoint(b)
print u'移除集合的元素并且获取值：',a.pop()
print u'获取a，b集合的并集:',a.union(b)
b.update(a)
print u'集合b更新后的内容为：',b
