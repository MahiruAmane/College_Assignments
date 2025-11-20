// Write a C Program To Use a Recursive Function GCD (num1, num2) That Accepts Two Integer Arguments. Use This Function to Find the Greatest Common Divisor Of Two Given Integers. 

#include <stdio.h>

int greatest_Common_Divisor(int a, int b)
{
    if (b == 0)
    {
        return a;
    }
    else
    {
        return greatest_Common_Divisor(b, a % b);
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

    printf("The Greatest Common Divisor Of %d & %d Is : %d", num1, num2, greatest_Common_Divisor(num1, num2));

    return 0;
}