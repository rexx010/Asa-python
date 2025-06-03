import bank_atm_function
from unittest import TestCase


class TestCube(TestCase):
	
	def test_that_function_exist(self):
		bank_atm_function.account_balance(2)

	def test_that_user_can_deposit(self):
		actual = bank_atm_function.account_balance(50000)
		expected = 50000
		self.assertEqual(actual, expected)

	def test_that_you_can_withdraw(self):
		bank_atm_function.withdrawal(100000)
		actual = 100000 - 70000
		expected = 30000.0
		self.assertEqual(actual, expected)

	def test_that_you_can_view_transaction_log(self):
		actual = bank_atm_function.transactions()
		expected = [2, 50000]
		self.assertEqual(actual, expected)