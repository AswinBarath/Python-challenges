class FormulaError(Exception):
	"""Exception raised for errors in the input formula.
    """
	def __init__(self):
		super().__init__(self.message)


try:
	input = input().split(' ')
	if len(input) != 3:
		raise FormulaError("Please eneter the correct formula in this format: 1 + 1 or 1 - 1")
	else:
		num1, operator, num2 = input
		num1 = float(num1)
		num2 = float(num2)
		if operator == '+':
			print(num1+num2)
		elif operator == '-':
			print(num1-num2)
		else:
			raise FormulaError("Please eneter the correct formula in this format: 1 + 1 or 1 - 1")
except FormulaError:
	print("Please enter the correct formula")
except ValueError:
	print("Please enter the correct values")
