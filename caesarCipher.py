def caesarCipher(s, k):
	cipherString = []
	
	k = k % 26
	
	alphabets = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
	ALPHABETS = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
	
	s = list(s)
	
	for swi in range(0, len(s)):
		if s[swi] in alphabets:
			temp = alphabets.index(s[swi])
			if temp + k < len(alphabets):
				cipherString.append(alphabets[temp+k])
			else:
				tempIndex = temp + k - len(alphabets)
				cipherString.append(alphabets[tempIndex])
			
		elif s[swi] in ALPHABETS:
			if s[swi] in ALPHABETS:
				temp = ALPHABETS.index(s[swi])
				if temp + k < len(ALPHABETS):
					cipherString.append(ALPHABETS[temp+k])
				else:
					tempIndex = temp + k - len(ALPHABETS)
					cipherString.append(ALPHABETS[tempIndex])
		else:
			cipherString.append(s[swi])
	
	return "".join(cipherString)
	
	
if __name__ == "__main__":
	s = "www.abc.xy"
	k = 87
	
	
	result = caesarCipher(s,k)
	print("Result: ", result)