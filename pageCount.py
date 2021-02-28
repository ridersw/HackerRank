def pageCount(numberOfPages, pageNumber):
	numberOfForwardFlips = 0
	numberOfBackwardFlips = 0
	
	if int(numberOfPages % 2) == 0:
		numberOfPages += 1
		
	print("numberOfPages: ", numberOfPages)
	
	numberOfForwardFlips = numberOfFlips(numberOfPages, pageNumber, 1)
	numberOfBackwardFlips = numberOfFlips(numberOfPages, pageNumber, -1)
	
	return min(int(numberOfForwardFlips), int(numberOfBackwardFlips))
	
def numberOfFlips(numberOfPages, pageNumber, signal):	
	
	flip = 0
	
	if signal > 0:
		for swi in range(0, numberOfPages, 2):
			if swi == pageNumber or (swi + 1) == pageNumber:
				return flip
			
			flip += 1
				
	else:
		for swi in range(numberOfPages, 0, -2):
			if swi == pageNumber or (swi - 1) == pageNumber:
				return flip
			
			flip += 1
	
	
if __name__ == "__main__":
	numberOfPages = 5
	pageNumber = 4
	result = pageCount(numberOfPages, pageNumber)
	print("Result: ", result)