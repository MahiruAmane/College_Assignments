// Write a C Program To Define Some Constant Variable In Pre Processor.

#include <stdio.h>
#define MULTIPLY 25

int main()
{
    int num1;
    int result;

    printf("Please Enter a Number : ");
    scanf("%d", &num1);

    result = num1 * MULTIPLY;

    printf("The Given Number Multiplied By 25 Is : %d", result);

    return 0;
}