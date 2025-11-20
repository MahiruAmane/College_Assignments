// Write a C Program To Use a Function to Check If a Number is Prime (Arguments, Return Value).

#include <stdio.h>
#include <math.h>

int CheckPrime(int x)
{
    if (x <= 1)
    {
        return 0;
    }
    else
    {
        for (int i = 2; i <= sqrt(x); i++)
        {
            if (x % i == 0)
            {
                return 0;
            }
            else
            {
                return 1;
            }
        }
    }

}

int main()
{
    int number;

    printf("Please Enter a Number To Check Whether It Is Prime Or Not : ");
    scanf("%d", &number);

    if (CheckPrime(number))
    {
        printf("%d Is a Prime Number", number);
    }
    else
    {
        printf("%d Is Not a Prime Number", number);
    }

    return 0;
}