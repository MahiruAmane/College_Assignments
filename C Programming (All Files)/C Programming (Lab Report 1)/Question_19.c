// Write a C Program To Declare a Local Variable Inside a Function And Try To Access It Outside The Function. Compare This With Accessing The Global Variable From Within The Function.

#include <stdio.h>

int global = 10;

void LocalFunction()
{
    int local;

    printf("Please Enter a Number : ");
    scanf("%d", &local);

    printf("The Variable Inside It's Own Function Is : %d\n", local);
    printf("The Global Variable (Outside The Main Function) Is : %d\n", global);
}

int main()
{
    printf("The Global Variable (Inside The Main Function) Is : %d\n", global);
    
    // printf("The Local Variable Value Outside Of It's Function Is : %d", local);
    // Identifier "local" Is Undefined (Because We Are Trying To Access It's Value Outside Of It's Home Function)

    LocalFunction();

    return 0;
}