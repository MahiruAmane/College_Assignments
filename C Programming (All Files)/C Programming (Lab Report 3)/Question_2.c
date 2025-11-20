// Write a C Program To Compute The Monthly Pay Of 100 Employees Using Each Employee's Name & Salary. The Dearness Allowance Is Computed As 52 % Of The Employee's Salary. Print The Employee's Name And Gross Salary.

#include <stdio.h>
#include <string.h>

struct Information
{
    char employee_name[64];
    float employee_salary;
    float gross_salary;
};

struct Information readInput(int n1, int allowance)
{
    struct Information c;

    getchar();

    printf("Please Enter The Name Of Employee Number %d : ", n1 + 1);
    fgets(c.employee_name, sizeof(c.employee_name), stdin);
    c.employee_name[strcspn(c.employee_name, "\n")] = '\0';

    printf("Please Enter The Salary Of Employee Number %d : ", n1 + 1);
    scanf("%f", &c.employee_salary);

    c.gross_salary = c.employee_salary + ((allowance * c.employee_salary) / 100);

    return c;
};

void writeOutput(struct Information a)
{
    printf("The Name Of The Employee Is : %s\n", a.employee_name);
    printf("The Base Salary Of %s Is : %.2f\n", a.employee_name, a.employee_salary);
    printf("The Gross Salary Of %s Is : %.2f\n", a.employee_name, a.gross_salary);
}

int main()
{
    struct Information employee[100];
    int n;
    float da;

    printf("Please Enter The Number Of Employee's You Want To Enter : ");
    scanf("%d", &n);

    if (n > 100)
    {
        printf("This Program Only Supports Upto 100 Employee's\n");
        return 1;
    }
    else if (n <= 0)
    {
        printf("Program Closed Successfully");
        return 1;
    }

    printf("Please Enter The Dearness Allowance (In Percentage) : ");
    scanf("%f", &da);

    printf("\n");

    for (int i = 0; i < n; i++)
    {
        printf("Please Enter The Details About The Employee %d \n", i + 1);
        employee[i] = readInput(i, da);
        printf("\n");
    }

    printf("\n");

    for (int i = 0; i < n; i++)
    {
        printf("The Details About The Employee %d Are As Follows : \n", i + 1);
        writeOutput(employee[i]);
        printf("\n");
    }

    return 0;
}