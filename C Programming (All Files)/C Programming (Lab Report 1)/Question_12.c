// Write a C Program To Enter Numbers Till The User Wants. At The End It Should Display The Count Of Positive, Negative, And Zeroes Entered.

#include <stdio.h>

int main()
{
    int number;
    int value;
    int positive = 0;
    int negative = 0;
    int zero = 0;

    printf("Please Enter How Many Numbers You Want To Input : ");
    scanf("%d", &number);

    for (int i = 1; i <= number; i++)
    {
        printf("Please Enter The Number Of Your Choice : ");
        scanf("%d", &value);

        if (value == 0)
        {
            zero = zero + 1;
        }
        else if (value > 0)
        {
            positive = positive + 1;
        }
        else
        {
            negative = negative + 1;
        }
    }

    printf("The Number Of Positive Numbers Entered Are : %d\n", positive);
    printf("The Number Of Negative Numbers Entered Are : %d\n", negative);
    printf("The Number Of Zero's Entered Are : %d", zero);

    return 0;
}