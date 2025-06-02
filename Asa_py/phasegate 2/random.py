

public class Random{



counter = 0;
correctAnswer = 0;
wrongAnswer= 0;


for counter in range(1, 11):
	firstNumber = randint() * 100);
	secondNumber = randint() * 100);
	result = 0;



	if(secondNumber > firstNumber):
		int firstcopy = firstNumber;
		firstNumber = secondNumber;
		secondNumber = firstcopy;

		result = firstNumber - secondNumber
	else:
		result = firstNumber - secondNumber


	attempted = 0;
	while attempted < 2:

		print("The first number is " + firstNumber+ " and the second number is " +secondNumber)

		print("what is the answer?: ")
		userChoice = input.nextInt()

		if(result == userChoice):
			print("correct")
			correctAnswer++
			attempted = 2

		if(result != userChoice):
			print("invalid answer")
			attempted = attempted + 1


print("correct answer is" +correctAnswer+ "/ 10")

