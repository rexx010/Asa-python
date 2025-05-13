for num in range(0, 11):
 for number in range(num):
  print(f'{'*':>1}', end=' ')
 print()

print()
for num in range(11, 0, -1):
 for number in range(num):
  print(f'{'*':>1}', end=' ')
 print()

print()

num = 10
for number in range(num):
 for space in range(number, num):
  print(' ', end=' ')
 for asterisk in range(number+1):
  print(f'{'*'}', end=' ')
 print()

print()
num = 10
for number in range(num):
 for space in range(number+1):
  print(' ', end=' ')
 for asterisk in range(number, num):
  print(f'{'*'}', end=' ')
 print()