// Write a C Program To Calculate a Person's Body Mass Index (BMI) and Display The Corresponding BMI Category.

#include <stdio.h>

int main()
{
    float height;
    float weight;
    float bmi;

    printf("Please Enter Your Weight (In Kilograms) : ");
    scanf("%f", &weight);

    printf("Please Enter Your Height (In Meters) : ");
    scanf("%f", &height);

    bmi = weight / (height * height);

    if (bmi < 18.5)
    {
        printf("Your Body Mass Index Is : %.2f\n", bmi);
        printf("You Are Under Weight");
    }
    else if (bmi < 25)
    {
        printf("Your Body Mass Index Is : %.2f\n", bmi);
        printf("You Have Normal Weight");
    }
    else if (bmi < 30)
    {
        printf("Your Body Mass Index Is : %.2f\n", bmi);
        printf("You Are Over Weight");
    }
    else if (bmi < 35)
    {
        printf("Your Body Mass Index Is : %.2f\n", bmi);
        printf("You Have Obesity Class I (Moderate)");
    }
    else if (bmi < 40)
    {
        printf("Your Body Mass Index Is : %.2f \n", bmi);
        printf("You Have Obesity Class II (Severe)");
    }
    else
    {
        printf("Your Body Mass Index Is : %.2f\n", bmi);
        printf("You Have Obesity Class III (Morbid)");
    }

    return 0;
}