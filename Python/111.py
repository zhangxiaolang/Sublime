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