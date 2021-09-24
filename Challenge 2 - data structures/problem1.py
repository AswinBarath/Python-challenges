from collections import Counter
def check_duplicates(a_list):
	for li in a_list:
		count = Counter(li)
		for val in count.items():
			if val[1] > 1:
				print(val[0], "->", val[1])



arr_list = [[1,1,3,2], [9,8,8,1], [0,4,5,0,0,1,4]]
check_duplicates(arr_list)