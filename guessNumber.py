import random

def guessNumber(number):
	
	computerGuess = random.randint(5, number)
	print("computerGuess: ", computerGuess)
	userGuess = 0
	
	while userGuess != computerGuess:
		userGuess = int(input("Guess the Number Buddy: "))
		
		
		if userGuess == computerGuess:
			print("You Did it!")
			
		elif abs(userGuess - computerGuess) <= (computerGuess / 10):
			print("Try Again, You are too close")
		
		elif abs(userGuess - computerGuess) <= (computerGuess / 5):
			print("Try Again, You are close")
			
		else:
			print("Oh come on!")




if __name__=="__main__":
	guessNumber(10)