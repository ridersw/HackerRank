def birthday(arrayChocolate, day, month):
	
	tempCount = 0
	
	share = 0
	if len(arrayChocolate) > 1:
		for i in range(len(arrayChocolate)-month+1):
			for j in range(i,i+month):
				tempCount += arrayChocolate[j]
				
			if tempCount == day:
				share += 1
				
			tempCount = 0
			
		return share
	else:
		if month == 1:
			if arrayChocolate[0] == day:
				return 1
			else:
				return 0
		
if __name__ == "__main__":
	arrayChocolate = [2, 5, 1, 3, 4, 4, 3, 5, 1, 1, 2, 1, 4, 1, 3, 3, 4, 2, 1]  #s
	day = 18				#d
	month = 7			#m
	result = birthday(arrayChocolate, day, month)
	print("Result: ", result)