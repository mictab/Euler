#include <stdio.h>
//and now a solution using C

int main(){
    int sum = 0;                        //sums the first 100 integers
    int sumofsquares = 0;
    for (int x = 1; x <= 100; x++){
        sum += x;
    }

    for (int i = 1; i <= 100 ; i++)
    {
        sumofsquares += i * i;
    }

    int squaresum = sum * sum;      //squares that sum

    printf("The answer is: %d\n", squaresum - sumofsquares);
}
