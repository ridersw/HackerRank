def theLoveLetterMystery(s):

	alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
	
	swi = 0
	swj = len(s)-1
	
	numberOfOperations = 0
	
	while swi <= swj:
		print("Comparing ", s[swi], " and ", s[swj])
		print("Index of ", s[swi], " is ", alphabets.index(s[swi]), " and ", s[swj], " is ", alphabets.index(s[swj]))
		#print("Difference is ", alphabets.index(s[swi])) - alphabets.index(s[swj])
		
		if s[swi] != s[swj]:
			tempNum1 = alphabets.index(s[swi])
			tempNum2 = alphabets.index(s[swj])
			numberOfOperations += abs(tempNum1 - tempNum2)
			#print("numberOfOperations: ", numberOfOperations)
		
		swi += 1
		swj -= 1
		
	return numberOfOperations
	
if __name__ == "__main__":
	s = "abcd"
	result = theLoveLetterMystery(s)
	print("Result: ", result)