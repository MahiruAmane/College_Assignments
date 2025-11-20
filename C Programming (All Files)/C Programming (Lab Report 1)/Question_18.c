// Write a C Program To Declare a Global Variable Outside All Functions And Use It Inside Various Functions To Understand Its Accessibility.

#include <stdio.h>

int global = 10;

void Function()
{
    printf("The Global Variable (Outside The Main Function) Is : %d", global);
}

int main()
{
    printf("The Global Variable (Inside The Main Function) Is : %d\n", global);
    
    int global;

    printf("Please Enter a Number To Shadow The Global Variable : ");
    scanf("%d", &global);

    printf("The Local Variable (Inside The Main Function) Is : %d\n", global);

    Function();

    return 0;
}