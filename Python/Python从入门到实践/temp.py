#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-10-10 19:42:33
# @Author  : 张小浪 (916900730@qq.com)
# @Link    : ${link}
# @Version : $Id$

import os
import json


file_name = '123\\user_name.json'

def login_on():
	names = []
	j = 1
	while(j):
		name = input('请输入您的姓名：')
		names.append(name)
		judge = input('您是否继续输入（Y/N）：')
		if judge == 'N' or judge == 'n':
			break

	#print(names)

	with open(file_name, 'w') as write_user:
		json.dump(names, write_user)


def say_hello():
	with open(file_name) as read_user:
		users = json.load(read_user)
		for i in users:
			print('hi {0},welcome to python world.'.format(i))

login_on()
say_hello()