import math

e_constant = 1.0

for number in range(1, 11):
	e_constant += 1 / math.factorial(number)
print(e_constant)