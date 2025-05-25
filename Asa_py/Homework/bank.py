import random

accounts = []


def create_account(name, phone_number, acc_number, bal=0.0):
	account = [name, phone_number, acc_number, bal]
	accounts.append(account)
	return accounts


def deposit(find_name, deposit_amount):
	for account in accounts:
		if account[0] == find_name:
			account[3] += deposit_amount
			return account
	return "invalid name"		

def withdraw(find_name, withdraw_amount):
	if accounts[0][3] < withdraw_amount:
		return "withdrawal exceed balance"
	
	if withdraw_amount > 0 and withdraw_amount <= accounts[0][3]:
		for account in accounts:
			if account[0] == find_name:
				account[3] -= withdraw_amount
				return account

def show_balance(find_name):
	for account in accounts:
		if account[0] == find_name:
			#print('your bank balance is:')
			#print(account[3])
			return accounts
	return "invalid name"

def check_accounts(phone_number, acc_number):
	if acc_number < 100000000 or acc_number > 9999999999:
		return 'invalid number'
	if phone_number < 1000000000 or phone_number > 99999999999:
		return 'invalid number'

	for account in accounts:
		if account[1] == phone_number and account[2] == acc_number:
			print(account)
		return accounts





name = 'dami'
phone_number = 17086135955
acc_number = random.randrange(100000000, 9999999999)

find_name = 'dami'
deposit_amount = 15000

withdraw_amount = 2000




create_account(name, phone_number, acc_number)
deposit(find_name, deposit_amount)
withdraw(find_name, withdraw_amount)
show_balance(find_name)
print(accounts)