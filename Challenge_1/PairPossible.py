class StringClass:
	def __init__(self, string):
		self.string = string
	
	def stringLength(self):
		return len(self.string)
	
	def convertString(self, string):
		return list(string)


class PairPossible(StringClass):
	def __init__(self, string):
		StringClass.__init__(self, string)
		self.string = string
		self.pairs = []
	
	def generatePairs(self):
		for s in list(self.string):
			for ss in list(self.string):
				self.pairs.append(s + ss)
	
	def printPairs(self):
		for s in self.pairs:
			print(s, sep=" ", end=" ")

str2 = PairPossible("Apple")
str2.generatePairs()
str2.printPairs()