def gridSearch(G, P):
	
	pi = 0
	pj = 0
	
	pRow = len(P)
	
	for gi in range(len(G)+1):
		for gj in range(len(G[0])):
			#print("Comparing ",gi, gj ," with ",pi)
			if pRow > 0:
				if G[gi][gj] == P[pi]:
					pRow -= 1
					pi += 1
					
					if pRow == 0:
						return "Pattern Found"
				else:
					pRow = len(P)
					pi = 0
				
	return "Pattern Not Found"

if __name__ == '__main__':
	G = [[4, 0, 0, 4, 5, 3],
		 [1, 1, 4, 2, 1, 3],
		 [4, 7, 4, 3, 8, 6]]
		 
	P = [4, 2, 1, 3]
	result = gridSearch(G, P)
	print("Result: ", result)