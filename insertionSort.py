def insertionSort1(n, arr):
	
	count = 0
	
	for swi in range(1, len(arr)):
		anchor = arr[swi]
		swj = swi - 1
		
		while swj >= 0 and arr[swj] > anchor:
			arr[swj+1] = arr[swj]
			count += 1
			swj -= 1
			
		arr[swj + 1] = anchor
		count += 1
		print("Array: ", arr)
		
	print("No of Swaps: ", count)
	
if __name__ == "__main__":
	arr = [21, 38, 29, 17, 4, 25, 11, 32, 9]
	insertionSort1(len(arr), arr)
	print(arr)