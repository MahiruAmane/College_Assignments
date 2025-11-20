// Write a C Program To Use a Function That Returns The Larger Of Two Numbers (Arguments, Return Value).

#include <stdio.h>

int LargerNumber(int a, int b)
{
    if (a > b)
    {
        return 1;
    }
    else
    {
        return 0;
    }
}

int main()
{
    int num1;
    int num2;

    printf("Please Enter The First Number : ");
    scanf("%d", &num1);

    printf("Please Enter The Second Number : ");
    scanf("%d", &num2);

    if (LargerNumber(num1, num2))
    {
        printf("The Larger Number Is : %d", num1);
    }
    else
    {
        printf("The Larger Number Is : %d", num2);
    }

    return 0;
}