// Write a Program To Generate The Following Set Of Output.

#include <stdio.h>

int main()
{
    int num;

    printf("Please Enter How Many Rows Of The Pattern You Would Like To See : ");
    scanf("%d", &num);

    for (int i = 0; i < num; i++)
    {
        for (int k = num - i ; k > 0; k--)
        {
            printf(" ");
        }

        int value = 1;

        for (int j = 0; j <= i; j++)
        {
            printf("%d ", value);
            value = value * (i - j) / (j + 1);
        }

        printf("\n");
    }

    return 0;
}