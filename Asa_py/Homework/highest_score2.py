highest_name = ' '
highest = 0
highest_name2 = ' '
highest2 = 0

no_of_student = int(input('Enter number of student score: '))

for number in range(no_of_student):
  name = input('Enter your name: ')
  score = int(input('Enter you student score: '))

  if score > highest:
   highest2 = highest
   highest_name2 = highest_name2

   highest = score
   highest_name = name

  elif score > highest2:
   highest2 = score
   highest_name2 = name

print(f'The name of the student with the highest score is {highest_name} with a score of {highest}')
print(f'The name of the student with the highest score is {highest_name2} with a score of {highest2}')
