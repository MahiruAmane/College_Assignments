// Write a C Program To Perform Pointer Arithmetic (Increment And Decrement) On Pointers Of Different Data Types. Observe How The Memory Addresses Change And The Effects On Data Access.

#include <stdio.h>

int main()
{
    int n1;
    int n2;
    int n3;

    printf("Please Enter The Maximum Length Of The Character Array : ");
    scanf("%d", &n1);

    printf("Please Enter The Maximum Length Of The Integral Array : ");
    scanf("%d", &n2);

    printf("Please Enter The Maximum Length Of The Floating Arrays : ");
    scanf("%d", &n3);

    char choice[n1];
    int num1[n2];
    float num2[n3];

    printf("\n");

    for (int i = 0; i < n1; i++)
    {
        printf("Enter Element %d of the Character Array: ", i + 1);
        scanf(" %c", &choice[i]);
    }

    for (int i = 0; i < n2; i++)
    {
        printf("Enter Element %d of the Integer Array: ", i + 1);
        scanf("%d", &num1[i]);
    }

    for (int i = 0; i < n3; i++)
    {
        printf("Enter Element %d of the Float Array: ", i + 1);
        scanf("%f", &num2[i]);
    }

    char *charPointer = choice;
    int *intPointer = num1;
    float *floatPointer = num2;

    printf("\n");

    for (int i = 0; i < n1; i++)
    {
        printf("The Value Of Element %d In The Character Array Is : %c\n", i + 1, *charPointer);
        printf("The Address Of The Character Is : %p\n", (void*)charPointer);
        charPointer++;
    }

    printf("\n");

    for (int i = 0; i < n2; i++)
    {
        printf("The Value Of Element %d In The Integral Array Is : %d\n", i + 1, *intPointer);
        printf("The Address Of The Character Is : %p\n", (void*)intPointer);
        intPointer++;
    }

    printf("\n");

    for (int i = 0; i < n3; i++)
    {
        printf("The Value Of Element %d In The Floating Array Is : %.2f\n", i + 1, *floatPointer);
        printf("The Address Of The Character Is : %p\n", (void*)floatPointer);
        floatPointer++;
    }

    printf("\n");

    return 0;
}