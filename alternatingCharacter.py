def isAdjacent(arr):
	count = 0
	
	for i in range(len(arr)-1):
		if arr[i] == arr[i+1]:
			count += 1
	
	
	return count
	

arr = "AAABBB"
Result = isAdjacent(arr)
print("Result: ", Result)	