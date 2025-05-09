number = int(input('Enter a five digit number: '))

number2 = number
one = number2 //10000 % 10
two = number2 //1000 % 10
three = number2 // 100 %10
four = number2 // 10 % 10
five = number2 % 10

rev = one''two''three''four''five
print(one,two,three,four,five)
print(rev)
