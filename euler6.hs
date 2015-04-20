-- my first Haskell program. For Euler problem 6.

squares = [x * x | x<-[1..100]]
sumsquares = sum squares
hundred_integers = [x | x<-[1..100]]
summan = sum hundred_integers
squaresum = summan * summan

difference = squaresum - sumsquares

--outputs 25164150 when calling "difference"
