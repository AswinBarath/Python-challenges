def convertDict(d):
	res = []
	for key in d:
		li = []
		li.append(key)
		for val in d[key]:
			li.append(val)
		res.append(li)
	return res

orginalDict = {'HuEx': [1,3,4], 'is': [7,6], 'best':[4,5]}

newList = convertDict(orginalDict)
print(newList)