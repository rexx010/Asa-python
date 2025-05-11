highest_name = ' '
highest = 0

for number in range(0, 5):
  name = input('Enter your name: ')
  score = int(input('Enter you student score: '))

  if score > highest:
   highest = score
   highest_name = name

print(f'The name of the student with the highest score is {highest_name} with a score of {highest}')
