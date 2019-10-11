#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-10-10 20:34:08
# @Author  : 张小浪 (916900730@qq.com)
# @Link    : ${link}
# @Version : $Id$

import os
import unittest
from city_functions import city_functions

class  NameTestcase(unittest.TestCase):
	"""docstring for  NameTestcase"""
	def test_city_country(self):
		fullName = city_functions('tianshui','china')
		self.assertEqual(fullName,'Tianshui, China')

	def test_city_province_country(self):
		fullName = city_functions('tianshui','china','gansu')
		self.assertEqual(fullName,'Tianshui, Gansu, China')

unittest.main()
