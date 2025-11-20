// Write a C Program To Check If The Triangle Is Valid Or Not. If The Validity Is Established, Do Check If The Triangle Is Scalene, Isosceles, Equilateral Or Right Angled Triangle.

#include <stdio.h>
#include <math.h>
#define error 0.0001

int main()
{
    float side1;
    float side2;
    float side3;
    float largest;
    float sidex;
    float sidey;

    printf("Please Enter The First Side Of The Triangle : ");
    scanf("%f", &side1);

    printf("Please Enter The Second Side Of The Triangle : ");
    scanf("%f", &side2);

    printf("Please Enter The Third Side Of The Triangle : ");
    scanf("%f", &side3);

    if (side1 > side2 && side1 > side3)
    {
        largest = side1;
        sidex = side2;
        sidey = side3;
    }
    else if (side2 > side1 && side2 > side3)
    {
        largest = side2;
        sidex = side1;
        sidey = side3;
    }
    else
    {
        largest = side3;
        sidex = side1;
        sidey = side2;
    }

    if (side1 > 0 && side2 > 0 && side3 > 0 && side1 + side2 > side3 && side1 + side3 > side2 && side2 + side3 > side1)
    {
        printf("The Triangle Is Valid\n");

        if (side1 == side2 && side1 ==side3)
        {
            printf("The Triangle Is Equilateral");
        }
        else if (fabs((largest * largest) - ((sidex * sidex) + (sidey * sidey))) < error)
        {
            printf("The Triangle Is a Right Angled Triangle\n");

            if (side1 == side2 || side1 == side3 || side2 == side3)
            {
                printf("The Triangle Is Isosceles");
            }
            else
            {
                printf("The Triangle Is Scalene");
            }
        }
        else
        {
            printf("The Triangle Is Not a Right Angled Triangle\n");

            if (side1 == side2 || side1 == side3 || side2 == side3)
            {
                printf("The Triangle Is Isosceles");
            }
            else
            {
                printf("The Triangle Is Scalene");
            }
        }
    }
    else
    {
        printf("The Triangle Is Not Valid");
    }

    return 0;
}