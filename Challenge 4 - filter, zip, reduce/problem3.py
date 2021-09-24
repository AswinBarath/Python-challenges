def negToPos(item):
	return item<0


def convertToNeg(item):
	return int(-1 * item)


lst1 = [-1000, 500, -600, 700, 5000, -90000, -175000]

ans = list(map(convertToNeg, list(filter(negToPos, lst1))))

print(ans)
