def flatlandSpaceStations(n, c):

	finalArray = []	
	forwardArray = []
	backwardArray = []
	
	if n == len(c):
		return 0
	
	for swi in range(0,n):		
		if swi in c:
			forwardArray.append(0)
			backwardArray.append(0)
			
		else:
			tempF = findNextSpaceStation(swi, n, c)
			forwardArray.append(tempF)
			
			tempB = findPreviousSpaceStation(swi, 0, c)
			backwardArray.append(tempB)
			
			if (tempF != 0 and tempB != 0):
				finalArray.append(min(tempB,tempF))
			elif (tempF == 0 or tempB == 0):
				finalArray.append(max(tempB,tempF))
			else:
				finalArray.append(0)
				
			
	
	#print("forwardArray: ", forwardArray)
	#print("backwardAray: ", backwardArray)
	#print("finalArray: ", finalArray)
	
	return max(finalArray)
	
def findNextSpaceStation(currentLocation, completeForwardPath, c):
	count = 0
	
	for i in range(currentLocation, completeForwardPath):
		if i not in c:
			count += 1
		else:
			return count
			
	return 0
	
def findPreviousSpaceStation(currentLocation, completeBackwardPath, c):
	count = 0
	
	for i in range(currentLocation, completeBackwardPath,-1):
		if i not in c:
			count += 1
		else:
			return count
			
	return count

	
if __name__ == "__main__":
	n = 100
	c = [0]
	
	#n = 5
	#c = [0,4] 
	result = flatlandSpaceStations(n,c)
	print("Result: ", result)