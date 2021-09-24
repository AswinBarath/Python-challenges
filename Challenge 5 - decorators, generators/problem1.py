# Decorator function

def do_twice(func):
    def wrapper_do_twice(*args, **kwargs):
        func(*args, **kwargs)
        func(*args, **kwargs)
    return wrapper_do_twice

# Function which uses Decorator

@do_twice
def multiply(num1, num2):
	print(num1*num2)

multiply(10, 20)
