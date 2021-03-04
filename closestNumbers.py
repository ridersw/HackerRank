def closestNumbers(arr):
	
	arr = sorted(arr)
	
	minDifference = max(arr)
	differenceArray = ""
	
	for swi in range(0, len(arr)-1):
		if arr[swi + 1] - arr[swi] < minDifference:
			minDifference = arr[swi + 1] - arr[swi]
			
			
	print("minDifference: ", minDifference)
	
	for swi in range(0, len(arr)-1):
		if arr[swi + 1] - arr[swi] == minDifference:
			differenceArray += str(arr[swi]) + " "
			differenceArray += str(arr[swi + 1]) + " "
	
	return differenceArray
	
if __name__ == "__main__":
	#arr = [5, 2, 3, 4, 1]
	arr = [-20, -3916237, -357920, -3620601, 7374819, -7330761, 30, 6246457, -6461594, 266854 ]
	result = closestNumbers(arr)
	print("Result: ", result)