#map/reduce

def f(x):                      #map
	return x*x
l = [1,2,3,4,5,6,7,8,9]
r = map(f,l)
print(list(r))
print(list(map(str,l)))

from functools import reduce
def fn(x,y):
	return x*10 + y
print(reduce(fn,[1,3,5,7,9]))


#filter函数

#1.在一个list中删掉偶数，保留奇数
def is_odd(n):
	return n % 2 ==1
#a = [1,2,3,4,5,6,7,8,9,]
a = range(1,10)
b = list(filter(is_odd,a))
print('{0}经过转换后为{1}'.format(a,b))

#2.删除已组元素中的none和空格
def not_empty(s):
	return s and s.strip()
c = ['A','','B',None,'C',' ']
print(list(filter(not_empty,c)))

#3.求素数——埃氏筛法
def _odd_iter():   #构建一个从3开始的奇数序列
	n =1
	while True:
		n = n + 2
		yield n
def _not_divisible(n):    #定义一个筛选函数
	return lambda x: x % n > 0
def primes():
	yield 2
	it = _odd_iter() #初始序列
	while True:
		n = next(it) #返回序列第一个数
		yield n
		it = filter(_not_divisible(n),it)
for n in primes():           #打印1000以内的素数
	if n < 1000:
		print(n)
	else:
		break


#求回文数(两种方法)
def is_palindrome(n):    #方法1
    s=str(n)
    if len(s)==1:
        return True
    else:
        lst=[c for c in s]
        new_lst=[]
        for x in range(len(lst)):
            new_lst.append(lst[len(lst)-x-1])    #将s倒过来
        if (''.join(new_lst))==s:
            return True
        else:
            return False
output = filter(is_palindrome, range(1, 1000))
print(list(output))

def is_palindrome(n):     #方法2
    return str(n)==str(n)[::-1] #将str倒过来
output = filter(is_palindrome, range(1, 1000))
print(list(output))


#排序sorted()
L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
L1 = sorted(L,key=lambda x : x[0])					#按照姓名排序
L2 = sorted(L,key=lambda x : x[1],reverse=True)     #按照成绩由高到低排序
print(L1)
print(L2)


#偏函数
import functools
int2 = functools.partial(int, base=2)   #(自定义int函数使用二进制,默认十进制)
print(int2('10'))

import sys
def test():
 args = sys.argv
 if len(args)==1:
  print('Hello, world!')
 elif len(args)==2:
  print('Hello, %s!' % args[1])
 else:
  print('Too many arguments!')
if __name__=='__main__':
 test()