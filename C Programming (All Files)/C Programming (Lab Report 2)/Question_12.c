// Write a C Program To Declare Different Types Of Pointers (int, float, char) And Initialize Them With The Addresses Of Variables. Print The Values Of Both The Pointers And The Variables They Point To.

#include <stdio.h>

int main()
{
    char choice;
    int num1;
    float num2;

    printf("Please Enter a Single Character : ");
    scanf("%c", &choice);

    printf("Please Enter an Integral Value : ");
    scanf("%d", &num1);

    printf("Please Enter a Floating Value : ");
    scanf("%f", &num2);

    int *intPointer = &num1;
    float *floatPointer = &num2;
    char *charPointer = &choice;

    printf("The Integral Value And It's Corresponding Pointer Value Are As Follows : %d & %d\n", num1, *intPointer);
    printf("The Address Of The Integral Value Is : %p\n", (void*)intPointer);

    printf("The Floating Value And It's Corresponding Pointer Value Are As Follows : %.2f & %.2f\n", num2, *floatPointer);
    printf("The Address Of The Floating Value Is : %p\n", (void*)floatPointer);

    printf("The Character Value And It's Corresponding Pointer Value Are As Follows : %c & %c\n", choice, *charPointer);
    printf("The Address Of The Character Is : %p", (void*)charPointer);

    return 0;
}