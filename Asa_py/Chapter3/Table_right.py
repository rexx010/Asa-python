print('number',	'square',	'cube')

for number in range(6):
 digits = number * number
 cube = number ** 3
 print(f'{number:>3}\t{digits:>3}\t{cube:>3}')