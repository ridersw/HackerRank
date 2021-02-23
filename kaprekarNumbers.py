def kaprekarNumbers(p, q):
	result = ""
	
	for swi in range(p,q+1):
		square = swi * swi
		
		tempFirstHalf = ""
		tempSecondHalf = ""
		tempStringSquare = str(square)
		
		if len(tempStringSquare) > 1: 
			for swj in range(0,int(len(tempStringSquare)/2)):
				tempFirstHalf += tempStringSquare[swj]
				
			for swj in range(int(len(tempStringSquare)/2), int(len(tempStringSquare))):
				tempSecondHalf += tempStringSquare[swj]
			
			if (int(float(tempFirstHalf)) + int(float(tempSecondHalf))) == swi: 
				#print("Kaprekar Number: ", swi)
				result += str(swi)
				result += " "

		else:
			for swj in range(0,int(len(tempStringSquare))):
				tempFirstHalf += tempStringSquare[swj]
				
			if int(float(tempFirstHalf)) == swi:
				#print("Kaprekar Number: ", swi)
				result += str(swi)
				result += " "
	
	if result == "":
		return "INVALID RANGE"
	else:
		return result
	
	
if __name__ == "__main__":
	p = 1
	q = 99999
	
	result = kaprekarNumbers(p, q)
	print("Result: ", result)