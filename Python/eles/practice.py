#输出形式有点像C语言，保留两位小数
name1 = input('请输入你的名字：')
print('{0},欢迎你'.format(name1))
name2 = input('请输入你的昵称：')
print('{0},你的昵称是{1},欢迎你'.fTormat(name1,name2))
s1 = 72
s2 = 85
a = ((85-72)/85)*100
print('hello,{0},成绩提升了{1:.2f}%'.format('小明',a))

#list使用
classmates = ['张三','李四','王五']
print(classmates)
classmates.append('小红')
print(classmates)
classmates.insert(0,'小燕')
print(classmates)
classmates.pop()    #删除list末尾元素
print(classmates)
classmates.pop(0)   #删除指定位置元素
print(classmates)
classmates[0] = '小张'   #替换某个位置元素

#定义数组时使用()表示tuple数组，这种数组一旦确实不能改动。
tuple1 = (1,2,3,4,5)
print(tuple1)

#计算小明的BMI值
h1 = 1.72
w1 = 81
zhishu = ['过轻','正常','过重','肥胖','严重肥胖']
BMI = w1/(h1*h1)
if 25<BMI<32:
 print('您的BMI指数为：{0}，属于{1}人群'.format(BMI,zhishu[2]))
else:
 print('lalala')

#在字段后的 ':' 后面加一个整数会限定该字段的最小宽度，这在美化表格时很有用
#dict键值对。删除值可以使用table.pop('Sjolerd')即可
table = {'Sjoerd':4127,'Jasck':4098,'Dcab':7578}
for name,phone in table.items():
	print('{0:10}=====>{1:10}'.format(name,phone))


#if语句
s = input('birthday:')
birth = int(s) #由于s是字符串，所以先转换为int再进行比较
if birth <2000:
   print('00前')
else:
   print('00后')

#for in语句
L = ['Bart','Lisa','Adam']
for x in L:
 print('Hello,' + x + '!')    #这两种输出结果相同
 print('Hello,{0}!'.format(x))


#定义函数并使用
import math
def move(x,y,step,angle=0):
	nx = x + step * math.cos(angle)
	ny = y + step * math.sin(angle)
	return nx,ny
x,y = move(100,100,60,math.pi/6)
print(x,y)


#求一元二次方程的解
import math
def quadratic(a, b, c):
    x1 = (-b + math.sqrt(math.pow(b, 2)-(4*a*c))) / (2*a)
    x2 = (-b - math.sqrt(math.pow(b, 2)-(4*a*c))) / (2*a)
    return x1, x2
print(quadratic(2, 3, 1))
print(quadratic(1, 3, -4))


#函数默认参数
def power(x, y=2):  # 这里的2则充当默认参数的作用
    s = 1
    while y > 0:
        y = y-1
        s = s*x
    return s
print(power(2))  # 输出4
print(power(2, 3))  # 输出8
print(power(2, 1))  # 输出2


#可变参数
def calc(*numbers):
    sum = 0
    for n in numbers:
        sum = sum + power(n)
    return sum
print(calc(1, 2))
a = [1, 2, 3, 4, 5]
print(calc(*a))


