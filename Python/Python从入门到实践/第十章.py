#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-10-10 19:08:00
# @Author  : 张小浪 (916900730@qq.com)
# @Link    : ${link}
# @Version : $Id$

#1,存储文件并读取
import os
import json

file_name = '123\\user_name.json'

def get_stored_username():
	try:
		with open(file_name) as f_obj:
			users = json.load(f_obj)

	except FileNotFoundError:
		return None

	else:
		return users


def login_on():
	names = []
	j = 1
	while(j):
		name = input('请输入您的姓名：')
		names.append(name)
		judge = input('您是否继续输入（Y/N）：')
		if judge.upper() == 'N':
			break

	with open(file_name, 'w') as write_user:
		json.dump(names, write_user)


def say_hello():
	users = get_stored_username()
	if users:
		for i in users:
			print('hi {0},welcome to python world.'.format(i))
	else:
		login_on()
		say_hello()

say_hello()