def decentNumber(n):
	if n % 3 == 0:
		return (str(5) * n)
	elif n % 5 == 0:
		return (str(3) * n)
	else:
		if (n - 5) % 3 == 0:
			return (str(5)*(n-5) + str(3) * 5)
		elif(n - 3) % 5 == 0:
			return (str(5)*(n-3) + str(3) * 3)
		else:
			return -1
	

n = 13	
result = decentNumber(n)
print("Result: ", result)