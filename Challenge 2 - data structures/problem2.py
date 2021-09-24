def Merge(l1, l2):
	res = []
	for val1 in l1:
		for val2 in l2:
			res.append(val1 + " "+ val2)
	return res

list1 = ["Hello", "take"]
list2 = ["Dear", "Sir"]

res = Merge(list1, list2)
print(res)