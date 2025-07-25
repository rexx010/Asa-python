import re

text = "The Silent Boy is sick today , call this number 09161171012"
pattern = re.findall(r'\w+\s+', text)
print(pattern)
pattern1 = re.compile(r'[a-zA-Z]+')
match = re.findall(pattern1, text)

print(match)