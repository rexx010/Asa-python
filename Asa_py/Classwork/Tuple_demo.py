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
