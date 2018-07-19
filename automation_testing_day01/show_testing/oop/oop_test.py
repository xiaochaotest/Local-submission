#!/usr/bin/env python
#-*- coding:utf-8 -*-
# author: Peng Chao

'''
面向对象的思想不再仅仅是关注持续的逻辑流程，而是软件或者程序中的对象
以及对象之间的关系，使用面向对象的优点是：
1.能够更好的设计软件架构
2.维护软件模块
3.易于架构和组件的重用

6.09日学习内容：
1.类的定义
  新式类
  经典类
2.属性
  类属性
  方法属性
3.方法
 类方法：装饰器@classmethod，属于类
 静态方法：属于类，装饰器@staticmethod
 普通方法：属于类的对象
 特性方法：装饰器@property，不能带参数，它属于类的对象
属于类：
	类方法
	静态方法
	类属性
属于对象：
	普通方法
	特性方法

4.类的继承
  从左到右
  从下到上

#经典类,已经是过去式
class Person():
	pass

面向对象介绍：
  编程是程序员用特定的语法+算法组成的代码告诉计算机如何执行任务的过程
两种最重要的编程范式是面向对象和面向过程编程。还有一种函数式编程
  oop编程是利用类和对象来创建各种模型来实现真实世界的描述。使用oop编程优点：
  1.它可以使程序的维护和扩展变得更简单，提高开发效率
  2.使用oop的程序可以使其他人更加容易理解你的代码逻辑
现实生活中的经验总结：
世界万物，皆可分类
世界万物，皆为对象
只要是对象，就肯定属于某种品类
只要是对象，就肯定有属性
特性（封装，继承，多态）
1.类（class）：一个类即是对一类拥有相同属性的抽象，蓝图，原型。
在类中定义了这些对象都具备属性，共同的方法
2.object对象：一个对象即是一个类的实例化后的实例，一个类必须经过实例化后方可在程序中调用，
一个类可以实例化多个对象，每个对象亦可以有不同的属性，就像人类是指所有人，
每个人指具体的对象，人与人之前有共性，亦有不同
封装（Encapsulation）：在类中对数据的赋值，内部调用对外部用户是透明的，这种类变成一个胶囊或容器，，里面包含着类的数据和方法
继承（Inheritance）：一个类可以逐生出子类，在这个父类里定义的属性，方法自动被子类继承
多态：多态是面向对象的重要特性，一个接口，多种实现

语法
属性
方法
构造函数
析构函数

私有方法，私有属性
类变量
实例变量

__dict__:类的属性（包含一个字典，由类的数据属性组成）
__doc__:类的文档字符串
__name__:类名
__moudule__:类定义所在的模块（类的全名是'__main__.className',
如果类位于一个导入模块mymod中，那么className.__module__等于mymod)
__bases__:类的所有父类构成元素（包含了一个由所有父类组成的元组）




'''
#新式类，任何类都继承与它的顶级类（object），所有的类都是它的子类
# class PersonSun(object):
# 	'''
# 	1.类的构造方法,所有下划线都是内置方法
# 	2.构造函数写不写构造函数，都会有构造函数
# 	3.类实例化的时候，如果构造函数有参数，一定要对参数进行赋值
# 	'''
# 	'''定义一个类的时候要注释类的用途'''
# 	def __init__(self,name,age):
# 		self.name = name
# 		self.age = age
# 	'''获取name'''
# 	def getName(self):
# 		return self.name
# 	'''设置name'''
# 	def setName(self,name):
# 		self.name = name
# 	'''获取age'''
# 	def getAge(self):
# 		return self.age
# 	'''设置age'''
# 	def setAge(self,age):
# 		self.age = age
# #类的实例化
# per = PersonSun('xiaochao',22)
# print per.getName()
# print per.getAge()
#
# per.setAge(21)
# per.setName("admin")
# print per.getName()
# print per.getAge()
# # __doc__讲述类是干什么的(说明文档）
# #print PersonSun.__doc__
#
#
# from selenium import webdriver
# import time as t
# class BaiduTest(object):
# 	def __init__(self):
# 		self.driver = webdriver.Firefox()
# 		self.driver.maximize_window()
# 		self.driver.implicitly_wait(30)
# 		self.driver.get('http://www.baidu.com')
# 		#析构函数：当使用del删除对象时，会调用他本身的析构函数，当对象在某个作用域中调用完毕，
# 	#再跳出其作用域的同时析构函数也会被调用一次，这样可以用来释放内存空间
# 	def __del__(self):
# 		self.driver.quit()
# 	def so(self):
# 		self.driver.find_element_by_id('kw').send_keys('selenium')
# 		t.sleep(5)
# p=BaiduTest()
# p.so()

class Psoin(object):
	#类属性，属于类以及类的对象，直接使用类名或对象名调用
	gj = u'中国'

	def __init__(self,name,age,salary):
		print u'start开始'
		self.name = name
		self.age = age
		self.salary = salary
	def getName(self):
		#方法的属性
		xc = 'xiaochao'
		print xc
		return self.name
	def setName(self,name):
		self.name = name
	def getAge(self):
		return self.age
	def setAge(self,age):
		self.age = age
	def getSalary(self):
		return self.salary
	def setSalary(self,salary):
		self.salary = salary
	def __del__(self):
		print u'pass结束，析构函数，释放内存,在对象消逝的时候被调用'

	#私有方法
	def __show(self):
		print u'这是一个类的私有方法，不能被外界调用'
	#调用私有方法的写法
	def show(self):
		self.__show()
		#普通方法
	def info(self):
		return u'国家:{0},姓名：{1},年龄：{2},工资{3}'.format(self.gj,self.name,self.age,self.salary)
	#特性方法
	@property
	def info(self):
		print u'"特性方法：",国家:{0},姓名：{1},年龄：{2},工资{3}'.format(self.gj,self.name,self.age,self.salary)
	#静态方法
	@staticmethod
	def show():
		print u'这是一个镜态方法'
	#类方法
	@classmethod
	def show1(cls):
		print u'这是一个类方法'
d = Psoin("AA",24,432)
name1 = d.setName("pythonTesting")
age1 = d.setAge(22)
salary = d.setSalary(9000)

print d.getName()
print d.info
print u'调用私有方法：',d.show()
#一般使用类名调用静态方法
Psoin.show()
#直接使用类名调用类方法
Psoin.show1()