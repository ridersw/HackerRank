def cavityMap(grid):
	
	if len(grid) < 3:
		return grid
		
	toMutate = []
		
	print("In Function")
	
	for i in range(1,len(grid)-1):
		for j in range(1, len(grid)-1):
			if (grid[i-1][j] < grid[i][j] and grid[i][j-1] < grid[i][j] and grid[i+1][j] < grid[i][j] and grid[i][j+1] < grid[i][j]):
				toMutate.append(i)
				toMutate.append(j)
				
				#grid[i][j] = 'X'
				#print(grid[i][j] + "YES")
			#else:
				#print(grid[i][j] + "NO")
	
	print("toMutate: ", toMutate)
	#print("toMutate: ", toMutate)
	
	for i in range(0,len(toMutate),2):
		print("change")
		tempNumR = toMutate[i]
		tempNumC = toMutate[i+1]
		tempList = list(grid[tempNumR])
		tempList[tempNumC] = 'X'
		grid[tempNumR] = ''.join(tempList)
	
	return grid
	

if __name__=="__main__":
	print("In main")
	grid = ['1112', '1912', '1892', '1234']
	result = cavityMap(grid)
	print("result: ", result)
	
