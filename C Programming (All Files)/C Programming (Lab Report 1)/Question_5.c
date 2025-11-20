// Write a C Program To Calculate The Area and Perimeter Of a Rectangle Based On Its Length And Breadth.

#include <stdio.h>

int main()
{
    float length;
    float breadth;
    float area;
    float perimeter;

    printf("Please Enter The Length Of The Rectangle : ");
    scanf("%f", &length);

    printf("Please Enter The Breadth Of The Rectangle : ");
    scanf("%f", &breadth);

    perimeter = 2 * (length + breadth);
    area = length * breadth;

    printf("The Area Of The Rectangle Is : %.2f\n", area);
    printf("The Perimeter Of The Rectangle Is : %.2f", perimeter);

    return 0;
}