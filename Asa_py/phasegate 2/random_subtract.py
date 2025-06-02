import random

counter = 0;
correctAnswer = 0;
wrongAnswer= 0;


for counter in range(1, 11):
	firstNumber = random.randrange(1, 100)
	secondNumber = random.randrange(1, 100)
	result = 0;


	if(secondNumber > firstNumber):
		firstcopy = firstNumber;
		firstNumber = secondNumber;
		secondNumber = firstcopy;

		result = firstNumber - secondNumber
	else:
		result = firstNumber - secondNumber
	

		attempted = 0;
		while attempted < 2:
				
			correctAnswer = 0;
			wrongAnswer= 0;
			print(f'The first number is ', {firstNumber} ,' and the second number is ', {secondNumber})
		
			print("what is the answer?: ")
			userChoice = int(input())

			if result == userChoice:
				print("correct")
				correctAnswer + 1
				attempted = 2

			if result != userChoice:
				print("invalid answer")
				attempted = attempted + 1


			print(f'correct answer is', {correctAnswer} , '/ 10')

