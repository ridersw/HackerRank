def isValidSubsequence(array, sequence):
    
	lengthOfArray = 0
	lengthOfSequence = 0
	
	while lengthOfArray < len(array) and lengthOfSequence < len(sequence):
		if array[lengthOfArray] == sequence[lengthOfSequence]:
			lengthOfArray += 1
			lengthOfSequence += 1
		else:
			lengthOfArray += 1
	
	#print("lengthOfArray: ", lengthOfArray)
	#print("lengthOfSequence: ", lengthOfSequence)
	
	if lengthOfSequence == len(sequence):
		return True
	else:
		return False

if __name__ == "__main__":
	array= [5, 1, 22, 25, 6, -1, 8, 10]
	sequence=  [1, 6, -1, 10]
	result = isValidSubsequence(array, sequence)
	print("Result: ", result)
	
