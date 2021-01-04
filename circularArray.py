def circularArrayRotation(a, k, queries):
	
	tempArray = [0] * len(a)
	indexArray = []
	j = 0
	
	k = k % len(a)
	
	for i in range(k, len(a)):
		tempArray[i] = a[j]
		j += 1
		print("tempArray (1): ",tempArray)
		
	for i in range(0,k):
		tempArray[i] = a[j]
		j += 1
		print("tempArray (2): ",tempArray)
		
	for i in range(len(queries)):
		temp = queries[i]
		indexArray.append(tempArray[temp])
		
	return indexArray
		
	
	
if __name__ == "__main__":
	a = [3, 4, 5]
	k = 2
	queries = [1, 2]
	
	result = circularArrayRotation(a, k, queries)
	print("Result: ", result)