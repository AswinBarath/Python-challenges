class StringClass:
	def __init__(self, string):
		self.string = string
	
	def stringLength(self):
		return len(self.string)
	
	def convertString(self, string):
		return list(string)


str1 = StringClass("Apple")
print(str1.stringLength()) # O/P: 5
print(str1.convertString("Apple")) # O/P: ['A', 'p', 'p', 'l', 'e']