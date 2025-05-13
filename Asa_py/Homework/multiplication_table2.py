print('\t','\t','Multiplication_table')
for num in range(1, 10):
 print(f'{num:>4}', end=' ')

print() 
print(f'-------------------------------------------------')
for num in range(1, 10):
 print(f'{num:>2}|', end=' ')

 for number in range(1, 10):
  multiples = num * number
  print(f'{multiples:>4}', end=' ')
 print()

  