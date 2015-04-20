def factorial(n):             #start by defining a recursive factorial function
	if n == 1: return 1
	if n == 0: return 1
	return n * factorial(n-1)

number = factorial(100)
number = str(number)          #convert our number to a string

summa = 0

for item in number:           #iterate through the string
	summa += int(item)

print(summa)                  #and the sum returned is '648'
