// Write a C Program To Create a New File And Write Text Into It.

#include <stdio.h>
#include <string.h>

int main()
{
    char lines[128];
    FILE *file;

    file = fopen("example.txt", "w");

    if (file == NULL)
    {
        printf("There Was An Error Opening The File");
        return 1;
    }

    printf("Please Enter What You Want To Write In The File : ");
    fgets(lines, sizeof(lines), stdin);
    lines[strcspn(lines, "\n")] = '\0';

    fprintf(file, "%s", lines);
    fclose(file);

    printf("The Data Has Been Successfully Written Into The File");

    return 0;
}