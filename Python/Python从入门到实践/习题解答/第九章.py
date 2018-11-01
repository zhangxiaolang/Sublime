#9-1,9-2
class Restaurant():
	# 定义数据
	def __init__(self,restaurant_name,cuisine_type):
		self.restaurant_name = restaurant_name
		self.cuisine_type = cuisine_type
	#输出信息
	def describt_restraurant(self):
		print('the restaurant name is {0}'.format(self.restaurant_name))
		print('the cuisine type is {0}'.format(self.cuisine_type))
	#是否营业
	def open_restraurant(self):
		print('{0} is open'.format(self.restaurant_name))

re1 = Restaurant('京跃华','火锅')
re2 = Restaurant('兰香阁','清真')

re1.describt_restraurant()
re2.open_restraurant()

#9-3
class User():
	def __init__(self,first_name,last_name,*else_info):
		self.first_name = first_name
		self.last_name = last_name

	def describe_user(self):
		print('{0}{1},welocme to python!'.format(self.first_name,self.last_name))

	def greet_user(self):
		print('hello,{0}.{1}!'.format(self.first_name.title(),self.last_name))

user1 = User('zhang','xiaolang',23)
user1.describe_user()
user1.greet_user()

#9-4
class Restaurant():
	# 定义数据
	def __init__(self,restaurant_name,cuisine_type,number_serverd=0):
		self.restaurant_name = restaurant_name
		self.cuisine_type = cuisine_type
		if number_serverd >= 0:
			self.number_serverd = int(number_serverd)
	#输出信息
	def describt_restraurant(self):
		print('餐馆名： {0}'.format(self.restaurant_name))
		print('餐馆类型： {0}'.format(self.cuisine_type))
		print('您当前就餐人数为：{0}'.format(self.number_serverd))
	#是否营业
	def open_restraurant(self):
		print('{0} is open'.format(self.restaurant_name))

	#设置就餐人数
	def set_number_serverd(self,number_serverd):
		if number_serverd > 0:
			self.number_serverd = int(number_serverd)
		print('您当前就餐人数为：{0}'.format(self.number_serverd))

	#递增就餐人数
	def increment_number_served(self):
		self.number_serverd += 200
		print('餐馆就餐历史总人数为：{0}'.format(self.number_serverd))



re1 = Restaurant('京跃华','火锅')
re2 = Restaurant('兰香阁','清真')

re1.describt_restraurant()
re1.open_restraurant()
re1.set_number_serverd(15)
re1.increment_number_served()
re1.increment_number_served()
re1.increment_number_served()


#9-5
class User():
	def __init__(self,first_name,last_name,login_attempts=5):
		self.first_name = first_name
		self.last_name = last_name
		self.login_attempts = login_attempts

	def describe_user(self):
		print('{0}{1},welocme to python!'.format(self.first_name,self.last_name))

	def greet_user(self):
		print('hello,{0}.{1}!'.format(self.first_name.title(),self.last_name))

	def increment_login_attempts(self):
		if self.login_attempts > 0:
			print('账号或密码错误，您还有{0}次登陆机会，之后账号将锁定一定时间！'.format(self.login_attempts))
			self.login_attempts -= 1
		else:
			print('错误次数过多，您的账号已被锁定，请稍后再试！')

	def reset_login_attempts(self):
		self.login_attempts = 5


user1 = User('zhang','xiaolang')
user1.describe_user()
for i in range(1,7):
	user1.increment_login_attempts()
print(user1.login_attempts)
user1.reset_login_attempts()
print(user1.login_attempts)

#9-6
class Restaurant():
	# 定义数据
	def __init__(self,restaurant_name,cuisine_type):
		self.restaurant_name = restaurant_name
		self.cuisine_type = cuisine_type
	#输出信息
	def describt_restraurant(self):
		print('the restaurant name is {0}'.format(self.restaurant_name))
		print('the cuisine type is {0}'.format(self.cuisine_type))
	#是否营业
	def open_restraurant(self):
		print('{0} is open'.format(self.restaurant_name))

class IceCreamStand(Restaurant):
	def __init__(self,restaurant_name,cuisine_type):
		super().__init__(restaurant_name,cuisine_type)
		self.flavors = flavors

	def describt_IceCreamStand(self):
		print('the restaurant name is {0}'.format(self.restaurant_name))
		print('the cuisine type is {0}'.format(self.cuisine_type))
		print('冰淇淋口味有：')
		for i in self.flavors:
			print(i)


flavors = ['抹茶','奶油','巧克力']
re1 = IceCreamStand('爱的礼物','糕点')
re1.describt_IceCreamStand()

#9-7,9-8
class User():
	def __init__(self,first_name,last_name,*elseinfo):
		self.first_name = first_name
		self.last_name = last_name

	def describe_user(self):
		print('{0}{1},welocme to python!'.format(self.first_name,self.last_name))

	def greet_user(self):
		print('hello,{0}.{1}!'.format(self.first_name.title(),self.last_name))

class Admin(User):
	"""docstring for Admin"""
	def __init__(self,first_name,last_name,privilegs):
		super().__init__(first_name,last_name,privilegs)
		self.privilegs = privilegs

	def show_privileges(self):
		print('管理员拥有的权限有：')
		for i in self.privilegs:
			print(i)

quanxian = ['增','删','改','查']

user1 = Admin('zhang','xiaolang', quanxian)
user1.describe_user()
user1.show_privileges()

#9-14
from random import randint
class Die():
	def __init__(self,side,count):
		self.side = side
		self.count = count

	def roll_die(self):
		n = randint(1,self.side)
		return n

def ThrowDie():
	a = int(input('请输入您想要的骰子的面数：'))
	b = int(input('请输入您想要的骰子的次数：'))
	A = Die(a,b)
	i=0
	print('您选的的骰子面数为{0}，投掷次数为{1}'.format(a,b))
	while(i<b):
		print('第{0}次投掷，结果为：{1}'.format(i+1,A.roll_die()))
		i += 1

	judge = input('您是否要继续玩(y/n)：')
	if (judge == 'y' or judge == 'Y'):
		ThrowDie()
	else:
		print('感谢您的使用！')

ThrowDie()
