-- Solving problem 1 using Haskell

summan = sum [x | x <-[1..999], x `mod` 5 == 0 || x `mod` 3 == 0]

--then just call "summan" and it gives you 233168
