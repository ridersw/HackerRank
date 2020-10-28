import statistics

def fraudCounts(expenditure, d):
	length = len(expenditure)
	
	count = 0
	
	for i in range(length-d):
		temp = []
		#print("Loop: ", i)
		for j in range(i,i+d):
			temp.append(expenditure[j])
			
		ans = statistics.median(temp)
		
		if (ans*2) <= expenditure[i+d]:
			count += 1
	
	return count
	
expenditure = [2, 3, 4, 2, 3, 6, 8, 4, 5]
d = 5

result = fraudCounts(expenditure, d)
print("Result: ", result)