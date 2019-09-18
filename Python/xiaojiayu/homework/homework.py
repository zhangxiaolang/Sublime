

import random
times = 3
secret = random.randint(1,10)
print('------------------我爱鱼C工作室------------------')
# 这里先给guess赋值（赋一个绝对不等于secret的值）
guess = 0
# print()默认是打印完字符串会自动添加一个换行符，end=" "参数告诉print()用空格代替换行
# 嗯，小甲鱼觉得富有创意的你应该会尝试用 end="JJ"？
print("不妨猜一下小甲鱼现在心里想的是哪个数字：", end=" ")
while (guess != secret) and (times > 0):
    temp = input()
    guess = int(temp)
    times = times - 1 # 用户每输入一次，可用机会就-1
    if guess == secret:
        print("我草，你是小甲鱼心里的蛔虫吗？！")
        print("哼，猜中了也没有奖励！")
    else:
        if guess > secret:
            print("哥，大了大了~~~")
        else:
            print("嘿，小了，小了~~~")
        if times > 0:
            print("再试一次吧：", end=" ")
        else:
            print("机会用光咯T_T")
print("游戏结束，不玩啦^_^")


#1、请写一个程序打印出 0~100 所有的奇数。
import random

print('0-100中的奇数有：')
for i in range(0,100):
    if(i % 2 ==1):
        print('{0},'.format(i),end = ' ')


#2、爱因斯坦曾出过这样一道有趣的数学题：有一个长阶梯，若每步上2阶，最后剩1阶；若每步上3阶，最后剩2阶；若每步上5阶，最后剩4阶；若每步上6阶，最后剩5阶；只有每步上7阶，最后刚好一阶也不剩。
#题目：请编程求解该阶梯至少有多少阶？
for i in range(1,1000):
    if(i % 7 == 0):
        if((i-5)%6==0):
            if (i-4)%5 == 0:
                if (i-2)%3 == 0:
                    if (i-1)%2 == 0:
                        print('台阶数最少为：{0}。'.format(i))
                        break


#解法2，占用内存特别高
temp = 7
i = 1
print('200以内满足条件的台阶数有：',end=' ')
while(temp<=200):
    if (temp%7 == 0) and (temp%6 == 5) and (temp%5 == 4) and (temp%3 == 2) and (temp%2 == 1) :
        print(temp,end=' ')
        i += 1
        temp *= i

#3、假设有 x = 1，y = 2，z = 3，请问如何快速将三个变量的值互相交换？
x=1
y=2
z=3
print('x=:{0}，y={1}，z={2}'.format(x,y,z))

temp = x
x = y
y = z
z = temp
print('变换之后的值：x=:{0}，y={1}，z={2}'.format(x,y,z))

#j解法2
x, y, z = z, y, x


#4、按照100分制，90分以上成绩为A，80到90为B，60到80为C，60以下为D，写一个程序，当用户输入分数，自动转换为ABCD的形式打印。
tag = 1
while(tag):
    score = int(input('请输入成绩：'))
    if(score >= 90):
        print('{0}分归为A档。'.format(score))
    elif(score >= 80):
        print('{0}分归为B档。'.format(score))
    elif(score >= 60):
        print('{0}分归为C档。'.format(score))
    else :
        print('{0}分归为D档。'.format(score))
    judge = input('是否继续输入成绩(Y/N)：')
    if judge == y or judge == Y:
        tag = 1
    elif judge == n or judge == N:
        tag = 0
    else :
        print('输入错误，程序即将退出.....')
        tag = 0


#5、编写一个程序，求 100~999 之间的所有水仙花数。
#如果一个 3 位数等于其各位数字的立方和，则称这个数为水仙花数。例如：153 = 1^3 + 5^3 + 3^3，因此 153 就是一个水仙花数。

def fun_narcissus():
    print('100-999之间的所有水仙花数有如下所示：')
    num = 100
    while(num <= 999):
        a = int(num/100)
        b = int(num/10) - (a * 10)
        c = num - (a * 100) - (b * 10)
        if num == a**3 + b**3 + c**3:
            print(num,end = ', ')
        num += 1
fun_narcissus()


#6、有红、黄、蓝三种颜色的球，其中红球 3 个，黄球 3 个，绿球 6 个。先将这 12 个球混合放在一个盒子中，从中任意摸出 8 个球，编程计算摸出球的各种颜色搭配。

print('red \t yellow \t green')
for red in range(0, 4):
    for yellow in range(0, 4):
        for green in range(2, 7):
            if red + yellow + green == 8:
                # 注意，下边不是字符串拼接，因此不用“+”哦~
                print(red, '\t', yellow, '\t', green)
