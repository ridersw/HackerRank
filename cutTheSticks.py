def cutTheSticks(arr):
	result = []
	count = len(arr)
	uniqueElements = []
	
	for number in arr:
		if number not in uniqueElements:
			uniqueElements.append(number)
			
	uniqueElements.sort()
	
	for number in uniqueElements:
		result.append(count)
		
		tempNumber = arr.count(number)
		count -= tempNumber
		tempNumber = 0
	
	
	return result
	
	
if __name__== "__main__":
	arr = [5,4,4,2,2,8]
	result = cutTheSticks(arr)
	print("result: ", result)