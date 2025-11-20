// Write a C Program To Apply Bitwise OR, AND & NOT Operators On Bit Level.

#include <stdio.h>

int main()
{
    int num1;
    int num2;
    int bitwise;

    printf("Please Enter The First Number : ");
    scanf("%d", &num1);

    printf("Please Enter The Second Number : ");
    scanf("%d", &num2);

    bitwise = num1 & num2;
    printf("Bitwise 'OR' Of %d And %d Is : %d\n", num1, num2, bitwise);

    bitwise = num1 | num2;
    printf("Bitwise 'AND' Of %d And %d Is : %d\n", num1, num2, bitwise);

    bitwise = ~num1;
    printf("Bitwise 'NOT' Of %d Is : %d\n", num1, bitwise);

    bitwise = ~num2;
    printf("Bitwise 'NOT' Of %d Is : %d", num2, bitwise);

    return 0;
}