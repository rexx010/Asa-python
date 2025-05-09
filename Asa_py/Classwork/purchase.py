"""
collect input from the user and store it in a variable;
create another variable to store the discount price;
check if the price falls in between 1000 and 10000, then multply it by 5%;
check if the price falls in between 10000 and 50000, then multply it by 10%;
check if the price falls in above 50000, then multply it by 20%
"""

discount_price = 0
price = 0
purchase = int(input('Enter your purchase amount: '))
if purchase < 1:
 print('invalid input')
if purchase > 1:
 
 if purchase > 999 and purchase < 10001:
  discount_price = purchase * 0.05
  price = purchase - discount_price
  print(f'discount = {discount_price:,.2f}')
  print(f'Total amount = {price:,.2f}')

 elif purchase > 10000 and purchase < 50001:
  discount_price = purchase * 0.10
  price = purchase - discount_price
  print(f'discount = {discount_price:,.2f}')
  print(f'Total amount = {price:,.2f}')

 elif purchase > 50000:
  discount_price = purchase * 0.20
  price = purchase - discount_price
  print(f'discount = {discount_price:,.2f}')
  print(f'Total amount = {price:,.2f}')
