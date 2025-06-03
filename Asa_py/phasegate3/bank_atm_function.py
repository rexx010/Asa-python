accounts = []
check = []

def account_balance(balance):
	if balance < 0:
		print("invalid amount")
	else:
		amount = 0.0
		amount = amount + balance
		accounts.append(amount)
		check.append(balance)
		print("your current balance is: ", amount)
		return amount
	
	
def withdrawal(withdraw):
	price = accounts[0];
	if withdraw > price:
		message = "Not enough balance"
		print(message)

	checker = accounts[0]
	checker = checker * 0.90
	
	if withdraw > checker:
		message = "can't withdraw more than 90% of your balance at once"
		print(message)
	else:


		bal = accounts[0] - withdraw
		print("Transaction succesful")
		print("withdrawal amount: ", withdraw)
		charges = 100
		bal = bal - charges
		print("withdrawal fee:", charges)
		print("remaining balance:", bal)
		accounts[0] = bal 
		check.append(withdraw)

def transactions():
	print("This are the list of your transactions")
	print(check)
	return check



