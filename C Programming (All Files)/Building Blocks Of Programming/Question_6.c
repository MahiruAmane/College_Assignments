// Write a C Program To Implement a Switch Case Calculator That Supports (+, -, *, /).

#include <stdio.h>

int main()
{
    char operation;

    printf("Please Enter The Operation You Want To Perform : ");
    scanf("%c", &operation);

    int num1;
    int num2;
    int result;

    printf("Please Enter The First Number : ");
    scanf("%d", &num1);

    printf("Please Enter The Second Number : ");
    scanf("%d", &num2);

    switch(operation)
    {
        case '+':
        {
            result = num1 + num2;
            printf("The Addition Of %d and %d Is : %d", num1, num2, result);
            break;
        }
        case '-':
        {
            result = num1 - num2;
            printf("The Subtraction Of %d and %d Is : %d", num1, num2, result);
            break;
        }
        case '*':
        {
            result = num1 * num2;
            printf("The Multiplication Of %d and %d Is : %d", num1, num2, result);
            break;
        }
        case '/':
        {
            if (num2 == 0)
            {
                printf("Division By Zero Is Not Defined");
                break;
            }
            else
            {
                result = num1 / num2;
                printf("The Division Of %d and %d Is : %d", num1, num2, result);
                break;
            }
        }
        default:
        {
            printf("Invalid Operation Used Please Use (Add, Subtract, Multiply Or Divide)");
            break;
        }
    }

    return 0;
}