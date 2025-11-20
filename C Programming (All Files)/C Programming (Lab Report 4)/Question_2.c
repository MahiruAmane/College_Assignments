// Write a C Program To Define a Function In Directives.

#include <stdio.h>
#define SQUARE(x) ((x) * (x))

int main() 
{
    int num;
    int result;

    printf("Please Enter a Number To Know It's Square : ");
    scanf("%d", &num);

    result = SQUARE(num);
    
    printf("The Square Of The Given Number %d Is : %d", num, result);
    
    return 0;
}