def fib(n):                 # defining a fibonacci generator
	a, b = 0, 1
	while n > 0:
		a, b = b, a + b
		n -= 1
	return a

n = 0
foundAnswer = False

while not foundAnswer:
	x = fib(n)
	if len(str(x)) == 1000:
		print("The index you're looking for is: ", n)           # n = 4782
		foundAnswer = True
	n+=1
