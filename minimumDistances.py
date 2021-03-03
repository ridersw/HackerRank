def minimumDistances(a):
	minDist = []
	
	for swi in range(0, len(a)):
		for swj in range(swi, len(a)):
			if a[swi] == a[swj] and (swj - swi) != 0:
				minDist.append(swj - swi)
	
	
	#print("minDist: ", minDist)
	if len(minDis) > 0:
		return min(minDist)
	else:
		return -1
	
if __name__ == "__main__":
	a = [7, 1, 3, 4, 1, 7]
	result = minimumDistances(a)
	print("Result: ", result)