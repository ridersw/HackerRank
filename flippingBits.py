import numpy as np

def flippingBits(n):
	
	binNum = convertToBinary(n)
	
	binaryNumber = ('0' * (32 - len(str(binNum)))) + binNum
	
	afterFlip = flipFunction(binaryNumber)
	
	decimalNumber = int(afterFlip,2)
	
	return decimalNumber

def flipFunction(bN):
	flipString = ''
	
	for item in bN:
		if item == '0':
			flipString += '1'
		else:
			flipString += '0'
			
	return flipString
	
def convertToBinary(dN):
	return bin(dN).replace("0b","")
	
if __name__ == "__main__":
	n = 2147483647
	result = flippingBits(n)
	print("Result: ", result)