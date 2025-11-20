// Write a C Program To Declare a Float Without Initializing and Later Assign a Value.

#include <stdio.h>

int main()
{
    float number;

    printf("Please Enter a Number You Want To Print : ");
    scanf("%f", &number);

    printf("The Floating Number You Entered Is : %.2f", number);

    return 0;
}