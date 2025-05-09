sum = 0
average = 0
product = 1
smallest = 1111111111111111111111111111111111111111111111111111111
largest = 0
count = 0

for number in range(4):
 number = int(input('Enter your integer value: '))
 count += 1
 sum += number
 average = sum / count
 product = product * number
 
 #smallest = number
 #largest = number

 if number < smallest:
  smallest = number

 if number > largest:
  largest = number

print(sum)
print(average)
print(product)
print(smallest)
print(largest)
