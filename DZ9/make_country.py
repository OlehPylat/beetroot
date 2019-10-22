def make_country(name,capital,**dict):
	pet = {}
	pet['name'] = name
	pet['capital'] = capital
	for key, value in dict.items():
		pet[key] = value
	return pet
print(make_country('Ukraine','Kyiv'))
