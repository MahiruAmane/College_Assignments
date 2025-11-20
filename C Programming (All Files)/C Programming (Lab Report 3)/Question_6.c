// Write a C Program To Open an Existing File And Read Its Content Character By Character, And Then Close The File.

#include <stdio.h>

int main()
{
    FILE *file;
    char character;

    file = fopen("example.txt", "r");

    if (file == NULL)
    {
        printf("There Was An Error Opening The File");
        return 1;
    }

    while ((character = fgetc(file)) != EOF)
    {
        putchar(character);
    }

    fclose(file);

    return 0;
}