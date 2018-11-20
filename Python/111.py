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