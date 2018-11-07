with open('pi.txt') as pi_txt:
	#第一种读法
	# for i in pi_txt:
	# 	print(i)
	#第二种
	context = pi_txt.read()
	# print(context)
	print(context.rstrip())
