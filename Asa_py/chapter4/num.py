import random

computer_num = random.randrange(1, 1001)

while True:
	user_num = int(input('Guess my number between 1 and 1000: '))


	if(user_num < computer_num):
		print("Too low. Try again")

	if(user_num > computer_num):
		print("Too high. Try again")

	if(user_num == computer_num):
		print("Congratulations. You guessed the number!")
		print("Do you want to continue?")
		question = int(input('Press 0 to stop and 1 to continue: '))
		if question == 0:
			break