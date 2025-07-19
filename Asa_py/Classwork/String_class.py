text = 'Lion King'
text2 = 'Lion'

print(f'[{text:^10}]')
print(f'{text:^10}')

print(f'[{text2:^10}]')
print(f'{text2:^10}')

print(len(f'[{text:^10}]'))
print(len(f'{text:^10}'))

print(len(f'[{text2:^10}]'))
print(len(f'{text2:^10}'))

text_aligned = f'[{text:^10}]'
print(text_aligned)
print(len(text_aligned))

num1 = 567
num2 = 39.980
print('{:d} {:.2f}'.format(num1, num2))
print('{:.1f}'.format(num1, num2))

fruit = 'apple for food'
print('-'.join(fruit))

fruit2 = 'apple', 'for', 'food'
print('-'.join(fruit2))

place = ' jungle race on '
print(place.strip())

place2 = ' \t\tjungle\t\t    '
print(place2.strip())

name = 'chIef okAfor'
print(name.capitalize())
print(name.title())
print(name.lower())
print(name.upper())

print('cat' > 'dog')
print('cat' > 'car')
print('dog' == 'dog')
print('eddy' > 'oba')

word = 'polymorphism'
print(word.find('morph'))
print(word.index('morph'))
print(word.find('moy'))
#print(word.index('moy'))

sentence = 'i love cats'
print(sentence.replace('cats', 'dogs'))

words = 'Time bound'
print(words.split())

word1 = 'one two three'.split()
print(word1)

raw_str = r"C:\Users\Name"
print(raw_str)

import re
pattern = "02935"
print(True if re.search(pattern, '0293') else False)

pattern2 = "yahoo.com"
text = "oba@yahoo.com"
replace = "gmail.com"
print(re.sub(pattern2, replace, text))

textss = "letter story comprehension"
pattern3 = ' '
print(re.split(pattern3, textss))

money = '80,000,000'
pattern4 = ','
pattern5 = '.'
first_in = re.split(pattern4, money)
print(first_in)
second_in_str = ''.join(first_in)
print(type(second_in_str))
result = re.sub(pattern5, '', second_in_str)
print(result)
