def multiples(num1, num2):
	result = 0
	for numbers in range(0, num2):
		result += num1
	return result


num1 = int(input('Enter the first digit: '))
num2 = int(input('Enter the second digit: '))

print(multiples(num1, num2))