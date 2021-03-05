def findMedian(arr):
	arr.sort()
	
	mid = int(len(arr) / 2)
	
	return arr[mid]
	
if __name__ == "__main__":
	arr = [5, 3, 1, 2, 4]
	
	result = findMedian(arr)
	print("Median: ", result)