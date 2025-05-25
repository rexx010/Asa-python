student_score1 = 50
student_score1 = 50
student_score1 = 50
student_score1 = 50
student_score1 = 50

cart = ['banana', 33, 'juice', 2.5, ['fish', 'palm oil'], True]
cart[4].insert(0, 6)
print(cart[4][1])
print()

print(len(cart))
print()

#	   0   1   2   3  4
scores = [50, 34, 45, 51, 25]

print("we have", len(scores), "scores")
print()

print(scores[0:3:2])
print()

x, y = scores[0:3:2]
print(x, y)
print()

print(len(scores))
print()

print(scores[2])
print()

for score in scores:
	print(score)
print()

for idx in range(len(scores)):
	print(idx)
print()

for index, value in enumerate(cart):
	print(index, value)
print()

print(list(enumerate(cart))[4])

#scores.append(99)
#scores.pop(1)
cart[4].insert(0, 6)
#scores.extend([34, 67, 87, 'oba'])
#new_list = cart + scores
print(scores[0:5:2])
print()

