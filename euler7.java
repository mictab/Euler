public class FindPrime {
	public static void main(String[] args) {
		int count = 0;
		for (int i = 1; count < 10001; i++ ) {
			if (isPrime(i)) {
				count ++;
				System.out.println("Prime#: " + count + " is " + i);
			}
			
		}
	}


	public static boolean isPrime(int num) {
		if (num % 2 == 0) {
			return false;
		}
		for (int i = 3; i <= Math.sqrt(num); i++) {
			if (num % i == 0) {
				return false;
			}
		}
		return true;
	}
}

/*
*Console output gives a list of primes including "Prime#: 10001 is 104743"
*/
