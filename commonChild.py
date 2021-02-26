from difflib import SequenceMatcher 

def commonChild(s1, s2):
	
	seqMatch = SequenceMatcher(None,s1,s2)

	match = seqMatch.find_longest_match(0, len(s1), 0, len(s2))
	
	if (match.size!=0): 
		return len(s1[match.a: match.a + match.size]) + 1
	else:
		return 0
	
if __name__=="__main__":
	s1 = "OUDFRMYMAW"
	s2 = "AWHYFCCMQX"
	result = commonChild(s1, s2)
	print("Result: ", result)