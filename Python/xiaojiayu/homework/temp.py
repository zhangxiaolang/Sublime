import os
import json


file_name = '123\\user_name.json'

def login_on():
	names = []
	name = input('请输入您的姓名：')
	names.append(name)
	print(names)

	with open(file_name, 'w') as write_user:
		json.dump(names, write_user)


def say_hello():
	with open(file_name) as read_user:
		users = json.load(read_user)
		print('hello {0},welcome python world.',format(users))

login_on()