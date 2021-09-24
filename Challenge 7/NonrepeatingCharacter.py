def NonrepeatingCharacter(strParam)	:
	# code goes here
	freq = {}
	for c in strParam:
		try:
			if freq[c] == 1:
				freq[c] +=1
		except:
			freq[c] = 1

	ans = ""
	for i in strParam:
		if freq[i] == 1:
			ans = i
			break
		
	return ans
	
# keep this function call here
print(NonrepeatingCharacter(input()))