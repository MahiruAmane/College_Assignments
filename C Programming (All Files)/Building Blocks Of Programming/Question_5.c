// Write a C Program To Use If Else Conditions to Find The Largest Of Three Numbers.

#include <stdio.h>

int main()
{
    int num1;
    int num2;
    int num3;

    printf("Please Enter The First Number : ");
    scanf("%d", &num1);

    printf("Please Enter The Second Number : ");
    scanf("%d", &num2);

    printf("Please Enter The Third Number : ");
    scanf("%d", &num3);

    if (num1 == num2 && num2 == num3)
    {
        printf("All The Numbers You Entered Are Same");
    }
    else if (num1 > num2 && num1 > num3)
    {
        printf("The Largest Number Is : %d", num1);
    }
    else if (num2 > num1 && num2 > num3)
    {
        printf("The Largest Number Is : %d", num2);
    }
    else
    {
        printf("The Largest Number Is : %d", num3);
    }

    return 0;
}