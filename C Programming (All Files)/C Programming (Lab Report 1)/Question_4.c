// Write a C Program That Prompts The User To Add Two Numbers.

#include <stdio.h>

int main()
{
    int num1;
    int num2;
    int sum;

    printf("Please Enter The First Number : ");
    scanf("%d", &num1);

    printf("Please Enter The First Number : ");
    scanf("%d", &num2);

    sum = num1 + num2;

    printf("The Sum Of %d And %d Is : %d", num1, num2, sum);

    return 0;
}