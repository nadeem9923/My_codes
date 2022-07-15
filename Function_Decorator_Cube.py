# Implement function decorator to display cube of a number

def decor(func):
	def inner():
		n = int(input(" Enter the number : "))
		return n * n * n
	return inner


@decor
def num():
	return inner

print(num())

