def climbingLeaderboard(ranked, player):
	temp = 0
	tempArray = []
	
	for item in player:
		ranked.append(item)
		ranked.sort(reverse=True)
		ranked = list(dict.fromkeys(ranked))
		
		tempArray.append(ranked.index(item) + 1)
		#print("Rank: ",temp + 1)
	
	return tempArray


ranked = [100, 90, 90, 80, 75, 60]
player = [50, 65, 77, 90, 102]
tempArray = climbingLeaderboard(ranked, player)
print("Ranking: ", tempArray)