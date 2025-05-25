def mystery(x):
 y = 0
 for value in x:
  y += value ** 2
 return y


num = [1, 2, 3, 4, 5] 
print(mystery(num))