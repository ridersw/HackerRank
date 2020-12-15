def lilysHomework(arr):
	tempArray1 = arr.copy()
	tempArray1.sort()
	
	tempArray2 = arr.copy()
	tempArray2.sort(reverse=True)
	
	count1 = 0
	count2 = 0
	
	for i in range(len(arr)):
		if arr[i] != tempArray1[i]:
			count1 += 1
			
	
	
	for i in range(len(arr)):
		if arr[i] != tempArray2[i]
		count2 += 1
	
	count = round(count / 2)
	
	return count

arr = [7,15,12,3]
result = lilysHomework(arr)
print(result)