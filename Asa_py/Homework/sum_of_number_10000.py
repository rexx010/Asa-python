def add_number(number):

 number_copy = number
 number_deducter = 0
 sum_of_number = 0
 
 while number_copy != 0:
  number_deducter = number_copy % 10
  sum_of_number += number_deducter
  number_copy = number_copy // 10

 return sum_of_number


while True:
 number = int(input('Enter integers within 1 to 10,000: '))
 if number > 1 and number < 10000:
  break

output = add_number(number)
print('sum_of_number', output)