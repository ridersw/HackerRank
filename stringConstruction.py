def stringConstruction(s):
	newString = ''
	cost = 0
	
	for i in s:
		if i not in newString:
			newString += i
			cost += 1
			
	return cost
	
if __name__ == "__main__":
	s = 'abcabc'
	result = stringConstruction(s)
	print("Cost: ", result)