#!/usr/bin/env python
#-*- coding:utf-8 -*-
# author: Peng Chao
from selenium import webdriver
import unittest

class Init(unittest.TestCase):
	def setUp(self):
		self.driver = webdriver.Firefox()
		self.driver.implicitly_wait(30)
		self.driver.maximize_window()
		self.driver.get('http://www.baidu.com')
	def tearDown(self):
		self.driver.quit()
