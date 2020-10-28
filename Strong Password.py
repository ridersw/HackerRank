def isStrongPassword(strongPassword):

	numbers = "0123456789"
	lower_case = "abcdefghijklmnopqrstuvwxyz"
	upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
	special_characters = "!@#$%^&*()-+"

	

	isSpecial = False
	isNumber = False
	isLowerCase = False
	isUpperCase = False
	
	count = 4

	for i in range(len(strongPassword)):
		if isNumber == False:
			if strongPassword[i] in numbers:
				isNumber = True
				count -= 1
				
		if isLowerCase == False:
			if strongPassword[i] in lower_case:
				isLowerCase = True
				count -= 1		
		if isUpperCase == False:
			if strongPassword[i] in upper_case:
				isUpperCase = True
				count -= 1
		
		if isSpecial == False:		
			if strongPassword[i] in special_characters:
				isSpecial = True
				count -= 1
		
	if len(strongPassword) < 6 and count == 0:
		return (6-len(strongPassword))
		
	return count
	

strongPassword = "Ab1"
Result = isStrongPassword(strongPassword)
print("Result: ", Result)	