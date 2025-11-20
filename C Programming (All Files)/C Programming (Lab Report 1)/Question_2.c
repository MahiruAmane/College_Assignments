// Write a C Program To Print The Address In Multiple Lines.

#include <stdio.h>
#include <string.h>

int main()
{
    char address1[128];
    char address2[128];
    char address3[128];

    printf("Please Enter The First Line Of Address : ");
    fgets(address1, sizeof(address1), stdin);
    address1[strcspn(address1, "\n")] = '\0';


    printf("Please Enter The Second Line Of Address : ");
    fgets(address2, sizeof(address2), stdin);
    address2[strcspn(address2, "\n")] = '\0';


    printf("Please Enter The Third Line Of Address : ");
    fgets(address3, sizeof(address3), stdin);
    address3[strcspn(address3, "\n")] = '\0';

    printf("Your Complete Address Is Given Below : \n%s \n%s \n%s", address1, address2, address3);

    return 0;
}