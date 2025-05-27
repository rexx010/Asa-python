import to_do_list_function
from unittest import TestCase


class TestCube(TestCase):

	def test_that_create_function_exits(self):
		to_do_list_function.create_console('name')

	def test_that_view_tasks(self):
		to_do_list_function.view_tasks()
		actual = to_do_list_function.view_tasks()
		expected = ['tobi']
		self.assertEqual(actual, expected)	
		