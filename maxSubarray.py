def maxSubarray(arr):
	
	if max(arr)<0:
		return(max(arr),max(arr))
	a=0
	best_sum = 0  
	current_sum = 0
	for i in arr:
		if i>0:
			a+=i

		current_sum = max(0, current_sum + i)
		best_sum = max(best_sum, current_sum)
    
	return best_sum,a
	
if __name__ == "__main__":
	arr = [1]
	result = maxSubarray(arr)
	print("Result: ", result)
	
	arr = [-1, -2, -3, -4, -5, -6]
	result = maxSubarray(arr)
	print("Result: ", result)
	
	arr = [1, -2]
	result = maxSubarray(arr)
	print("Result: ", result)
	
	arr = [1, 2, 3]
	result = maxSubarray(arr)
	print("Result: ", result)
	
	arr = [-10]
	result = maxSubarray(arr)
	print("Result: ", result)
	
	arr = [1, -1, -1, -1, -1, 5]
	result = maxSubarray(arr)
	print("Result: ", result)