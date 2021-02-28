def marsExploration(s):
	countOfLetters = 0
	
	compareMessage = 'SOS'
	
	if int(len(s) / 3) != 0:  
		compareMessage *= (int(len(s) / 3) + 1)
	else:
		compareMessage *= (int(len(s) / 3))

	for swi in range(len(s)):
		if s[swi] != compareMessage[swi]:
			countOfLetters += 1
	
	return countOfLetters
	
if __name__ == "__main__":
	s = 'ABC'
	result = marsExploration(s)
	print("Result: ", result)