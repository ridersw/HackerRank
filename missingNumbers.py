def missingNumbers(arr, brr):
	freq = {}
			
	for item in brr:
		if item in freq:
			freq[item] += 1
		else:
			freq[item] = 1
			
	for item in arr:
		if item in freq:
			freq[item] -= 1
	temp = ""
	for key, value in freq.items():
		if value >= 1:
			temp = temp +str(key) + " "
	
	#print("temp: ", temp)
	
	return temp
	

arr = [203, 204, 205, 206, 207, 208, 203, 204, 205, 206]
brr = [203, 204, 204, 205, 206, 207, 205, 208, 203, 206, 205, 206, 204]
result = missingNumbers(arr, brr)
print("Result: ", result)