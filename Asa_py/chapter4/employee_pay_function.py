payroll = ['Employee name:', 'Hours Worked:', 'Pay Rate:', 'Federal withholding:', 'State withholding:', 'Total Deduction:']

def add_employee(name, hours, payrate, ftaxRate, staxRate):
	username = name
	workHours = hours
	pay = payrate
	fed = ftaxRate / 100
	state = staxRate / 100

	grosspay = workHours * pay

	federalWithholding = grosspay * fed
	withholding = grosspay * state
	totalDeduction = federalWithholding + withholding
	netPay = grosspay - totalDeduction



	payroll.append(username)
	payroll.append(workHours)
	payroll.append(pay)
	payroll.append(grosspay)
	payroll.append(federalWithholding)
	payroll.append(withholding)
	payroll.append(totalDeduction)
	payroll.append(netPay)
	
	return payroll



def view():
	print(payroll)	
	return payroll


def update_user_information(user_choice):
	for index, value in enumerate(payroll):
		if index == user_choice:
			workHours = hours
			pay = payrate
			fed = ftaxRate / 100
			state = staxRate / 100

			grosspay = workHours * pay

			federalWithholding = grosspay * fed
			withholding = grosspay * state
			totalDeduction = federalWithholding + withholding
			netPay = grosspay - totalDeduction



			payroll.append(username)
			payroll.append(workHours)
			payroll.append(pay)
			payroll.append(grosspay)
			payroll.append(federalWithholding)
			payroll.append(withholding)
			payroll.append(totalDeduction)
			payroll.append(netPay)
	
			return payroll
	