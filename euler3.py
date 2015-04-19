def sall(n):                #this function generates primes
	primes = []
	multipler = set()
	for i in range(2, n + 1):
		if i not in multipler:
			primes.append(i)
			multipler.update(range(i*i, n+1, i))
	return primes

def findFactors(number):                    #this function finds prime factors and returns the maximum
	lista = sall(int(number ** 0.5))
	maximum = 0
	for i in lista:
		if number % i == 0 and i > maximum:
			maximum = i
	return maximum

print(findFactors(600851475143))
