def fib(n):
	a, b = 0, 1
	while n > 0:
		a, b = b, a + b
		n -= 1
	return a

n = 0
summa = 0

while fib(n) < 4000000 :
	if fib(n) % 2 == 0:
		summa += fib(n)
	n+=1
print(summa)
