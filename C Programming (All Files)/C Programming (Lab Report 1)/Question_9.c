// Write a C Program To Check If Three Points (x1, y1), (x2, y2) And (x3, y3) Are Collinear Or Not.

#include <stdio.h>
#include <math.h>

int main()
{
    int x1, y1;
    int x2, y2;
    int x3, y3;
    float area;

    printf("Please Enter The First Set Of Coordinates : ");
    scanf("%d %d", &x1, &y1);

    printf("Please Enter The Second Set Of Coordinates : ");
    scanf("%d %d", &x2, &y2);

    printf("Please Enter The Third Set Of Coordinates : ");
    scanf("%d %d", &x3, &y3);

    area = 0.5 * fabs(x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2));

    if (area == 0)
    {
        printf("The Given Set Of Coordinates Are Collinear");
    }
    else
    {
        printf("The Given Set Of Coordinates Are Not Collinear");
    }

    return 0;
}