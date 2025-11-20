// Write a C Program To Read a List Of Integers From The User and Store It In a Single Dimensional Array. Also Count And Display Positive, Negative, Odd, and Even Numbers In The Array.

#include <stdio.h>

int main()
{
    int n;
    int num;
    int even = 0;
    int odd = 0;
    int positive = 0;
    int negative = 0;

    printf("Please Enter How Many Numbers You Want In The Array : ");
    scanf("%d", &n);

    int arr[n];

    for (int i = 0; i < n; i++)
    {
        printf("Please Enter The Element %d In The Array : ", i + 1);
        scanf("%d", &num);

        arr[i] = num;
    }

    for (int i = 0; i < n; i++)
    {
        printf("Element %d In The Array Is : %d\n", i + 1, arr[i]);
    }

    for (int i = 0; i < n; i++)
    {
        if (arr[i] % 2 == 0)
        {
            even = even + 1;

            if (arr[i] > 0)
            {
                positive = positive + 1;
            }
            else
            {
                negative = negative + 1;
            }
        }
        else
        {
            odd = odd + 1;

            if (arr[i] > 0)
            {
                positive = positive + 1;
            }
            else
            {
                negative = negative + 1;
            }
        }

    }

    printf("The Number Of Even Numbers In The Array Are : %d\n", even);
    printf("The Number Of Odd Numbers In The Array Are : %d\n", odd);
    printf("The Number Of Positive Numbers In The Array Are : %d\n", positive);
    printf("The Number Of Negative Numbers In The Array Are : %d", negative);

    return 0;
}