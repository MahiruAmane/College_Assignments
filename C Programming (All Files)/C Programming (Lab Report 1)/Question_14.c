// Write a Program To Generate The Following Set Of Output.

#include <stdio.h>

int main()
{
    int num;
    int value = 1;

    printf("Please Enter How Many Rows Of The Pattern You Would Like To See : ");
    scanf("%d", &num);

    for (int i = 1; i <= num; i++)
    {
        for (int k = num - i ; k >= 0; k--)
        {
            printf(" ");
        }

        for (int j = 1; j <= i; j++)
        {
            printf("%d ", value);
            value = value + 1;
        }

        printf("\n");
    }
    
    return 0;
}