#递归函数（当传入数太大时会发生栈溢出错误，尾递归可以防止这种错误的发生）
def fact(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return n * fact(n-1)
a = input('请输入：')
print(type(a))
b = int(a)
print(fact(b))

#尾递归函数
def fact(n):
	return fact_iter(n,1)
def fact_iter(num,product):
	if num == 1:
		return product
	return fact_iter(num-1, num*product)
a = input('请输入：')
print(type(a))
b = int(a)
print(fact(b))


# 利用递归函数移动汉诺塔:
def move(n, a, b, c):
    if n == 1:
        print('move', a, '-->', c)
    else:
        move(n-1, a, c, b)
        move(1, a, b, c)
        move(n-1, b, a, c)
a = input("请输入A柱上面的盘子数目：")
b = int(a)
move(b, 'A', 'B', 'C')


#Python切片
L = ['Michael', 'Sarah', 'Tracy', 'Bob', 'Jack']

print('L[0:3] =', L[0:3])            #从0到3不包括3
print('L[:3] =', L[:3])              #同上，0可省略
print('L[1:3] =', L[1:3])			 #1到3不包括3
print('L[-2:] =', L[-2:])			 #-2到结束

R = list(range(100))				 #从0开始的一百位数字，即0-99
print('R[:10] =', R[:10])
print('R[-10:] =', R[-10:])
print('R[10:20] =', R[10:20])
print('R[:10:2] =', R[:10:2])		 #0到9，每两个数取一个
print('R[::5] =', R[::5])			 #所有数，每五个数取一个


#迭代(默认为取key的值)
d = {'a':1, 'b':2, 'c':3}
for key in d:
	print(key)

for value in d.values():
	print(value)

for k,v in d.items():
	print('key:{0}======>value:{1}'.format(k,v))


#列表生成式
l1 = list(range(1,11))
print('生成的l1为：{0}'.format(l1))

l2 = []
for x in range(1,11):
	l2.append(x*x)
print('生成的l2为：{0}'.format(l2))

#使用列表生成式
l3 = [x*x for x in range(1,11)]        #单层循环
print('生成的l3为：{0}'.format(l3))

l4 = [m+n for m in 'ABC' for n in 'XYZ']   #两层循环
print('生成的l4为：{0}'.format(l4))

L1 = ['Hello', 'World', 18, 'Apple', None]
L2 = [s.lower() for s in L1 if isinstance(s,str)]
print(L2)     #输出为['hello', 'world', 'apple']


#斐波那契数列
def Fibonacci(max):
	n,a,b = 0,0,1
	while n<max:
		print(b)
		a,b = b,a+b
		n = n+1
	return 'done'

i = input('请输入您想要的斐波那契数列的位数：')
x = int(i)
print(Fibonacci(x))


#杨辉三角
def triangles():
    L = [1]
    while True:
        yield L
       # L.append(0)
       # L = [L[i-1] + L[i] for i in range(len(L))]
        L = [1] + [L[i] + L[i+1] for i in range(len(L)-1)] + [1]
n = 0
for t in triangles():
    print(t)
    n = n + 1
    if n == 10:
        break


lista = list(range(1,10))
print(lista)
for i in lista:
    print('this is {0}\n'.format(i))


listb = list(range(1,10,2))
print(listb)


listc = []
listd = []
for i in range(1,1000,100):
    listd.append(i)
    listc.append(i**2)
print('{0}\n{1}'.format(listc,listd))
print('the min value in listc is :{0}'.format(min(listc)))
print('the max value in listc is :{0}'.format(max(listc)))
print('the listc sum is :{0}'.format(sum(listc)))


#4-10
print('The first three items in the list are:{0}'.format(listc[0:3]))
k = int(len(listc)/3)
print(k)
print('Three items from the middle of the list are:{0}'.format(listc[k:k+3]))
print('The last three items in the list are:{0}'.format(listc[-3:]))


#4-11  切片在复制列表中使用
foods = ['chiken','noodles','dumplings']
friend_foods = foods
friend_foods_2 = foods[:]
foods.append('tomato')
friend_foods.append('potato')
friend_foods_2.append('apple')
print('foods is :{0}'.format(foods))
print('friend_foods is :{0}'.format(friend_foods))
print('friend_foods_2 is :{0}'.format(friend_foods_2))

for i in foods:
    print('{0}'.format(i))




#定义未确认的用户
unconfiremd_users = ['alice','slabe','brian']
#定义已确认的用户
confiremed_users = []
while unconfiremd_users:
    current_user = unconfiremd_users.pop()
    print('Verifying user:' + current_user.title())
    confiremed_users.append(current_user)

print('\nThe following user have been confiremd:')
for confiremed_user in confiremed_users:
    print (confiremed_user.title())



#验证问题
responses = {}

answer_flag = True;

while answer_flag:
    name = input('\n您的姓名：')
    response = input('您喜欢吃什么东西：')
    responses[name] = response
    repeat = input('是否要继续录入数据（y/n）:')
    if repeat.upper() == 'N':
        answer_flag = False
    elif repeat.upper() == 'Y':
        answer_flag = True
    else:
        answer_flag = False
        repeat = input('输入错误，退出输入！')

print('--------结果如下--------')
for name,response in responses.items():
    print(name + '喜欢吃' + response)
