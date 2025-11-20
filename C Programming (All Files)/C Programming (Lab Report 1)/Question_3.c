// Write a C Program That Prompts The User To Enter Their Name And Age.

#include <stdio.h>
#include <string.h>

int main()
{
    int age;
    char name[128];

    printf("Please Enter Your Name : ");
    fgets(name, sizeof(name), stdin);
    name[strcspn(name, "\n")] = '\0';

    printf("Please Enter Your Age : ");
    scanf("%d", &age);

    printf("Your Name Is %s And Your Age Is %d", name, age);

    return 0;
}