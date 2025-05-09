principal = float(input('Enter a principal amount: '))

rate = float(input('Enter the annual rate: '))

duration = float(input('Enter the mortgage duration: '))

rate = float(rate /100/ 12)

duration = float(duration * 12)

sum1 = float(principal * rate * (1 + rate) ** duration)
sum2 = float((1 + rate) ** duration - 1)

total = float(sum1 / sum2)

print(total)










