import to_do_list_function
from unittest import TestCase


class TestCube(TestCase):

	def test_that_create_function_exits(self):
		to_do_list_function.create_console('name')

	def test_that_function_mark_task_completed(self):
		actual = to_do_list_function.mark_task_completed('tobi[X]')
		expected = 'tobi[X]'
		self.assertEqual(actual, expected)