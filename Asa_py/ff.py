def userinput_check(user_input):

	if not user_input or user_input.isspace():
		return "Input cannot be empty, Try again"

	elif len(user_input) != 1:
		return "Invalid, Too many inputs"

	elif user_input.isdecimal():
		return True

	else:
		return "Invalid character. Pick a number"



def name_check(name):

	if not name or name.isspace():
		return "Name cannot be empty"

	if name.startswith(" ") or name.endswith(" "):
		return "Invalid space present"

	new_name = name.replace(" ","")

	if len(new_name) < 2 or len(new_name) > 30:
		return "Character limit error"

	if any(char == " " for char in name[1:3]):
		return "Invalid name"

	if new_name.isalpha():
		return True
	else:
		return "Invalid name"




def hours_worked_check(working_hrs):

	if not working_hrs or working_hrs.isspace():
		return "Name cannot be empty"

	if not working_hrs.isdecimal():
		return "Invalid characters present"

	working_hrs = int(working_hrs)

	if working_hrs <= 0:
		return "Invalid hours entered"

	if working_hrs > 168:
		return "There are only 168 hours in a week"

	else: return True
	



def payments_check(pay_per_hr):

	if not pay_per_hr or pay_per_hr.isspace():
		return "Name cannot be empty"

	temp = pay_per_hr.replace('.','',1)

	if not temp.isdecimal():
		return "Invalid characters present"

	pay_per_hr = float(pay_per_hr)

	if pay_per_hr != round(pay_per_hr, 2) or pay_per_hr <= 0:
		return "Invalid amount entered"

	else: return True




def tax_check(tax):
	
	if not tax or tax.isspace():
		return "Name cannot be empty"

	temp = tax.replace('.','',1)

	if not temp.isdecimal():
		return "Invalid characters present"

	tax = float(tax)

	if tax != round(tax, 2):
		return "Invalid amount entered"

	if tax <= 0 or tax >= 100:
		return "rate can only in percentage(1-100)"

	else: return True




def employee_details(payroll):

	name = str(input("Employee's name: "))
	
	if name in payroll.keys():
		return "This employee already exists"

	working_hrs = str(input("How many hours did this employee work this week: "))
	pay_per_hr = str(input("What is the pay-per-hour rate: "))
	fed_tax = str(input("What is the federal withholding tax rate: "))
	state_tax = str(input("What is the state withholding tax rate: "))


	if name_check(name) != True:
		return name_check(name)
	if hours_worked_check(working_hrs) != True:
		return hours_worked_check(working_hrs)
	if payments_check(pay_per_hr) != True:
		return payments_check(pay_per_hr)
	if tax_check(fed_tax) != True:
		return tax_check(fed_tax)
	if tax_check(state_tax) != True:
		return tax_check(state_tax)

	working_hrs = int(working_hrs)
	pay_per_hr = float(pay_per_hr)
	fed_tax = float(fed_tax)
	state_tax = float(state_tax)
	
	return (name, working_hrs, pay_per_hr, fed_tax, state_tax)




def add(payroll, details):

	name, working_hrs, pay_per_hr, fed_tax, state_tax = details

	gross = round((working_hrs * pay_per_hr), 2)
	f_tax = round((gross * (fed_tax/100)), 2)
	s_tax = round((gross * (state_tax/100)), 2)
	total = round((f_tax + s_tax), 2)
	net_pay = round((gross - total), 2)

	new_name = name.lower()

	payroll[new_name] = {'Employee name' : name, 'Hours worked' : working_hrs, 'Pay rate' : f"£{pay_per_hr}", 'Gross pay' : f"£{gross}", 'Deductions' : ' ', '\tFederal withholding rate' : f"£{f_tax}", '\tState withholding rate' : f"£{s_tax}", '\tTotal deduction' : f"£{total}", 'Net pay' : f"£{net_pay}"}

	return "employee payroll added>>>"




def view(payroll):

	if len(payroll) == 0:
		print("There are no payrolls available to view")

	else:
		for key, details in payroll.items():
			for detail, info in details.items():
				print(f"{detail}: {info}")
			print()



def update(payroll, name):

	name = name.lower()

	if name not in payroll.keys():
		return False
	else:
		payroll.pop(name)
		return True