// Write a C Program To Use a Recursive Function FIBO (num1) That Accepts An Integer Argument. Use This Function To Generate The Fibonacci Sequence.

#include <stdio.h>

int fibonacci_Series(int n)
{
    if (n == 0)
    {
        return 0;
    }
    else if (n == 1)
    {
        return 1;
    }
    else
    {
        return fibonacci_Series(n - 1) + fibonacci_Series(n - 2);
    }
}

int main()
{
    int num1;

    printf("Please Enter The Number Of Terms You Want To See : ");
    scanf("%d", &num1);

    printf("The Fibonacci Series Upto %d Terms Are : ", num1);

    for (int i = 0; i < num1; i++)
    {
        printf("%d ", fibonacci_Series(i));
    }

    return 0;
}