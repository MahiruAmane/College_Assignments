// Write a C Program To Print The Multiplication Table Of a Number Entered By The User.

#include <stdio.h>

int main()
{
    int n;
    int number;
    int value;

    printf("Please Enter a Number To Print It's Multiplication Table : ");
    scanf("%d", &number);
    
    printf("Please Enter The Number Of Rows You Want To Print For The Multiplication Table Of %d : ", number);
    scanf("%d", &n);

    for (int i = 0; i <= n; i++)
    {
        value = number * i;
        printf("%d x %d = %d\n", number, i, value);
    }

    return 0;
}