// Write a C Program TO Create a Book Structure Containing Book ID, Title, Price And Author Name.

#include <stdio.h>
#include <string.h>

struct Information
{
    char book_title[64];
    char author_name[64];
    int book_id;
    float price;
};

struct Information readInput()
{
    struct Information c;

    getchar();

    printf("Please Enter The Book Name : ");
    fgets(c.book_title, sizeof(c.book_title), stdin);
    c.book_title[strcspn(c.book_title, "\n")] = '\0';

    printf("Please Enter The Author Name : ");
    fgets(c.author_name, sizeof(c.author_name), stdin);
    c.author_name[strcspn(c.author_name, "\n")] = '\0';

    printf("Please Enter The Book Identification Number : ");
    scanf("%d", &c.book_id);

    printf("Please Enter The Price Of The Book : ");
    scanf("%f", &c.price);

    return c;
};

void writeOutput(struct Information a)
{
    printf("The Name Of The Book Is : %s\n", a.book_title);
    printf("The Author Of The Book %s Is : %s\n", a.book_title, a.author_name);
    printf("The Book Identification Number Is : %d\n", a.book_id);
    printf("The Price Of The Book %s Is : %.2f\n", a.book_title, a.price);
}

int main()
{
    struct Information books[25];
    int n;

    printf("Please Enter How Many Books You Want To Enter : ");
    scanf("%d", &n);

    if (n > 25)
    {
        printf("This Program Only Supports Upto 25 Unique Book Logs");
        return 1;
    }
    else if (n <= 0)
    {
        printf("Program Closed Successfully");
        return 1;
    }

    printf("\n");

    for (int i = 0; i < n; i++)
    {
        printf("Please Enter The Details About The Book Log %d ", i + 1);
        printf("\n");
        books[i] = readInput();
        printf("\n");
    }

    for (int i = 0; i < n; i++)
    {
        printf("The Details About The Book Log %d Are As Follows ", i + 1);
        printf("\n");
        writeOutput(books[i]);
        printf("\n");
    }

    return 0;
}