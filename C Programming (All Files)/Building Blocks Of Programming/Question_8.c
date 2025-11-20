// Write a C Program To Use While Loop To Print Fibonacci Series Up To n Terms.

#include <stdio.h>

int main()
{
    int num;
    int i = 0;
    int value1 = 0;
    int value2 = 1;
    int sum;

    printf("Please Enter The Number Of Terms Of The Fibonacci Series : ");
    scanf("%d", &num);

    printf("Fibonacci Series Up To %d Terms : ", num);

    while (i < num)
    {
        printf("%d ", value1);
        sum = value1 + value2;
        value1 = value2;
        value2 = sum;
        i++;
    }

    return 0;
}