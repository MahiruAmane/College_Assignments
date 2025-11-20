// Write a C Program To Demonstrate Shadowing Of a Global Variable By a Local Variable.

#include <stdio.h>

void function()
{
    int global = 10;

    printf("The Original Global Variable Is : %d", global);
}

int main()
{
    int global;

    printf("Please Enter a Number That Will Shadow The Global Variable : ");
    scanf("%d", &global);

    printf("The Local Variable You Entered Is : %d\n", global);

    function();

    return 0;
}