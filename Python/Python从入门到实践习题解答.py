#2-3（将用户的姓名存到一个变量中，并向该用户显示一条消息。显示的消息应非常简单，
#如 “Hello Eric, would you like to learn some Python today?” ）
name = input('Enter your name: ')
print('Hello {0}, would you like to learn some Python today?'.format(name))

#2-4(调整名字的大小写： 将一个人名存储到一个变量中，再以小写、大写和首字母大写的方式显示这个人名。)
name = input('Enter your name: ')
print(name.lower())
print(name.upper())
print(name.title())

#2-5(名言： 找一句你钦佩的名人说的名言，将这个名人的姓名和他的名言打印出来。输出应类似于下面这样（包括引号）：)
name = input('Enter your name: ')
content = input('Enter contain: ')
print('{0} once said, “{1}.”'.format(name,content))

#2-6，7(剔除人名中的空白： 存储一个人名，并在其开头和末尾都包含一些空白字符。务必至少使用字符组合 "\t" 和 "\n" 各一次。
#打印这个人名，以显示其开头和末尾的空白。然后，分别使用剔除函数 lstrip() 、 rstrip() 和 strip() 对人名进行处理，并将结果打印出来。)
name = input('Enter your name: ')
print(name.lstrip())
print('制表\t'+ name.rstrip())
print('回车\n'+name.strip())

#