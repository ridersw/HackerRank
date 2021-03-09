def lonelyinteger(a):
	
	dict = {}
	
	for item in a:
		if item not in dict:
			dict[item] = 1
		else:
			dict[item] += 1
			
	print("dict: ", dict)
			
	for key, value in dict.items():
		print("value: ", value)
		if value == 1:
			return key
	
	return -1
	
if __name__ == "__main__":
	a = [4, 9, 95, 93, 57, 4 ,57 ,93 ,9]
	result = lonelyinteger(a)
	print("Lonely Integer: ", result)