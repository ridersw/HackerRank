def designerPdfViewer(h, word):
	max = 0
	
	array = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
	#length = len(word)
	for swi in range(0, len(word)):
		tempIndex = array.index(word[swi])
		if h[tempIndex] > max:
			max = h[tempIndex]
			
	return (max * len(word))
	
if __name__ == "__main__":
	h = [1, 3, 1, 3, 1, 4, 1, 3, 2, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 7]
	word = 'zaba'
	result = designerPdfViewer(h, word)
	print("Result: ", result)