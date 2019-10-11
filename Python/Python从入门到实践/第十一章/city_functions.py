#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-10-10 20:28:40
# @Author  : 张小浪 (916900730@qq.com)
# @Link    : ${link}
# @Version : $Id$

import os

def city_functions(city, country, province = ''):
	if province:
		fullName = city + ', ' + province + ', ' + country
	else:
		fullName = city + ', ' + country

	return fullName.title()
