with open('pi.txt') as pi_txt:
	#第一种读法
	# for i in pi_txt:
	# 	print(i)
	#第二种
	context = pi_txt.read()
	# print(context)
	print(context.rstrip())
#python 不识别..
with open('else\\111.txt') as pi_txt:
	#第一种读法
	# for i in pi_txt:
	# 	print(i)
	#第二种
	context = pi_txt.read()
	# print(context)
	print(context.rstrip())

filename = 'pi.txt'with open(filename) as pi_txt:
	#存储到列表
	context = pi_txt.readlines()
for i in context:
	print(i.rstrip())


#文件读写
#w,文件不存在则创建并写入，文件存在则清空并写入
filename = 'pi.txt'
with open(filename,'w') as pi_txt:
	pi_txt.writelines('this is a test!\n')
#a,在文件末尾插入，不会删除文件原来信息
filename = 'pi.txt'
with open(filename,'a') as pi_txt:
	pi_txt.writelines('this is a test!\n')


#10-3
guestname = input('please input your name:')
fliename = 'Guest_name.txt'
with open('File_folder\\Guest_name.txt','a') as gname:
	gname.writelines(guestname+'\n')

with open('File_folder\\Guest_name.txt') as gname2:
	context = gname2.read()
	print(context.rstrip())

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