#Using nested for-loops, comparing strings


biggest = 0
for x in range(100,1000):
	for i in range(100,1000):
		z = x * i
		y = str(x * i)
		if y == y[::-1] and z > biggest:
			biggest = z
print(biggest)
