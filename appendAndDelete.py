def appendAndDelete(s, t, k):

	if s == t:
		countOfMoves = ((2 * len(s)) + 1)
		if countOfMoves == k:
			return 'Yes'
		else:
			return 'No'

	countOfMoves = abs(len(s) - len(t))
	
	#print("CountOfMoves: ", countOfMoves)
	
	length = min(len(s), len(t))
	
	#print("length: ", length)
	
	for swi in range(length):
		if s[swi] != t[swi]:
			#print("swi: ", swi)
			countOfMoves += 2 * (length - swi)
			break
	
	if countOfMoves == k:
		return 'Yes'
	else:
		return 'No'
	
if __name__ == "__main__":
	#s: Initial String
	#t: Final String
	#k: No of Moves
	
	s = 'hackerhappy'
	t = 'hackerrank'
	k = 9
	
	result = appendAndDelete(s, t, k)
	print("Result: ", result)