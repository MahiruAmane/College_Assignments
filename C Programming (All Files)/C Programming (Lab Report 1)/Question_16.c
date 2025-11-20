// Write a C Program To Determine The Population At The End Of Each Year In The Last Decade.

#include <stdio.h>

int main()
{
    int population;
    int years;
    int rate;

    printf("Please Enter The Current Population Of The Town : ");
    scanf("%d", &population);

    printf("Please Enter The Rate Of Increase Of The Population : ");
    scanf("%d", &rate);

    printf("Please Enter The Total Survey Time (In Years) : ");
    scanf("%d", &years);

    for (int i = 1; i <= years; i++)
    {
        population = population + population * (rate * 0.01);
    }

    printf("The Population Of The Town After %d Years Is : %d", years, population);

    return 0;
}