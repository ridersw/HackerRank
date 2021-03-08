def minimumLoss(price):
	indices = {}
	for i in range(len(price)):
		indices[price[i]] = i
    
	print("Indices: ", indices)
	price = sorted(price, reverse=True)    
	print("price: ", price)
    
	ans = price[0] - price[-1]
	print("ans: ", ans)
	for i in range(len(price)-1):
		print("indices[price[i]]: ", indices[price[i]]," ", "< indices[price[i+1] ", indices[price[i+1]])
		if indices[price[i]] < indices[price[i+1]]:
			ans = min(ans, price[i] - price[i+1])
	return ans
	
if __name__ == "__main__":
	price = [20, 15, 8, 2, 12]
	#price = []
	result = minimumLoss(price)
	print("Minimum Loss: ", result)