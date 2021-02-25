def anagram(str):
	if len(str) % 2 != 0:
		return -1
		
	str = list(str)
		
	half = int(len(str)/2)
	length = int(len(str))
	
	count = 0
	
	tempStr1 = str[:half]
	tempStr2 = str[half:length]
	
	#str = list(str)
	
	#tempStr1 = list(tempStr1)
	#tempStr2 = list(tempStr2)
	
	#print("tempStr1: ", tempStr1)
	#print("tempStr2: ", tempStr2)
	
	swi = 0
	swj = half - 1
	
	while half > 0:
		#print("tempStr1[swi]: ", tempStr1[swi])
		#print("tempStr2[swj]: ", tempStr2[swj])
		
		if tempStr1[swi] not in tempStr2:
			count += 1
		else:
			tempIndex = tempStr2.index(tempStr1[swi])
			tempStr2.pop(tempIndex)
			
		swi += 1
		swj -= 1
		half -= 1
	
	return count
	
	
if __name__ == "__main__":
	s = "xaxbbbxx"
	result = anagram(s)
	print("Result: ", result)
	