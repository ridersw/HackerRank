def isValid(s):
	freq = {}
	
	for i in range(len(s)):
		temp = s[i]
		if s[i] in freq:
			freq[temp] += 1
		else:
			freq[temp] = 1
	
	temp = []
	
	for key, value in freq.items():
		temp.append(value)
	
	temp.sort()
	
	print("temp: ", temp)
	
	freq = {}
	
	for i in range(len(temp)):
		temp1 = temp[i]
		if temp[i] in freq:
			freq[temp1] += 1
		else:
			freq[temp1] = 1
		
	print("freq: ", freq )
	count = 0		
	
	for key, value in freq.items():
		if value >= 2:
			count += 1
		
		if count >= 2:
			return "NO"
	
	return "YES"
	
s = "aaaabbcc"
result = isValid(s)
print("Result: ", result)