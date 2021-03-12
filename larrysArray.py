def larrysArray(A):

	count = 0
	
	for swi in range(1,len(A)):
		#print("swi: ", swi)
		for swj in range(0,swi):
			#print("		swj: ", swj)
			#print("A[swi]: ", A[swi], " and A[swj]: ", A[swj])
			if A[swj] > A[swi]:
				count += 1
				#print("Count Increase")
		#print("Count: ", count)
	
	#print("Count: ", count)
	if count % 2 == 0:
		return "YES"
	else:
		return "NO"
	
if __name__ == "__main__":
	#array = [1,6,5,2,4,3]
	#result = larrysArray(array)
	#print("Sorted: ", result)
	
	array = [9, 6, 8, 12, 3, 7, 1, 11, 10, 2, 5, 4]
	result = larrysArray(array)
	print("Sorted: ", result)
	
	array = [17, 21, 2, 1, 16, 9, 12, 11, 6, 18, 20, 7, 14, 8, 19, 10, 3, 4, 13, 5, 15]
	result = larrysArray(array)
	print("Sorted: ", result)
	
	array = [5, 8, 13, 3, 10, 4, 12, 1, 2, 7, 14, 6, 15, 11, 9]
	result = larrysArray(array)
	print("Sorted: ", result)
	
	array = [8, 10, 6, 11, 7, 1, 9, 12, 3, 5, 13, 4, 2]
	result = larrysArray(array)
	print("Sorted: ", result)
	
	array = [7, 9, 15, 8, 10, 16, 6, 14, 5, 13, 17, 12, 3, 11, 4, 1, 18, 2]
	result = larrysArray(array)
	print("Sorted: ", result)