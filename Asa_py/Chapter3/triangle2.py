for a in range(1, 21):
	for b in range(a, 21):
		for c in range(b, 21):
			if (c**2) == (a**2) + (b**2):
					print(f"{c} = {a} + {b}")