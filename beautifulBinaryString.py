class binaryString:
	def __init__(self, b):
		self.b = b
		countOfOperations = 0
		
	def beautifulBinaryString(self):
		
		countOfOperations = 0	
		toIgnore = []
		for swi in range(0, len(self.b) - 2):
			if self.b[swi] == '0':
				if self.b[swi+1] == '1' and self.b[swi+2] == '0' and swi not in toIgnore:
					countOfOperations += 1
					toIgnore.append(swi+2)
					#print("toIgnore: ", toIgnore)
			
		return countOfOperations
		
if __name__ == "__main__":
	b = "0101010"
	binary = binaryString(b)
	result = binary.beautifulBinaryString()
	print("Result: ", result)
	