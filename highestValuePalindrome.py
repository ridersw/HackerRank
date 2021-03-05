import math

def highestValuePalindrome(s, n, k):
	
	if len(s) <= 1:
		return '9'
		
	else:
		s = list(s)
		
		swi = 0
		swj = len(s)-1
		
		while swi < swj and k > 0:
			if s[swi] != s[swj]:
				if k > 1:
					s[swi] = '9'
					s[swj] = '9'
					k -= 2
				else:
					temp = str(max(int(s[swi]), int(s[swj])))
					s[swi] = temp
					s[swj] = temp
					k -= 1
					
			swi += 1
			swj -= 1
	
		while swi < swj and k >= 2:
			if int(s[swi]) < 9 and int(s[swj]) < 9:
				s[swi] = '9'
				s[swj] = '9'
				k -= 2
		
		if (len(s) % 2 != 0):
			leng = math.ceil(len(s) / 2)
			
			s[leng-1] = '9'	
			
		s = "".join(s)
		s = str(s)
		
		newS = s[::-1]
		
		#print("s: ", s)
		
		
		
		if s == newS:
			return s
		else:
			return '-1'
		
	return s
	
if __name__ == "__main__":
	s = '12321'
	n = 5 #no of digits
	k = 1 #no of changes allowed
	result = highestValuePalindrome(s, n, k)
	print("Cost: ", result)