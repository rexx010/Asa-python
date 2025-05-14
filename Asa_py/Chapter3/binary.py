binary = 11011

decimal = 0
store = 0

while binary != 0:
 div = binary % 10
 decimal = decimal + div * pow(2, store)
 binary = binary // 10
 store += 1

print(decimal)