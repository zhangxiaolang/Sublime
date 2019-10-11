#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-10-10 21:07:19
# @Author  : 张小浪 (916900730@qq.com)
# @Link    : ${link}
# @Version : $Id$

import os
import unittest
from Employee import Employee

class TestEmployee(unittest.TestCase):
	"""docstring for TestEmployee"""
	#setup函数建立默认实例化内容，避免重复实例化浪费资源。
	def setUp(self):
		self.employeea = Employee('slade',5000)

	def test_give_default_raise(self):
		salary1 = self.employeea.give_default_raise()
		self.assertEqual(salary1,10000)

	def test_give_custom_raise(self):
		salary2 = self.employeea.give_custom_raise(1000)
		self.assertEqual(salary2,6000)

unittest.main()
