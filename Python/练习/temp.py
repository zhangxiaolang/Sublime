# #读取excel文件并输出
# import os
# import xlrd
# print(os.getcwd())  #获取并输出当前文件夹位置
# os.chdir('E:\\MES\\Order\\05024')
# print(os.getcwd())
# book = xlrd.open_workbook('05024br.xls')
# sh = book.sheet_by_index(0)
# print(sh.name,sh.nrows,sh.ncols)
# for rx in range(sh.nrows):
# 	print(sh.row(rx))
# book.close()


#读取txt文档
import os
print(os.getcwd())  #获取并输出当前文件夹位置
os.chdir('C:\\Users\\Administrator\\Desktop')
print(os.getcwd())
#if os.path.exists('1234.txt'):   #方法1
try:
	data = open('123.txt')
	#print(data.readline,end='')
	#data.seek(0)  #返回文件其实位置（也可以使用tell()）
	for each_line in data:
		#if not each_line.find('.') == -1:   #当数据行中没有“.”时绕过，保证正确运行
		try:
			(role,line_spoken) = each_line.split('.',1)  #后面的参数1保证了在有多个"."的时候也只分为两部分
			print(role)
			print(line_spoken)
		except ValueError:	#except后面加参数表示抓取特定的错误
			pass
	data.close()   #处理完的文件进行关闭
#else:  #方法1
except IOError:
	print('The data file is missing!')