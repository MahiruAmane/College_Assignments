// Write a C Program To Apply Left Shift And Right Shift Operator.

#include <stdio.h>

int main()
{
    int num1;
    int shifter;
    int n;

    printf("Please Enter The First Number : ");
    scanf("%d", &num1);

    printf("Please Enter How Many Bits You Want To Shift : ");
    scanf("%d", &n);

    shifter = num1 << n;
    printf("Left Shift Adds 0 Towards The Left Side (The Binary Value Get's Changed)\n");
    printf("After Applying Left Shift %d Becomes : %d\n", num1, shifter);

    shifter = num1 >> n;
    printf("Right Shift Adds 0 Towards The Right Side (The Binary Value Get's Changed)\n");
    printf("After Applying Right Shift %d Becomes : %d", num1, shifter);

    return 0;
}