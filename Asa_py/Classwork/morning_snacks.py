nums = [10, 20, 30, 40, 50]
count = 1
for num in nums:
    if count == 3:
        print(num)
    count += 1

colors = ['red', 'green', 'blue']
colors.remove("blue")
colors.append('yellow')
colors.append('purple')
print(colors)

list_elements = [1, 2, 3, 4, 5]
list_elements.remove(3)
print(list_elements)

list_name = [len('Alice'), len('Bob'), len('Charlie')]
print(list_name)

nums = [4, 1, 3, 9, 2]
arranged = sorted(nums)
print(arranged)

def new_numbers(numbers):
    new_list = []
    counter = 0
    for num in numbers:
        if counter % 2 == 0:
            new_list.append(num)
        counter += 1
    return new_list

numbers = [1,2,3,4,5,6,7,8,9]
print(new_numbers(numbers))

a = [1, 2, 3]
b = [4, 5, 6]
c = a + b
print(c)

list = ['lamb', 'kit', 'yam', 'king', 'dogs', 'man']
new_list = []
for item in list:
    if len(item) > 3:
        new_list.append(item)
print(new_list)