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
		super().__init__(self,first_name,last_name,privilegs)
		self.privilegs = privilegs

	def show_privileges(self):
		print('管理员拥有的权限有：')
		for i in self.privilegs:
			print(i)

quanxian = ['增','删','改','查']

user1 = Admin('zhang','xiaolang',quanxian)
user1.describe_user()
user1.show_privileges()