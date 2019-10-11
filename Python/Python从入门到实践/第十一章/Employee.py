#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-10-10 21:01:32
# @Author  : 张小浪 (916900730@qq.com)
# @Link    : ${link}
# @Version : $Id$

import os
class Employee(object):
	"""docstring for Employee"""

	def __init__(self, name, salary):
		self.name = name
		self.salary = salary

	def give_default_raise(self):
		self.salary += 5000
		return self.salary

	def give_custom_raise(self, custom_salary):
		self.salary += custom_salary
		return self.salary
		