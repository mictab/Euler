--Simple (but rather slow, takes almost 30 sec) Haskell code that solves problem 9

pythagoranTriplet = [(a, b, c) | c<-[1..1000], b<-[1..c], a<-[1..b], a^2 + b^2 == c^2, a+b+c == 1000]

--this returns a tuple (200, 375, 425) and then you just multiply them
