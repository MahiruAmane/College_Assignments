// Write a C Program To Create a Static Library For Performing Arithmetic Functions.

#include <stdio.h>
#include "operation.h"

int main()
{
    int num1;
    int num2;

    printf("Please Enter The First Number : ");
    scanf("%d", &num1);

    printf("Please Enter The Second Number : ");
    scanf("%d", &num2);

    printf("The Addition Of The Given Numbers %d & %d Is : %d\n", num1, num2, add(num1, num2));
    printf("The Subtraction Of The Given Numbers %d & %d Is : %d\n", num1, num2, subtract(num1, num2));
    printf("The Multiplication Of The Given Numbers %d & %d Is : %d\n", num1, num2, multiply(num1, num2));
    
    if (num2 == 0)
    {
        printf("Division By Zero Is Not Defined");
    }
    else
    {
        printf("The Division Of The Given Numbers %d & %d Is : %.2f", num1, num2, divide(num1, num2));
    }

    return 0;
}