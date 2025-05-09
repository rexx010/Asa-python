number = int(input('Enter a five digit number: '))
number2 = number
rev = int(0)
num = int(1)
i = int(0)

while num <= number2:
 i = number2 % 10
 rev = rev * 10 + i
 number2 = number2 // 10

print(rev)

if rev == number:
 print(True)
else:
 print(False)