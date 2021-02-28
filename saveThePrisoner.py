def saveThePrisoner(n, m, s):
	m = m % n
	
	return (m + s - 1)		
	
if __name__ == "__main__":
	#n = no of prisoners
	#m = no of sweets
	#s = distribution starts at
	
	n = 12 
	m = 430895283  
	s = 10
	
	result = saveThePrisoner(n, m, s)
	print("Result: ", result)