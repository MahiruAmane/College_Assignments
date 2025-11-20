// Write a C Program to Check If a Number Is Divisible By 3 and 5.

#include <stdio.h>

int main()
{
    int number;

    printf("Please Enter a Number To Check Divisibility By 3 and 5 : ");
    scanf("%d", &number);

    if (number % 3 == 0 && number % 5 == 0)
    {
        printf("The Number %d Is Divisible By 3 and 5", number);
    }
    else
    {
        printf("The Number %d Is Not Divisible By 3 and 5", number);
    }

    return 0;
}