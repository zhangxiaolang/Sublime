def build_profile(first_name,last_name,**else_info):
	profile = {}
	profile['first_name'] = first_name
	profile['last_name'] = last_name
	for key,value in else_info.items():
			profile[key] = value
	return profile

user_a = build_profile('zhang','xiaolang',age = '24',location = 'tianshui',active = True)
print(user_a)
