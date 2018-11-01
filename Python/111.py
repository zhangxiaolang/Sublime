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
