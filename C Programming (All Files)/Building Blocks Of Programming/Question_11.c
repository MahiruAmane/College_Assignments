// Write a C Program To Use a Function that Prints Factorial Of a Number (Arguments, Don't Return Value).

#include <stdio.h>

int Factorial(int x)
{
    int fact = 1;
    
    for (int i = 1; i <= x; i++)
    {
        fact = fact * i;
    }

    printf("The Factorial Of %d Is : %d", x, fact);
}

int main()
{
    int n;

    printf("Please Enter a Number To Know It's Factorial : ");
    scanf("%d", &n);

    Factorial(n);

    return 0;
}