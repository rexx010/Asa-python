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