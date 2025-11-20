// Write a C Program To Declare a Static Local Variable Inside a Function. Observe How Its Value Persists Across Function Calls.

#include <stdio.h>

int Function()
{
    static int num;
    printf("The Value Of The Static Variable Is : %d\n", num);
    num++;
}

int main()
{
    int n;

    printf("Please Enter How Many Times You Want To Call The Function : ");
    scanf("%d", &n);

    for (int i = 1; i <= n; i++)
    {
        Function();
    }

    return 0;
}