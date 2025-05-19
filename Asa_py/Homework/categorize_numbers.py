def get_numbers(*args, divisible_by=2):


	if divisible_by == 0:
		return 'not divisible by zero'

	

	nums = []
	for num in args:
		if num % divisible_by == 0:
			nums.append(num)

		


	if nums:
		return nums
	else:
		return 'no divisible number found'

			
	




num1 = 10
num2 = 15
num3 = 21
num4 = 30

print(get_numbers(num1, num2, num3, num4))

	