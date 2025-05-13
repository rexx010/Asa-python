highest_name = ' '
highest = 0

no_of_student = int(input('Enter number of student score: '))

for number in range(no_of_student):
  name = input('Enter your name: ')
  score = int(input('Enter you student score: '))

  if score > highest:
   highest = score
   highest_name = name

print(f'The name of the student with the highest score is {highest_name} with a score of {highest}')
