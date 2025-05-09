investment_amount = int(input('Enter your investment amount: '))
duration_in_years = int(input('Enter the number year: '))
interest_rate = int(input('Enter the rate amount: '))

interest_rate = interest_rate / 100

for number in range(1, duration_in_years+1):
 return_amount = investment_amount * (1 + interest_rate) ** number
 print(f'The yearly interest amount is:( year {number}	#{return_amount:,.2f})')