movie = ["The Holy Grial", "The Life of Brian", "The Meaning of Life"]		#创建数组
movie.append('3')			#在数组末尾添加元素
movie.pop()					#删除数组末尾元素
movie.extend(['4','5'])		#在末尾添加数据项集合
movie.remove("4")			#删除具体元素
movie.insert(3,"3")			#在具体位置插入具体元素

movie.insert(1,1975)
movie.insert(3,1979)
movie.insert(5,1983)


movie = ["The Holy Grial", 1975,"The Life of Brian",1979 ,"The Meaning of Life",1983,
 ["Graham Chapman",["Michael Palin","John Cleese","Terry Gilliam","Eric Idle","Terry Jones",["第四层",["第五层"]]]]]

def print_lot(b):				#递归调用,python3默认递归深度不超过100
	for a in b:
		if isinstance(a,list):
			print_lot(a)
		else:
			print(a)

print_lot(movie)


def aplusb(self,a,b):
	self = a+b
	return self
c = int(input("请输入第一个整数："))
d = int(input("请输入第二个整数："))
n = 0
print("两数之和为{0}".format(aplusb(n,c,d)))