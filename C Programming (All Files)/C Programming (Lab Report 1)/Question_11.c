// Write a C Program Using Ternary Operator, Where The User Should Input The Length And Breadth Of a Rectangle, One Has To Find Out Which Rectangle Has The Highest Perimeter (The Minimum Number Of Rectangles Should Be Three).

#include <stdio.h>

int main()
{
    int num;
    float length;
    float breadth;
    float perimeter;
    float max_perimeter = 0;

    printf("Please Enter How Many Rectangles You Want To Compare : ");
    scanf("%d", &num);

    for (int i = 1; i <= num; i++)
    {
        printf("Please Enter The Length Of The Rectangle %d : ", i);
        scanf("%f", &length);

        printf("Please Enter The Breadth Of The Rectangle %d : ", i);
        scanf("%f", &breadth);

        perimeter = 2 * (length + breadth);

        max_perimeter = (perimeter > max_perimeter) ? perimeter : max_perimeter;
    }

    printf("The Largest Perimeter After Comparing All The Rectangles Is : %.2f", max_perimeter);

    return 0;
}