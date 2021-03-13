def minimumAbsoluteDifference(arr):
	arr.sort()
	length = len(arr)
	
	mindif = arr[length-1]
	
	for swi in range(0, len(arr)-1):
		if arr[swi+1] - arr[swi] < mindif:
			mindif = arr[swi+1] - arr[swi]
	return mindif
	
if __name__ == "__main__":
	arr = [3, -7, 0]
	result = minimumAbsoluteDifference(arr)
	print("Result: ", result)