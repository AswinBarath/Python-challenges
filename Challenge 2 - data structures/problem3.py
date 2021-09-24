list1 = ["a", "b", ["c", ["d", "e", ["f", "g"], "k"], "l"], "m", "n"]

subList = ["h", "i", "j"]
for val in subList:
	list1[2][1][2].append(val)
print(list1)