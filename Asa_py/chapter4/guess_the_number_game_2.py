import random

computer_num = random.randrange(1, 1001)
counter = 0
while True:
	
	user_num = int(input('Guess my number between 1 and 1000: '))

	if counter > 10:
		print("Your head don dry Oga\nYou should be able to do better!\nWhy should it take no more than 10 guesses?")

	counter += 1

	if(user_num < computer_num):
		print("Too low. Try again")

	if(user_num > computer_num):
		print("Too high. Try again")

	if(user_num == computer_num):
		if counter < 10:
			print("Either you know the secret or you got lucky!")
		print("Congratulations. You guessed the number!")
		print("Do you want to continue?")
		question = int(input('Press 0 to stop and 1 to continue: '))
		if question == 0:
			break