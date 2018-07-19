#!/usr/bin/env python
#-*- coding:utf-8 -*-
# author: Peng Chao


'''
继承：python多继承
两个元则：（针对得是方法）
1.从左到右：当子类继承N个父类的时候，父类中有同样的方法，那么当子类调用父类方法的时候，顺序是从左到右
2.从下到上：	子类继承了多个父类后，子类重写了父类的方法，调用的时候先调用子类的
3.尽量一个类继承两个类，不要继承太多个

父类==基类
子类==派生类



'''
class Person(object):
	def __init__(self,name,age):
		self.name = name
		self.age = age
#子类继承父类
class Xc(Person):
	def __init__(self,name,age,address):
		#子类继承父类属性
	#	Person.__init__(self,name,age)
		super(Xc, self).__init__(name,age)
		self.address = address
	def address(self):
		return self.address
	def info(self):
		print u'姓名：{0},年龄：{1},所在城市:{2}'.format(self.name,self.age,self.address)

class Clover(Person):
	def __init__(self,name,age,work):
		#直接用父类调用属性
		#Person.__init__(self,name,age)
		super(Clover, self).__init__(name,age)
		self.work = work
	def work(self):
		return self.work
	def info(self):
		print u'姓名：{0},年龄：{1},从事的工作:{2}'.format(self.name,self.age,self.work)


x = Xc(u'小超',24,u'成都')
s = Clover(u'王大',42,u'测试工程师')
print x.info()
print s.info()

'''
继承从左到右
	当子类继承N个父类的时候，父类中有同样的方法，那么当子类调用父类方法的时候，顺序是从左到右
从下到上
	子类继承了多个父类后，子类重写了父类的方法，调用的时候先调用子类的
		

'''
class Alax(object):
	def __init__(self,name,age):
		self.name = name
		self.age = age
	def getName(self):
		return self.name
	def setName(self,name):
		self.name = name
	def getAge(self):
		return self.age
	def setAge(self,age):
		self.age = age
	def info(self):
		print u'姓名：{0},年龄：{1}'.format(self.name,self.age)
class Ala(object):
	def __init__(self,name,age,salary):
		self.name = name
		self.age = age
		self.salary = salary
	def getSalary(self):
		return self.salary
	def setSalary(self,salary):
		self.salary = salary
	def info1(self):
		print u'姓名：{0},年龄:{1},工资:{2}'.format(self.name,self.age,self.salary)
#继承两个父类
class Lax(Ala,Alax):
	def __init__(self,name,age,salary,address):
		super(Lax,self).__init__(name,age,salary)
		self.address = address
	def getAddress(self):
		return self.address()
	def setAddress(self,address):
		self.address()
	def info(self):
		print u'姓名：{0},年龄:{1},工资:{2},地点:{3}'.format(self.name,self.age,self.salary,self.address)

so = Lax('AA',21,100,u'成都')
so.info()

