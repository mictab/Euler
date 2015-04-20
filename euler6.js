//Eh, why not. Solving the problem using JS. See corresponding HTML and completely unnessecary CSS files.

function SumTheSquares () {
	var summa = 0;
	for (var i = 1; i <= 100; i++) {
		summa += i*i;
	}
	
	return summa;
}

function SquareTheSum () {
	var summa = 0;
	var squaresum;
	for (var i = 1; i <= 100; i++) {
		summa += i;
	}
	squaresum = Math.pow(summa, 2);
	return squaresum;
}

document.write(SquareTheSum()-SumTheSquares());
