def cost(B):
	costOfB = 0
	
	testCase1 = 0 #B[swi] - 1
	testCase2 = 0 #B[swi] - B[swi-1]
	testCase3 = 0 #B[swi-1] - 1
	
	
	for swi in range(1, len(B), 1):
		testCase1 = B[swi] - 1
		testCase2 = B[swi] - B[swi-1]
		testCase3 = B[swi-1] - 1
		
		if testCase1 == max(testCase1, testCase2, testCase3):
			B[swi-1] = 1
		elif testCase3 == max(testCase1, testCase2, testCase3):
			B[swi] = 1
	
	print("Before Last Element Operations: B: ", B)	
		
	length = len(B)
	if B[length-2] > B[length-1]:
		B[length-1] = 1
		
	print("After Last Element Operations: B: ", B)	
	
	for swi in range(1, len(B)):
		costOfB += abs(B[swi] - B[swi-1])
	
	return costOfB
	
if __name__ == "__main__":
	B = [3, 15, 4, 12, 10]
	result = cost(B)
	print("Cost: ", result)
	B = [4, 7, 9]
	result = cost(B)
	print("Cost: ", result)
	B = [100, 2, 100, 2, 100]
	result = cost(B)
	print("Cost: ", result)