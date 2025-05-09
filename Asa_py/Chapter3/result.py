passes = 0
failures = 0

for student in range(10):

 while True:
  result = int(input('Enter result (1=pass, 2=fail): '))
  if result == 1 or result == 2:
   break

 if result == 1:
  passes = passes + 1
 else:
  failures = failures + 1
	
print('passed:', passes)
print('failed:', failures)