import categorize_numbers
from unittest import TestCase



class TestCategorizeNumbers(TestCase):
	def test_that_get_numbers_function_exists(self):
		categorize_numbers.get_numbers(1)

	
	
	def test_that_get_numbers_return_numbers_that_are_dividable(self):
		actual = categorize_numbers.get_numbers(10, 15, 21, 30, 10, divisible_by=2)
		expected = [10, 30, 10]
		self.assertEqual(actual, expected)

	def test_that_tells_if_there_are_no_divisibles(self):
		actual = categorize_numbers.get_numbers(9, 15, 21, 17, divisible_by=2)
		expected = 'no divisible number found'
		self.assertEqual(actual, expected)

	def test_that_get_numbers_divisible_numbers_is_not_zero(self):
		actual = categorize_numbers.get_numbers(10, 15, 21, 30, divisible_by=0)
		expected = 'not divisible by zero'
		self.assertEqual(actual, expected)
	