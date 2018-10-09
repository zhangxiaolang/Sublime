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

#8-6
def city_country(city,country):
	print("{0},{1}".format(city,country))

judge = 'y'
while judge.upper() == 'Y':
	city = input('please input you city:')
	country = input('please input you country:')
	city_country(city,country)
	judge = input('\n go on ?(y/n):')

#8-7,8-8
def sings(name,sing_name,qualtity = ''):
	info = {'歌手':name, '歌曲名':sing_name}
	if qualtity:
		info['歌曲数'] = qualtity
	return info

judge = 'y'
while judge.upper() == 'Y':
	a = input('please input singer name:')
	b = input('please input  the CD name:')
	c = input('if you know the CD sings qualtity ,pls enter:')
	if c:
		print(sings(a,b,c))
	else:
		print(sings(a,b))
	judge = input('\n go on ?(y/n):')

#8-7,8-8加强版
def sings(name,sing_name,qualtity = ''):
	info = {'歌手':name, '歌曲名':sing_name}
	if qualtity:
		info['歌曲数'] = qualtity
	return info

judge = 'y'
infos = []
while judge.upper() == 'Y':
	a = input('please input singer name:')
	b = input('please input  the CD name:')
	c = input('if you know the CD sings qualtity ,pls enter:')
	if c:
		sings(a,b,c)
		infos.append(sings(a,b,c))
	else:
		sings(a,b)
		infos.append(sings(a,b))
	judge = input('\n go on ?(y/n):')

for i in infos:
	print(i)


#8-9,10
magicians = ['1','2','3']
def show_magicians(magicians):
	for i in magicians:
		print('{0}是一个魔术师！'.format(i))

def make_great(magicians):
	j = 0
	for i in magicians:
		magicians[j] = magicians[j] + '不'
		print('{0}是一个魔术师！'.format(magicians[j]))
		j += 1
for i in magicians:
	print(i)
show_magicians(magicians)
make_great(magicians)
show_magicians(magicians)

#8-11
magicians = ['1','2','3']
def show_magicians(magicians):
	for i in magicians:
		print('{0}是一个魔术师！'.format(i))

def make_great(magicians):
	j = 0
	for i in magicians:
		magicians[j] = magicians[j] + '不'
		print('{0}是一个魔术师！'.format(magicians[j]))
		j += 1
for i in magicians:
	print(i)
show_magicians(magicians)
make_great(magicians[:])
show_magicians(magicians)

#8-12
def pizzas(*toppings):
	print('您的pizza中加的料如下：')
	for i in toppings:
		print(i)
	print('--------------------------')

pizzas('鸡肉','火腿')
pizzas('鸡蛋','培根','早餐肉')

#8-13,14
def build_profile(first_name,last_name,**else_info):
	profile = {}
	profile['first_name'] = first_name
	profile['last_name'] = last_name
	for key,value in else_info.items():
			profile[key] = value
	return profile

user_a = build_profile('zhang','xiaolang',age = '24',location = 'tianshui',active = True)
print(user_a)
