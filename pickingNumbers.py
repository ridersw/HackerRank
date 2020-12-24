def pickingNumbers(a):
	count = 0
	temp = 0
	
	a.sort()
	#print("a: ", a)
	
	for i in range(len(a)-1):
		if count < temp:
			count = temp
		temp = 1
		for j in range(i+1, len(a)):
			#print("Comparing ", a[i], " and ", a[j])
			if abs(a[j] - a[i]) > 1:
				break
			else:
				temp += 1
				#print("temp: ", temp)	
	
	#for i in range(len(a)-1):
	#	if abs(a[i+1] - a[i]) < 2:
	#		print("a[i]: " , a[i])
	#		temp += 1
	#	else:
	#		
	#		if count < temp:
	#			count = temp
	#			temp = 0
	#
	#return count
	
	#for i in range(len(a)-1):
	#	print("TempArray: ", tempArray)
	#	tempArray = []
	#	tempNumber = a[i]
	#	print("Count: ", count)
	#	print("Temp: ", temp)		
		
	#	if count < temp:
	#		count = temp
	
	#	temp = 1
	#	tempArray.append(a[i])
	#	for j in range(i+1, len(a)):
	#		if abs(a[i] - a[j]) < 2:
	#			print("--------------------a[i]: " , a[i])
	#			print("a[j]: " , a[j])
	#			temp += 1
	#			tempArray.append(a[j])
	
	
	
	return count

a = [1,2,2,3,1,2]
print("a:", a)
result = pickingNumbers(a)
print(result)