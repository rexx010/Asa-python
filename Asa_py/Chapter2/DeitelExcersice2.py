#exercise 2


rating = input('Enter an integer rating between 1 and 10: ')
print(rating)

'''the issue with this line of code is that we are expecting to get an integer input from the user but anything that comes in through the input is a string by default, except we give it an interger type.'''


rating = int(input('Enter an integer rating between 1 and 10: '))
print(rating)

#now we should be having and integer output