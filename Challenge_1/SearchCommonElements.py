class StringClass:
	def __init__(self, string):
		self.string = string
	
	def getStr1(self):
		return self.string

	def stringLength(self):
		return len(self.string)
	
	def convertString(self, string):
		return list(string)


class PairPossible(StringClass):
	def __init__(self, string):
		# StringClass.__init__(self)
		self.string = string
		self.pairs = []
	
	def getStr2(self):
		return self.string

	def generatePairs(self):
		for s in list(self.string):
			for ss in list(self.string):
				self.pairs.append(s + ss)
	
	def printPairs(self):
		for s in self.pairs:
			print(s, sep=" ", end=" ")

s1 = StringClass("Refreshment")
s2 = PairPossible("fresh")

class SearchCommonElements:
	def __init__(self, str1, str2):
		self.str1 = str1
		self.str2 = str2
		self.common = {}
		self.commonList = []
	
	def commonElements(self):
		for ele1 in self.str1:
			self.common[ele1] = 1

		for ele2 in self.str2:
			if ele2 in self.common:
				self.common[ele2] += 1

		for ele in self.common.keys():
			if self.common[ele] > 1 :
				self.commonList.append(ele)

		return self.commonList

ans = SearchCommonElements(s1.getStr1(), s2.getStr2())
print(ans.commonElements())