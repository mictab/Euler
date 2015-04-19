public class SquareSum {
	public static void main(String[] args) {
		int sum_the_squares = 0, square_the_sum = 0;
		for (int i = 1; i <= 100 ; i++ ) {

			sum_the_squares+= i * i;
		}

		for (int i = 1; i <= 100 ; i++ ) {
			
			square_the_sum += i;
		}

		square_the_sum= square_the_sum * square_the_sum;
		System.out.println(square_the_sum - sum_the_squares);
	}
}
