def normalize(name):
	return name.capitalize()
L1 = ['adam','LISA','barT']
L2 = list(map(normalize,L1))
print(L2)
