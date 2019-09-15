#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-08-05 16:33:25
# @Author  : zk
# @Link    : http://example.org
# @Version : $Id$

import os
import random
print('----------the first game by zk----------')

def guess_number():
	temp = int(input("猜一个数字，看是否和我想的一样:"))
	guess = temp
	if guess == 8:
		print("bingo! it's right.")
	elif guess < 8:
		print("猜错了，应该比{0}大.".format(temp))
		guess_number()
	elif guess >8:
		print("猜错了，应该比{0}小.".format(temp))
		guess_number()


def guess_number2():
	i = random.randint(1,9)
	j = 1
	print(i)
	print("猜一个数字，看是否和我想的一样，您总共有5次机会:",end = ' ')
	guess = int(input())
	while(isinstance(guess,int) == False):
		guess = int(input("输入类型有误，请重新输入："))
	if guess == i:
		print("bingo! it's right.游戏结束！")
	else:
		while(guess != i and j < 5):
			guess = int(input("猜错了，请重新输入:"))
			while(isinstance(guess,int) == False):
				guess = int(input("输入类型有误，请重新输入："))
			if guess == i:
				print("bingo! it's right.游戏结束！")
			elif guess < i:
				print("猜错了，应该比{0}大.".format(guess))
				j = j + 1
			elif guess >i:
				print("猜错了，应该比{0}小.".format(guess))
				j = j + 1
		if j == 5:
			print("您的游戏次数已用完，游戏结束。")
guess_number2()

dir(__builtins__)
type(1.2)
isinstance(1.2,float)