import math

def encryption(string):
	#rows = 0
	cols = 0
	
	string = string.replace(" ","")
	#("len: ", len(string))
	length = math.sqrt(len(string))
	
	if (length - int(length)) > 0:
		cols = math.ceil(length)
		#rows = math.floor(length)
	else:
		#rows = cols = length
		cols = int(length)
		
	print("cols: ", cols)
		
	newString = ""
	
	num = 0
	num1 = 0
	temp = ""
	
	while num < cols:
		num1 = int(num)
		print("num: ", num)
		print("num1: ", num1)
		while num1 < num1 + cols and num1 < len(string):
			print("string[num1]: ", string[num1])
			temp = string[num1]
			newString += temp
			num1 += cols
		
		newString += " "
		num += 1
	
	return newString

if __name__ == '__main__':
	#string = "feed the dog"
	string = "if facts dont fit to theory change the facts"
	result = encryption(string)
	print("Result: ",result)