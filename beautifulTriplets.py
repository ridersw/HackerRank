def beautifulTriplets(d, arr):
	countOfTriplets = 0
	
	for swi in range(len(arr)):
		tempswi1 = arr[swi] + d
		tempswi2 = tempswi1 + d
		length = len(arr)
		tempArray = arr[swi:length]
		
		if tempswi1 in tempArray and tempswi2 in tempArray:
			countOfTriplets += 1
	
	return countOfTriplets
	
if __name__ == "__main__":
	d = 1
	arr = [2,2,3,4,5]
	result = beautifulTriplets(d, arr)
	print("Result: ", result)