def timeInWords(h, m):
	str = ""
	
	minutes = ['one','two','three','four','five','six','seven','eight','nine','ten','eleven','twelve','thirteen','fourteen','quarter','sixteen','seventeen','eighteen','nineteen','twenty','twenty one','twenty two','twenty three','twenty four','twenty five','twenty six','twenty seven','twenty eight','twenty nine','half']
	
	min = 'minutes'
	
	if m < 30 and m < 10 and m > 0:
		str = minutes[m-1] + ' minute past ' + minutes[h-1]
		return str
		
	elif m < 30 and m > 0 and m != 15:
		print("m: ", m)
		str = minutes[m-1] + ' minutes past ' + minutes[h-1]
		return str
		
	elif m < 30 and m > 0 and m == 15:
		str = minutes[m-1] + ' past ' + minutes[h-1]
		return str
		
	elif m == 30:
		str = minutes[m-1] + ' past ' + minutes[h-1]
		return str
		
	elif m == 00:
		str = minutes[h-1] + " o' " + 'clock'
		return str
		
	elif m > 30 and (30-m) != -15:
		str = minutes[30-m-1] + ' minutes to ' + minutes[h]
		return str
	
	elif m > 30 and (30-m) == -15:
		str = minutes[30-m-1] + ' to ' + minutes[h]
		return str


if __name__=='__main__':
	h = 7
	m = 15
	Result = timeInWords(h, m)
	print("Result: ", Result)
