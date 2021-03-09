def maxMin(k, arr):

	length = len(arr)
	
	
	arr.sort()
	
	minDifference = arr[length-1]
	
	#print("Sorted Array: ", arr)
	
	for swi in range(0, length-k+1):
		print("(arr[swi+k-1] - arr[swi]): ", (arr[swi+k-1] - arr[swi]))
		if minDifference > (arr[swi+k-1] - arr[swi]):
			minDifference = (arr[swi+k-1] - arr[swi])
			print("minDifference: ", minDifference)
	
	#print("minDifference: ", minDifference)
	return minDifference
	
	
if __name__ == "__main__":
	k = 3
	arr = [100,200,300,350,400,401,402]
	result = maxMin(k, arr)
	print("Result: ", result)