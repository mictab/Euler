fil = open('lang.txt')
filr = fil.readlines()
glosor = []
for number in filr:
	glosor.append(int(number.strip('\n')))

summa = sum(glosor)
print(summa)
summa = str(summa)
print(summa[:10])
