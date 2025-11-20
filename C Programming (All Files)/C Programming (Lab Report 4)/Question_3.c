// Write a C Program To Define Multiple Macro's To Perform Arithmetic Operations.

#include <stdio.h>
#define ADD(x, y) ((x) + (y))
#define SUBTRACT(x, y) ((x) - (y))
#define MULTIPLY(x, y) ((x) * (y))
#define DIVIDE(x, y) ((float)(x) / (y))

int main()
{
    int num1;
    int num2;
    float result;

    printf("Please Enter The First Number : ");
    scanf("%d", &num1);

    printf("Please Enter The Second Number : ");
    scanf("%d", &num2);

    result = ADD(num1, num2);
    printf("The Addition Of The Given Numbers %d & %d Is : %.2f\n", num1, num2, result);

    result = SUBTRACT(num1, num2);
    printf("The Subtraction Of The Given Numbers %d & %d Is : %.2f\n", num1, num2, result);

    result = MULTIPLY(num1, num2);
    printf("The Multiplication Of The Given Numbers %d & %d Is : %.2f\n", num1, num2, result);

    if (num2 == 0)
    {
        printf("Divison By Zero Is Not Defined");
    }
    else
    {
        result = DIVIDE(num1, num2);
        printf("The Division Of The Given Number %d & %d Is : %.2f", num1, num2, result);
    }

    return 0;
}