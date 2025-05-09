password = input('Enter password: ')

num = len(password)

print(num)
if num < 8:
 print("Very weak")

elif num == 8:
 print('Weak')

elif num > 8 and num < 17:
 print('Strong')

elif num > 16:
 print('Very Strong')