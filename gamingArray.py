def gamingArray(arr):
	countOfMoves = 0
	
	print("length of Array: ", len(arr))
	
	maxValue = 0
	
	for item in arr:
		if item > maxValue:
			maxValue = item
			countOfMoves += 1
	
	if countOfMoves % 2 == 0:
		return "ANDY"
	else:
		return "BOB"
	
if __name__ == "__main__":
	#arr = [1, 3, 5, 7, 9]
	#result = gamingArray(arr)
	#print("Winner is: ", result)
	
	#arr = [2156, 90629, 23857 ,94325, 33447 ,78537, 48772 ,35902 ,47202, 79445, 63982, 4784, 68417, 3497, 90081, 36426, 86918, 30739, 95728, 31932, 7775, 14575]
	#result = gamingArray(arr)
	#print("Winner is: ", result)
	
	#arr = [65194,8115,6117,29036,32362,61968,33097,8933,48404,20798,22878,79156,12529,85569,6694,2312,95138,48680,83657,61801,67326,14165,92214,4546,84948,27986,88208,57285,60345,19284,2502,81434,95271,64223,38949,53020,26690,15360,95263,53404,36099,43951,58886,53245,42341,71994,74035,66042,78917,26868,23754,47366]
	#result = gamingArray(arr)
	#print("Winner is: ", result)
	
	arr = [5, 9, 8, 5, 6, 4, 2, 10]
	result = gamingArray(arr)
	print("Winner is: ", result)