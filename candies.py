def candies(n, arr):
	candiesArray = [1] * n
	
	for swi in range(0, n-1):
		if arr[swi+1] > arr[swi]:
			candiesArray[swi+1] = candiesArray[swi] + 1
	
	#print("arr         : ", arr)
	#print("candiesArray: ", candiesArray)
	
	for swi in range(n-1, 0, -1):
		if arr[swi-1] > arr[swi] and candiesArray[swi-1] <= candiesArray[swi]:
			candiesArray[swi-1] = candiesArray[swi] + 1
	
	#print("candiesArray: ", candiesArray)
	
	return sum(candiesArray)
	
def modifyCandyCount(candiesArray):
	for swi in range(0, len(arr)-1):
		if arr[swi] < arr[swi+1]:
			if candiesArray[swi] >= candiesArray[swi+1]:
				candiesArray[swi+1] = candiesArray[swi] + 1
		elif arr[swi] > arr[swi+1]:
			if candiesArray[swi] <= candiesArray[swi+1]:
				candiesArray[swi] = candiesArray[swi+1]+1

	return candiesArray
	
if __name__ == "__main__":
	n = 10
	#n = 3
	arr = [2 , 4, 2, 6, 1, 7, 8, 9, 2, 1]
	#arr = [1, 2, 2]
	result = candies(n, arr)
	print("Minimum Candies: ", result)