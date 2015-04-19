/*
*Another solution for problem 1 but using Java
* :-)
*/

public class FindSum {
	public static void main(String[] args) {
		int sum = 0;

		for (int i = 0; i < 1000 ; i++ ) {
			if (i % 5 == 0 || i % 3 == 0) {
				sum += i;
			}
		}

		System.out.println(sum); //this prints 233168
	}

}
