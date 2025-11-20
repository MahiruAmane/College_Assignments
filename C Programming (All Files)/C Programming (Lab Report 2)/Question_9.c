// Write a C Program To Use The Function REVERSE (str) That Accepts a String Argument. Use This Function To Find The Reverse Of a Given String.

#include <stdio.h>
#include <string.h>

int ReverseString(char reverse[])
{
    int length = strlen(reverse);
    char temp;

    for (int i = 0; i < length / 2; i++)
    {
        temp = reverse[i];
        reverse[i] = reverse[length - i - 1];
        reverse[length - i - 1] = temp;
    }

    printf("The Reversed String Is : %s", reverse);
}

int main()
{
    char string[128];

    printf("Please Enter a String : ");
    scanf("%s", &string);

    ReverseString(string);

    return 0;
}