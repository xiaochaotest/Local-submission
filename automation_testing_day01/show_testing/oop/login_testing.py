#!/usr/bin/env python
#-*- coding:utf-8 -*-
# author: Peng Chao
from selenium import webdriver
import unittest
from initTesting import Init
class Login(Init):
	def test_info(self):
		pass

if __name__ == '__main__':
	unittest.main(verbosity=2)