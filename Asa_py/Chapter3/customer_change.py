quaters = 25
dimes = 10
pennies = 1

item_cost_in_cent = int(input('Enter the cost of the item in cent: '))
purchase_price = int(input('Enter the price in dollar: '))

purchase_price = purchase_price * 100

change = purchase_price - item_cost_in_cent
quater = change // quaters

dime = change % quaters // dimes

pennie = change % quaters % dimes // pennies

print('The purchaser is due ', change,'cent')
print('your remaining change is')
print(quater,'quaters')
print(dime,'dimes')
print(pennie,'pennies')