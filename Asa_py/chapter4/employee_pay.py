import employee_pay_function

hello = True
while hello:
	message = """
Welcome to Semicolon Employee Payroll

press 1 to Add Employee Payroll
press 2 to View Employee Payroll
press 3 to Update Employee Payroll
press 4 to exit
"""

	print(message);
	choice = int(input())

	match(choice):
		case 1:
			message = """
Add Employee's Information
			"""

			print(message)
			name = input("Enter employee's name: ")
			hours = int(input("Number of hours work in a week: "))
			payrate = float(input("Enter hourly pay rate: "))
			f_tax_rate = float(input("Enter federal tax withholding rate: "))
			s_tax_rate = float(input("Enter state tax withholding rate: "))
			employee_pay_function.add_employee(name, hours, payrate, f_tax_rate, s_tax_rate)

		case 2:
			message = """
View Employee's Information
			"""
			print(message)
			employee_pay_function.view()

		case 3:
			message = """
Update employee's payroll
			"""
			print(message)
			choose_user = input("Enter your name: ")
			employee_pay_function.update_user_information(choose_user)

		case 4:
			message = """
Thank you
			"""
			print(message)
			hello = False

		case _:
			print("Invalid import")