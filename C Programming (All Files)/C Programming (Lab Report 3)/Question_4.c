// Write a C Program To Create an Union Containing 6 Strings (Name, Home_Address, Current_Address, City, State And Postal Code).

#include <stdio.h>
#include <string.h>

union Address
{
    char name[64];
    char home_address[128];
    char current_address[128];
    char city[64];
    char state[64];
    int postal_code;
};


int main()
{
    union Address c;

    printf("Please Enter Your Name : ");
    fgets(c.name, sizeof(c.name), stdin);
    c.name[strcspn(c.name, "\n")] = '\0';

    printf("Your Name Is : %s", c.name);
    printf("\n");

    printf("Please Enter Your Home Address : ");
    fgets(c.home_address, sizeof(c.home_address), stdin);
    c.home_address[strcspn(c.home_address, "\n")] = '\0';

    printf("Your Home Address Is : %s", c.home_address);
    printf("\n");

    printf("Please Enter Your Current Address : ");
    fgets(c.current_address, sizeof(c.current_address), stdin);
    c.current_address[strcspn(c.current_address, "\n")] = '\0';

    printf("Your Current Address Is : %s", c.current_address);
    printf("\n");

    printf("Please Enter Your Home City : ");
    fgets(c.city, sizeof(c.city), stdin);
    c.city[strcspn(c.city, "\n")] = '\0';

    printf("Your Home City Is : %s", c.city);
    printf("\n");

    printf("Please Enter Your Home State : ");
    fgets(c.state, sizeof(c.state), stdin);
    c.city[strcspn(c.state, "\n")] = '\0';

    printf("Your Home State Is : %s", c.state);
    printf("\n");

    printf("Please Enter Your Postal Code : ");
    scanf("%d", &c.postal_code);

    printf("Your Postal Code Is : %d", c.postal_code);
    printf("\n");

    return 0;
}