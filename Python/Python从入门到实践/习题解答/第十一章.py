#开始
def get_formatted_name(first, last):
"""Generate a neatly formatted full name."""
	full_name = first + ' ' + last
	return full_name.title()

#11-1
#shiyizhang.py
def get_formatted_name(first, last):
	"""Generate a neatly formatted full name."""
	full_name = first + ',' + last
	return full_name.title()
#测试用例
import unittest
from shiyizhang import get_formatted_name
class NameTestCase(unittest.TestCase):
	def test_city_county(self):
		city_country = get_formatted_name('tianshui','china')
		self.assertEqual(city_country,'Tianshui,China')

unittest.main()


#11-2
#shiyizhang.py
def get_city_country_name(city,country,population = ''):
	if population:
		full_name = city + ',' + country + ',population-' + population
		return full_name.title()
	else:
		full_name = city + ',' + country
		return full_name.title()
#测试用例
import unittest
from shiyizhang import get_city_country_name
class testcase(unittest.TestCase):
	def test_city(self):
		name1 = get_city_country_name('tianshui','china','200000')
		self.assertEqual(name1,'Tianshui,China,Population-200000')

	def test_city2(self):
		name2 = get_city_country_name('tianshui','china')
		self.assertEqual(name2,'Tianshui,China')

unittest.main()

