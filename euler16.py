number = 2**1000

number = str(number)			#make it a string to put in list
alist = []
the_sum = 0

for item in number:
	alist.append(item)

for item in alist:
	the_sum += int(item)

print("The sum is: ", the_sum)
