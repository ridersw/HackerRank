def hackerlandRadioTransmitters(x, k):
	noOfAntenae = 0
	x.sort()
	length = len(x)
	
	x.append(0)
	
	swi = 0
	
	while swi < length:
		swj = swi
		
		print("First While Loop")
		
		while x[swj] - x[swi] <= k and swj < length:
			swj += 1
		swj -= 1
		noOfAntenae += 1
		
		print("Second While Loop")
		
		swi = swj + 1
		
		while x[swi] - x[swj] <= k and swi < length:
			swi += 1
	
	return noOfAntenae
	
if __name__ == "__main__":
	x = [7, 2, 4, 6, 5, 9, 12, 11]
	k = 2
	result = hackerlandRadioTransmitters(x, k)
	print("No of Antena Needed: ", result)