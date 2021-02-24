def flatlandSpaceStations(n, c):
	print("c: ", c)
	c = sorted(c)
	print("c: ", c)
	res = c[0]
	print("res: ", res)
	for ind in range(1, len(c)):
		res = max(res, (c[ind] - c[ind-1])//2)
        
	res = max(res, n-1 - c[-1])
        
	return res

	
if __name__ == "__main__":
	n = 20
	c = [1,6,10,11,13]
	result = flatlandSpaceStations(n,c)
	print("Result: ", result)