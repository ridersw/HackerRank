def checkPalindrome(string):
	count = len(string)-1
	
	for i in range(len(string)):
		
		if i <= count:
			print("Comparing ", string[i], " with ", string[count])
			if string[count] != string[i]:
				#print("string[count]: ", string[count])
				#print("string[count-1]: ", string[count-1])
				
				if string[count] != string[i+1]:
					#print("Returning Count")
					return count
				else:
					#print("Returning i")
					return i
			else:
				count -= 1
	
	return -1
	
	
string = "hgygsvlfcwnswtuhmyaljkqlqjjqlqkjlaymhutwsnwcwflvsgygh"

result = checkPalindrome(string)
print("Result: ",result)