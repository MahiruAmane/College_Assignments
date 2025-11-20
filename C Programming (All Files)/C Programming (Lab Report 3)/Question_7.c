// Write a C Program To Open a File, Read It's Content Line By Line, And Display Each Line On The Console.

#include <stdio.h>

int main()
{
    FILE *file;
    char lines[100];

    file = fopen("example.txt", "r");

    if (file == NULL)
    {
        printf("There Was An Error Opening The File");
        return 1;
    }

    while (fgets(lines, sizeof(lines), file) != NULL);
    {
        printf("%s", lines);
    }

    fclose(file);

    return 0;
}