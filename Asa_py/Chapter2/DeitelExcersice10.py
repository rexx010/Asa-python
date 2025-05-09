num1 = int(input('Enter an integer number'))
num2 = int(input('Enter an integer number'))
num3 = int(input('Enter an integer number'))

sum = num1 + num2 + num3
average = sum / 3
product = num1 * num2 * num3

smallest = num1
largest = num1

if num2 < smallest:
 smallest = num2

if num3 < smallest:
 smallest = num3

if num2 > largest:
 largest = num2

if num3 > largest:
 largest = num3

print('The sum is', sum)
print('The average is', average)
print('The product is', product)
print('The smallest is', smallest)
print('The largest is', largest)