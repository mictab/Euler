summa = 0
for x in range(1,1001):
	summa += x**x
summa = str(summa)
print(summa[-10:])		#gives the last ten digits and prints 9110846700
