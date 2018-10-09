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