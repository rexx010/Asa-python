"""def unpack_collection(collection):
    result = [0, 0, 0, 0]
    for index in range(4):
        result[index] = collection[index]
    return result"""
#print(unpack_collection(number))


number = [1, 2, 3, 4, 5, 6, 7, 8]
def unpack_collection(numbers):
    first_number, second_number, third_number, *others = numbers
    return first_number, second_number, third_number, others
print(unpack_collection(number))

def slice_collection(collection):
    return collection[: 3: ]
print(slice_collection(number))

def sorth_collection(collection):
    collection.sort(reverse=True)
    return collection
print(sorth_collection(number))

number_filter = [1, 2, 3, 4, 5, 6, 7, 8, 9]

def isOdd(number_filter):
    return number_filter % 2 == 1

def filter_collection(collection):
    return list(filter(isOdd, collection))
print(filter_collection(number_filter))

filtered_value = list(filter(isOdd, number_filter))
print(filtered_value)

def filter_with_lambda(collection):
    return list(filter(lambda number: number % 2 == 1, collection))

print(filter_with_lambda(number_filter))

def sum_collection(number_filter):
    sum_all_numbers = sum(map(lambda number: number, number_filter))
    return sum_all_numbers
print(sum_collection(number_filter))