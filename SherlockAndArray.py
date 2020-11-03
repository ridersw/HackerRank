def SherlockAndArray(arr):
	#for i in range(0,len(arr)-1):
	#	templ= 0
	#	tempr = 0
	#	
	#	for j in range(i):
	#		templ += arr[j]
			
	#	for k in range(i+1, len(arr)):
	#		tempr += arr[k]
			
	#	if templ == tempr:
	#		return "YES"
			
	#return "NO"
	
	total = sum(arr)
	print("tot: ", total)
	add = 0
	for i in arr:
		#print("tot-i-add: ", total-i-add)
		if add == total-i-add:
			return "YES"
		add+=i
		#print("Adding 1 to i: ", add)
	return "NO"
	
arr = [2,0,0,0]
result = SherlockAndArray(arr)
print("Result: ", result)