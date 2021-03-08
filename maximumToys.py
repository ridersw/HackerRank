def maximumToys(prices, k):
	priceOfToys = 0
	
	prices.sort()
	
	for swi in range(0, len(prices)):
		if priceOfToys + prices[swi] <= k:
			priceOfToys += prices[swi]
		else:
			return swi
	
	return swi
	
	#return countOfToys
	
	
if __name__ == "__main__":
	prices = [1, 12, 5, 111, 200, 1000, 10]
	k = 50
	result = maximumToys(prices, k)
	print("Maximum Toys: ", result)