// Write a C Program To Read a List Of Integers From The User And Store It In a Single Dimensional Array. Also Find The Frequency Of a Particular Number In a List Of Integers.

#include <stdio.h>

int main()
{
    int n;
    int num;
    int find;
    int count = 0;

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

    printf("Please Enter The Number You Want To Find (Also Shows Frequency) : ");
    scanf("%d", &find);

    for (int i = 0; i < n; i++)
    {
        if (arr[i] == find)
        {
            count = count + 1;
        }
    }

    if (count == 0)
    {
        printf("The Number %d Is Not Present In The Array", find);
    }
    else
    {
        printf("The Number %d Is There And Has Appeared %d Times", find, count);
    }

    return 0;
}