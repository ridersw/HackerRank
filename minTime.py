def minTime(files, numCores, limit):
	timeRequired = 0
	
	files.sort()
	
	files = files[::-1]
	
	for swi in range(len(files)):
		if files[swi] % numCores == 0 and limit > 0:
			timeRequired += files[swi] / numCores
			limit -= 1
		else:
			timeRequired += files[swi]
			
	return int(timeRequired)
	
if __name__ == "__main__":
	files = [5,3,1]
	numCores = 1
	limit = 5
	
	result = minTime(files, numCores, limit)
	print("result: ", result)