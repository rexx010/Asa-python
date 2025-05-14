highest = 0
highest2 = 0

for number in range(1, 11):
  number = int(input('Enter a number: '))

  if number > highest:
   highest2 = highest
   highest = number

  elif number > highest2:
   highest2 = number
   

print(f'The highest number is {highest}')
print(f'The second highest number is {highest2}')