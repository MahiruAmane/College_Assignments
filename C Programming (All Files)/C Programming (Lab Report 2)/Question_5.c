// Write a C Program To Create a Recursive And Non Recursive Function To Find The Factorial Of a Number. Using This Function, Compute The Binomial Coefficient. Tabulate The Results For Different Values Of n And r With Suitable Messages. 

#include <stdio.h>

int factorial_Recursive(int y)
{
    if (y <= 1)
    {
        return 1;
    }
    else
    {
        return y * factorial_Recursive(y - 1);
    }
}

int factorial_Non_Recursive(int x)
{
    int sum = 1;

    for (int i = 1; i <= x; i++)
    {
        sum = sum * i;
    }

    return sum;
}

int main()
{
    int n;
    int r;

    printf("Please Enter a Number To Find It's Factorial : ");
    scanf("%d", &n);

    printf("The Factorial Using The Non Recursive Function Is : %d\n", factorial_Non_Recursive(n));
    printf("The Factorial Using The Recursive Function Is : %d\n", factorial_Recursive(n));

    printf("Please Enter a Number To Find The Binomial Coefficient : ");
    scanf("%d", &r);

    if (r > n || r < 0)
    {
        printf("Invalid Input Please Try a Different Value");
        return 1;
    }

    printf("\n");

    for (int i = 1; i <= n; i++)
    {
        for (int j = 0; j <= r; j++)
        {
            if (j > i || j < 0)
            {
                break;
            }

            int binomial_non_recursive = factorial_Non_Recursive(i) / (factorial_Non_Recursive(j) * factorial_Non_Recursive(i - j));
            int binomial_recursive = factorial_Recursive(i) / (factorial_Recursive(j) * factorial_Recursive(i - j));

            printf("The Binomial Coefficient (%d,%d) Using Non Recursive Function Is : %d\n", i, j, binomial_non_recursive);
            printf("The Binomial Coefficient (%d,%d) Using Recursive Function Is : %d\n", i, j, binomial_recursive);

            printf("\n");
        }

        printf("\n");
    }

    return 0;
}