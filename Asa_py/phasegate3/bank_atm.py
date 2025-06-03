import bank_atm_function
hi = True
while hi:
	message = '''
welcome to my bank app
press 1 to deposit
press 2 to withdraw
press 3 Transactions
press 0 to exit
	'''
	print(message)
	userchoice = int(input())
	match(userchoice):

		case 1:
	
			message = '''
choose a number
press 1 to deposit
press 0 to go back
				'''
			print(message)
			
			choice1 = int(input())
			match(choice1):
				
				#while back_menu:
				case 1:
					message = '''
Enter amount
					'''
					print(message)
					user_amount = int(input())
					bank_atm_function.account_balance(user_amount)

				case _:
					print("invalid input")
		case 2:
			while True:
				message = '''
press amount to withdraw in multiple of 500 or 1000

press 1 for 500
press 2 for 1000
press 0 to exit
				'''
				print(message)
				choice1 = int(input())
				match(choice1):
			
					case 1:
						message = '''
press 1 for 5000
press 2 for 10000
press 3 for 15000
press 4 for 20000
press 5 to enter an amount						'''
						print(message)
						choice1 = int(input())
						match(choice1):
							case 1:
								five_thousand = 5000.0
								bank_atm_function.withdrawal(five_thousand)
							case 2:
								ten_thousand = 10000.0
								bank_atm_function.withdrawal(ten_thousand)
							case 3:
								fifteen_thousand = 15000.0
								bank_atm_function.withdrawal(fifteen_thousand)
							case 4:
								twenty_thousand = 20000.0

							case _:
								print("Invalid amount")




					case 2:
						message = '''
press 1 for 5000
press 2 for 10000
press 3 for 15000
press 4 for 20000	
						'''
						print(message)
						choice1 = int(input())
						match(choice1):
							case 1:
								five_thousand = 5000.0
								bank_atm_function.withdrawal(five_thousand)
							case 2:
								ten_thousand = 10000.0
								bank_atm_function.withdrawal(ten_thousand)
							case 3:
								fifteen_thousand = 15000.0
								bank_atm_function.withdrawal(fifteen_thousand)
							case 4:
								twenty_thousand = 20000.0
								bank_atm_function.withdrawal(twenty_thousand)
							case _:
								print("Invalid amount")

					case 0: 
						break

					case _:
						print("Invalid input")

		case 3:
			 bank_atm_function.transactions()


		case 0:
			hi = False
		case _:
			print("invalid input")
	
	
	
