#Quite short and simple solution imo. Using Ruby (awesome language).

require 'prime'

sum = 0

Prime.each(2000000)  do | prime |
	sum += prime
	
end

puts(sum)

#Takes about 3 sec. Could be optimized but I like the simplicity for now.
