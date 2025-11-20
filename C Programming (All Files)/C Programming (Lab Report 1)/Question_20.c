// Write a C Program To Declare Variables Within Different Code Blocks (Enclosed By Curly Braces) and Test Their Accessibility Within and Outside Those Blocks.

#include <stdio.h>

int main()
{
    {
        int num1;

        printf("The First Variable Declared Inside It's Code Block Is : ");
        scanf("%d", &num1);

        printf("The First Variable Inside It's Code Block Is : %d\n", num1);
    }

    {
        int num2;

        printf("The Second Variable Declared Inside It's Code Block Is : ");
        scanf("%d", &num2);

        printf("The Second Variable Inside It's Code Block Is : %d", num2);

        // printf("The Variable Inside It's Code Block Is : %d", num1);
        // Identifier "num1" Is Undefined (Because We Are Trying To Access It's Value Outside Of It's Home Code Block)
    }

    // printf("The Variable Outside It's Code Block Is : %d", num1);
    // Identifier "num1" Is Undefined (Because We Are Trying To Access It's Value Outside Of It's Home Code Block)

    return 0;
}