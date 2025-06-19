import random

list_of_ten_number = []

def creation_of_list():
    for num in range(10):
        number = random.randint(1, 50)
        list_of_ten_number.append(number)
    return list_of_ten_number

def the_length_of_the_list(list_of_ten_number):
    count = 0
    for num in list_of_ten_number:
        count += 1
    return count

def the_sum_of_even_elements(list_of_ten_number):
    sum_even = 0
    index_count = 0
    for value in list_of_ten_number:
        if index_count % 2 == 0:
            sum_even += value
        index_count += 1
    return sum_even

def sum_of_odd_elements(list_of_ten_number):
    sum_odd = 0
    index_count = 0
    for value in list_of_ten_number:

        if index_count % 2 != 0:
            sum_odd += value
        index_count += 1
    return sum_odd

def elements_at_third_index(list_of_ten_number):
    multi = 1
    for index in range(2, 10, 3):
        multi *= list_of_ten_number[index]
    return multi

def calculate_all_element_average(list_of_ten_number, number_length):
    total_ans = 0
    average_of_sum = 0
    for item in list_of_ten_number:
        total_ans += item
    average_of_sum = float(total_ans / number_length)
    return average_of_sum
