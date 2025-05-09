principal = float(input('Enter the deposit amount: '))

rate = float(input('Enter the rate amount: '))

year = int(input('Enter the year: '))



for number in range (year, 1, -1):
 amount = principal * (1 + rate) ** number
 print(round (amount,2))