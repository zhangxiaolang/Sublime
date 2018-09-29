#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-03-26 21:57:12
# @Author  : 张小浪 
# @E-mail  : 916900730@qq.com


import os

#猜数字游戏
age_of_princal =56
def guess(x):
    guess_age = int(input("you guess age is :"))
    while(guess_age != x):
        if(guess_age > x):
            print("sorry,you answer is bigger than the actual answer!")
        elif(guess_age < x):
            print("sorry,you answer is smaller than the actual answer!")
        return guess(x)
    if(guess_age == x):
        print("congratulation！you answer is right!")
guess(age_of_princal)


#登录接口，三次失败即锁定
account = 'admin'
password = 'admin'
i = 1
def log_in(account,password,i):
    input_acc = input("请输入您的账号：")
    input_pass = input("请输入您的密码：")
    if(input_acc == account and input_pass == password):
        print("您好，{0},欢迎您登录！".format(input_acc))
    elif(input_acc != account or input_pass != password):
        print("您好，账号或密码输入错误,请您重新输入！")
        i = i + 1
        if(i > 3):
            print("您信息输入错误三次，账号已被锁定")
        else:
            log_in(account,password,i)
log_in(account,password,i)

