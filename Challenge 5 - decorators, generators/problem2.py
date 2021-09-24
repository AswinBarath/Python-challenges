# Generator for Fibonacci Numbers
def fib(limit):
	a, b = 0, 1
	while a < limit:
		yield a
		a, b = b, a + b

# Generator object
x = fib(6)

# Iterating using next
print(x.__next__())
print(x.__next__())
print(x.__next__())
print(x.__next__())
print(x.__next__())
print(x.__next__())

# Iterating using for loop
print("\n Using for in loop")
for i in fib(6):
	print(i)
