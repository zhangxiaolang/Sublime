def get_formatted_name(first, last):
	"""Generate a neatly formatted full name."""
	full_name = first + ',' + last
	return full_name.title()


def get_city_country_name(city,country,population = ''):
	if population:
		full_name = city + ',' + country + ',population-' + population
		return full_name.title()
	else:
		full_name = city + ',' + country
		return full_name.title()
