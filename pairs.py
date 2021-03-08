def pairs(k, arr):
	countOfPairs = 0
	
	arr.sort()
	
	#for swi in range(0, len(arr)):
	#	if (arr[swi] + k) in arr:
	#		countOfPairs += 1
	
	swi = 0
	swj = 0
	
	while swi < len(arr) and swj < len(arr):
		temp = arr[swj] - arr[swi]
		if temp < k:
			swj += 1
		elif temp > k:
			swi += 1
		else:
			countOfPairs += 1
			swi += 1
			swj += 1
	
	return countOfPairs
	
if __name__ == "__main__":
	k = 2
	arr = [1,5,3,4,2]
	result = pairs(k, arr)
	print("No. of Pairs: ", result)