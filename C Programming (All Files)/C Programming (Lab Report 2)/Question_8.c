// Write a C Program To Use The Function ISPRIME (num1) That Accepts an Integer Argument and Returns 1 If The Argument Is Prime, 0 Otherwise. Use This Function To Generate Prime Numbers Between The Given Ranges. 

#include <stdio.h>
#include <math.h>

int Prime(int prime)
{
    if (prime <= 1)
    {
        return 0;
    }
    else 
    {
        for (int i = 2; i <= sqrt(prime); i++)
        {
            if (prime % i == 0)
            {
                return 0;
            }
        }

        return 1;
    }
}

int main()
{
    int n;
    int count = 0;

    printf("Please Enter An Upper Limit To Check For Prime Numbers : ");
    scanf("%d", &n);

    for (int i = 1; i <= n; i++)
    {
        if (Prime(i))
        {
            printf("%d Is A Prime Number\n", i);
            count++;
        }
    }

    printf("There Were a Total Of %d Prime Numbers Between 2 And %d", count, n);

    return 0;
}