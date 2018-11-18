#10-11
import json
a = input('请输入你喜欢的数字：')
filename = 'number.json'

with open(filename,'w') as f_obj:
	json.dump(a,f_obj)


with open(filename) as f_obj2:
	a = json.load(f_obj2)
	print('你喜欢的数字是：{0}'.format(a))