fivenumber = int(input('Enter 5 digit numbers: '))

one = fivenumber // 10000 % 10
two = fivenumber // 1000 % 10
three = fivenumber // 100 % 10
four = fivenumber // 10 % 10
five = fivenumber % 10
print(one, two, three, four, five)