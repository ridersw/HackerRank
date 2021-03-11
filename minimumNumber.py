def minimumNumber(n, strongPassword):
	
	count = 4
	
	haveNumbers = "False"
	haveLowerCase = "False"
	haveUpperCase = "False"
	haveSpecialCharacters = "False"
	
	numbers = "0123456789"
	lower_case = "abcdefghijklmnopqrstuvwxyz"
	upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
	special_characters = "!@#$%^&*()-+"
	
	for letter in strongPassword:
		if letter in numbers and haveNumbers == "False":
			#print("COunt: ", count)
			haveNumbers = "True"
			count -= 1
		elif letter in lower_case and haveLowerCase == "False":
			haveLowerCase = "True"
			count -= 1
		elif letter in upper_case and haveUpperCase == "False":
			haveUpperCase = "True"
			count -= 1
		elif letter in special_characters and haveSpecialCharacters == "False":
			haveSpecialCharacters = "True"
			count -= 1
	
	if count > 0 and count + len(strongPassword) >= 6:
		print("Count: ",count)
		print("return 31")
		return count
	elif count == 0 and len(strongPassword) >= 6:
		return 0
	else:
		print("return 34")
		return 6-len(strongPassword)
		
if __name__ == "__main__":
	n = 6
	strongPassword = "#cP!F9Z"
	
	result = minimumNumber(n, strongPassword)
	print("Result: ", result)