from functools import reduce

def multiplier(acc, item):
	return acc*item

my_list = [1,2,3,4,5]
ans = reduce(multiplier, my_list, 1)

print(ans)