number = int(input('Enter a number with five integers: '))

seperator = 10000
while number != 0:
	output = number // seperator
	print(output, end='\t')
	number = number % seperator
	divisor //= 10