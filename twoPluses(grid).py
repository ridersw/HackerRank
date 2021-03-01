def twoPluses(grid):
	result = []
	
	for swi in range(1, len(grid) - 1):
		for swj in range(1, len(grid[swi])):
			count = 0
			tempTest = isPlus(grid, swi, swj, count)
			if tempTest != 0:
				result.append(1 + (4 * tempTest))
	
	finalAnswer = 1
	
	if len(result) > 1:	
		for i in range(0, 2):
			temp = max(result)
			finalAnswer *= temp
			result.remove(temp)
	
		return finalAnswer
	else:
		return result[0]
	

def isPlus(grid, swi, swj, count):

	if swi + 1 + count < len(grid) and swj + 1 + count < len(grid[swi]) and swi - 1 - count >= 0 and swj - 1 - count >= 0:
		if grid[swi + 1 + count][swj] == 'G' and grid[swi - 1 - count][swj] == 'G' and grid[swi][swj + 1 + count] == 'G' and grid[swi][swj - 1 - count] == 'G':
			count += 1
			return isPlus(grid, swi, swj, count)
		else:
			return count
			
	else:
		return count
	
	
	
if __name__ == "__main__":
	#grid = [['G', 'G', 'G', 'G', 'G', 'G'],['G', 'B', 'B', 'B', 'G', 'B'],['G', 'G', 'G', 'G', 'G', 'G'],['G', 'G', 'B', 'B', 'G', 'B'],['G', 'G', 'G', 'G', 'G', 'G']]
	
	#grid = [['B','G','G'],['G','G','G'],['G','G','G']]
	
	#grid = [['B','G','B','B','G','B'], ['G','G','G','G','G','G'], ['B','G','B','B','G','B'], ['G','G','G','G','G','G'], ['B','G','B','B','G','B'], ['B','G','B','B','G','B']]
	
	grid = [['G','G','G','G','G','G','G'], ['B','G','B','B','B','B','G'], ['B','G','B','B','B','B','G'], ['G','G','G','G','G','G','G'], ['G','G','G','G','G','G','G'], ['B','G','B','B','B','B','G']]
	
	result = twoPluses(grid)
	print("Result: ", result)