def doesStringMatch(s1,s2):
	for sw in range(len(s1)):	
		if s1[sw] in s2:
			return "YES"
			
			
	return "NO"
	
	
s1 = "Hello"
s2 = "DragnBrn"
result = doesStringMatch(s1,s2)
print("Result: ", result)