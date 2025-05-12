highest = 0

for number in range(0, 5):
  number = int(input('Enter a number: '))

  if number > highest:
   highest = number

print(f'The highest number is {highest}')