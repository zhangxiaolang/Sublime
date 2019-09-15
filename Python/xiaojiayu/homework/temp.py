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
