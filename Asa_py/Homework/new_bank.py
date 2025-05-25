import random

accounts = []



def create_account(name, number, account_number, balance=0.0):
	account = [name, phone_number, account_number, balance]
	accounts.append(account)
	return accounts


def deposit():
	accounts
def withdrawal():
	accounts
def show_balance():
	accounts
def check_account():
	print(accounts)

option = True
while option:
	message = '''
Welcome to back to my console Bank...

press 1: To create account.
press 2: to deposit.
press 3: to withdraw.
press 4: to show balance
press 5: to check accounts in the bank.
press 0: to Exist.
'''
	print(message)
	user_selection = input('pick a number: ')
	match(user_selection):
		case '1': 
			name = input('Enter your name: ')
			phone_number = input('Enter your phone number: ')
			account_number = random.randrange(100000000, 9999999999)
			create_account(name, phone_number, account_number, balance=0.0)
			
		case '2': 
			search = input('Enter the name on the account you want to deposit to: ')
			deposit_amount = float(input('Enter the amount to deposit: '))
			deposit()
			for account in accounts:
				if account[0] == search:
					account[3] += deposit_amount

		case '3': 
			search = input('Enter the name on the account you want to deposit to: ')
			withdraw_amount = float(input('Enter the amount to deposit: '))
			withdrawal()
			for account in accounts:
				if account[0] == search:
					account[3] -= withdraw_amount

		case '4': 
			search = input('Enter the name on the account: ')
			show_balance()
			for account in accounts:
				if account[0] == search:
					print('your bank balance is:')
					print(account[3])
		case '5': 
			check_account()
			
		case '0': option = False
		case _: print("Invalid..., Read the lines again and choose the corrrect input")