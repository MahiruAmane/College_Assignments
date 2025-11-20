// Write a C Program To Use Do While Loop To Read Numbers Until User Enters 0.

#include <stdio.h>

int main()
{
    int number;

    do
    {
        printf("Please Enter Zero To Exit The Loop : ");
        scanf("%d", &number);

        if (number != 0)
        {
            printf("The Number You Entered Is : %d\n", number);
        }

    } while(number != 0);

    printf("Program Terminated");

    return 0;
}