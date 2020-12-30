import math

def viralAdvertising(n):
	sum = 5
	peopleLiked = 0
	for i in range(n):
		print("Before Sharing- People Count: ", sum)
		sum = math.floor(sum/2)
		print("Liked Advertisement People Count: ", sum)
		peopleLiked += sum
		sum *= 3
		print("Total People: ", sum)
		
	return peopleLiked


if __name__ == '__main__':
	n = 3
	result = viralAdvertising(n)
	print("Result: ",result)