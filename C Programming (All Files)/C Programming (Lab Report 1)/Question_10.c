// Write a C Program That Determines The Day Of The Week for January 1st Of Any Given Year, Based On The Fact That January 1st, 0001 Was a Monday According To The Gregorian Calendar.

#include <stdio.h>

int main()
{
    int year;
    int leap_year = 0;
    int normal_year = 0;
    int days = 0;
    int week;

    printf("Please Enter The Year : ");
    scanf("%d", &year);

    for (int i = 1; i < year; i++)
    {
        if (i % 4 == 0 && i % 100 != 0 || i % 400 == 0)
        {
            leap_year = leap_year + 1;
        }
        else
        {
            normal_year = normal_year + 1;
        }
    }

    days = (leap_year * 366) + (normal_year * 365);
    week = (days % 7);

    switch(week)
    {
        case 0:
        {
            printf("Monday");
            break;
        }
        case 1:
        {
            printf("Tuesday");
            break;
        }
        case 2:
        {
            printf("Wednesday");
            break;
        }
        case 3:
        {
            printf("Thursday");
            break;
        }
        case 4:
        {
            printf("Friday");
            break;
        }
        case 5:
        {
            printf("Saturday");
            break;
        }
        case 6:
        {
            printf("Sunday");
            break;
        }
    }

    return 0;
}