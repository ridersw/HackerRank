def makingAnagrams(s1, s2):
	for i in s1:
		if i in s2:
			s1=s1.replace(i,"",1)
			print("s1: ", s1)
			s2=s2.replace(i,"",1)
			print("s2: ", s2)
	return(len(s1)+len(s2))
	
	
if __name__ == "__main__":
	s1 = 'absdjkvuahdakejfnfauhdsaavasdlkj'
	s2 = 'djfladfhiawasdkjvalskufhafablsdkashlahdfa'
	
	result = makingAnagrams(s1, s2)
	print("Result: ", result)