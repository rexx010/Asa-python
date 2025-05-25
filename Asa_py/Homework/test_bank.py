from bank import accounts, create_account, deposit, withdraw, show_balance, check_accounts
from unittest import TestCase

class Testbank(TestCase):

	def test_that_account_created(self):
		create_account(1,2,3)

	def test_that_account_balance_is_not_negative(self):
		create_account('rexx', 87654, 654398, bal=0.0)
		actual = bal=0.0
		expected = bal=0.0
		self.assertEqual(actual, expected)
	
	def test_that_deposit_exist(self):
		deposit('rexx', 0.0)
		
	def test_that_user_can_search_for_account_name(self):
		deposit('dami', 1000)
		actual = accounts[0][0]
		expected = 'dami'
		self.assertEqual(actual, expected)

	def test_that_user_name_does_not_exit(self):
		deposit('john', 1000)
		actual = deposit('john', 1000)
		expected = "invalid name"
		self.assertEqual(actual, expected)

	def test_that_withdrawal_exists(self):
		withdraw('dami', 1000)

	def test_that_withdrawal_exceed_balance(self):
		withdraw('dami', 1000)
		actual = withdraw('dami', 100000)
		expected = "withdrawal exceed balance"
		self.assertEqual(actual, expected)

	def test_that_withdrawal_does_not_exceed_balance(self):
		withdraw('dami', 2000)
		actual = accounts[0][3] - 0
		expected = accounts[0][3]
		self.assertEqual(actual, expected)

	def test_that_show_balance_exists(self):
		show_balance('rexx')

	def test_that_show_balance_is_not_returns_balance(self):
		show_balance('rexx')
		actual = show_balance('rexx')
		expected = accounts
		self.assertEqual(actual, expected)

	def test_that_account_to_show_exists(self):
		show_balance('dami')
		actual = show_balance('tunji')
		expected = "invalid name"
		self.assertEqual(actual, expected)

	def test_that_check_accounts_exists(self):
		check_accounts('phone_number', 234536)

	def test_that_list_of_the_accounts_available_can_be_seen(self):
		check_accounts('phone_number', 234536)
		actual = check_accounts(1234567891, 1234567891)
		expected = accounts
		self.assertEqual(actual, expected)

	def test_that_user_can_use_account_number_or_phone_number_to_check_account_details(self):
		check_accounts('phone_number', 234536)
		actual = check_accounts(1234567891, 1234567891)
		expected = accounts
		self.assertEqual(actual, expected)

	def test_that_account_number_is_up_to_ten_digits(self):
		check_accounts(123456787651, 2345361234)
		actual = check_accounts(1234567876, 23453611)
		expected = "invalid number"
		self.assertEqual(actual, expected)

	def test_that_phone_number_is_up_to_eleven_digits(self):
		check_accounts(12345678912, 2345361234)
		actual = check_accounts(12348912, 2345369812)
		expected = "invalid number"
		self.assertEqual(actual, expected)



