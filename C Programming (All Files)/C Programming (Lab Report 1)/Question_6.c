// Write a C Program To Convert Temperature From Celsius To Fahrenheit.

#include <stdio.h>

int main()
{
    float celsius;
    float fahrenheit;

    printf("Please Enter The Temperature In Celsius : ");
    scanf("%f", & celsius);

    fahrenheit = (celsius * 9/5) + 32;

    printf("The Temperature In Fahrenheit Is : %.2f", fahrenheit);
    
    return 0;
}