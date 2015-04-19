for a in range(1,1000):
	for b in range(a,1000):
		c = 1000 - a - b                                #using the fact that a + b + c = 1000
		if a**2 + b**2 == c**2 and a + b + c == 1000:
			print(a,b,c)                                  #prints the numbers
			print(a*b*c)                                  #and their product
