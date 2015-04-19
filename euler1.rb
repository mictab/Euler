#And this is a solution in Ruby

sum = 0

for i in 0...1000
	if i % 5 == 0 || i % 3 == 0 then
		sum += i
		
	end
end

puts(sum)
