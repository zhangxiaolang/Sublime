#10-4
fliename = 'Guest_name.txt'
def guest():
	flag = 1
	while(flag==1):
		guestname = input('hi,welcome,please input your name:')
		with open('File_folder\\Guest_name.txt','a') as gname:
			gname.writelines(guestname+'\n')
		judge = input('continue(y/n)?:')
		if(judge.upper() == 'Y'):
			flag =1
		else:
			flag =2
guest()
with open('File_folder\\Guest_name.txt') as gname2:
	context = gname2.read()
	print('hello,'+context.rstrip())