// Write a C Program To Use The Function That Accepts Pointers as Parameters. Pass Variables By Reference Using Pointers And Modify Their Values Within The Function.

#include <stdio.h>

int Pointer(int *a, int *b)
{
    *a = *a * 2;
    *b = *b * 2;

    printf("The Modified Value Of The First Number Is : %d\n", *a);
    printf("The Modified Value Of The Second Number Is : %d", *b); 
}

int main()
{
    int x;
    int y;

    printf("Please Enter The First Number : ");
    scanf("%d", &x);

    printf("Please Enter The Second Number : ");
    scanf("%d", &y);

    printf("The Original Value Of The First Number Is : %d\n", x);
    printf("The Original Value Of The Second Number Is : %d\n", y);

    Pointer(&x, &y);

    return 0;
}