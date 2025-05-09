while True:
 n = int(input('Enter an integer: '))
 if n > 1:
  break

for number in range(n, 0, -1):
 print(number)
 if number == 1:
  print("Blast Off!")