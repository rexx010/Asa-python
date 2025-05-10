num = int(input('Enter an integer number to provide its factorial: '))

factorial = 1

for number in range(1, num+1):
 factorial = factorial * number

print(f'The factorial of {num} is {factorial}')