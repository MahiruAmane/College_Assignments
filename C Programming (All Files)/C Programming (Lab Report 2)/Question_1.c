// Write a C Program To Read a List Of Integers From The User and Store It In a Single Dimensional Array. Also Compute The Second Largest Integer In The List Of Integers.

#include <stdio.h>

int main()
{
    int n;
    int num;
    int temp;

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

    if (n >= 2)
    {
        for (int i = 0; i < n; i++)
        {
            for (int j = i; j < n - 1; j++)
            {
                if (arr[j] > arr[j + 1])
                {
                    temp = arr[j];
                    arr[j] = arr[j + 1];
                    arr[j + 1] = temp;
                }
            }

        }
    }
    else
    {
        printf("Please Input More Numbers In The Array To Find The Second Largest Number\n");
    }

    if (n >= 2)
    {
        printf("The Second Largest Number In The Array Is : %d", arr[n - 2]);
    }

    return 0;
}