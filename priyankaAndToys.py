def toys(w):
	numberOfContainers = 1
	
	w.sort()
	
	minElement = w[0]
	
	for swi in range(1, len(w)):
		#print("minElement: ", minElement)
		#print("swi: ", w[swi])
		
		if abs(minElement - w[swi]) <= 4:
			#print("w[swi] - minElement: ", w[swi] - minElement)
		else:
			minElement = w[swi]
			#print("w[swi] - minElement: ", w[swi] - minElement)
			numberOfContainers += 1
		
		#if abs(minElement - w[swi]) >= 4:
		#	numberOfContainers += 1
		#else:
		#	minElement = w[swi]
	
	return numberOfContainers
	
	
	
if __name__ == "__main__":
	w = [1, 2, 3, 21, 7, 12, 14, 21]
	result = toys(w)
	print("No of Containers: ", result)