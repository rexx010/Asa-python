gallons = 0
miles = 0
total = 0
gallon = 0
quit = 0

while quit != -1:
	gallon = float(input('Enter gallons used: '))
	mile = int(input('Enter miles drivened: '))
	quit = int(input('press -1 to end:'))

	gallons += gallon 
	miles += mile
	
total = miles / gallons

print(f'The overall average miles/gallon was {total:,.2f}')