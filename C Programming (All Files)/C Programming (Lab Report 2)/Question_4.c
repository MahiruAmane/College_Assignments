// Write a C Program To Read Two Matrices A (m x n) And B (p x q) And Computes The Product A and B. Read Matrix A and Matrix B In Row Major Order Respectively. Print Both The Input Matrices And Resultant Matrix With Suitable Headings And Output Should Be in Matrix Format Only. Program Must Check The Compatibility Of Orders Of The Matrices For Multiplication. Report Appropriate Message In Case Of Incompatibility.

#include <stdio.h>

int main()
{
    int row1, row2;
    int column1, column2;

    printf("Enter Number Of Rows And Columns For Matrix A : ");
    scanf("%d %d", &row1, &column1);

    printf("Enter Number Of Rows and Columns For Matrix B : ");
    scanf("%d %d", &row2, &column2);

    int Matrix_A[row1][column1];
    int Matrix_B[row2][column2];
    int Matrix_C[row1][column2];

    if (column1 != row2)
    {
        printf("Matrix Multiplication Is Not Possible\n");
        printf("The Matrix A (Column) Should Be Equal To Matrix B (Row) To Compute Matrix Multiplication\n");
        return 0;
    }

    printf("\n");
    printf("Please Enter Elements Of Matrix A\n");

    for(int i = 0; i < row1; i++)
    {
        for(int j = 0; j < column1; j++)
        {
            printf("Please Enter The Element (%d,%d) : ", i + 1, j + 1);
            scanf("%d", &Matrix_A[i][j]);
        }
    }

    printf("Please Enter Elements Of Matrix B\n");

    for(int i = 0; i < row2; i++)
    {
        for(int j = 0; j < column2; j++)
        {
            printf("Please Enter The Element (%d,%d) : ", i + 1, j + 1);
            scanf("%d", &Matrix_B[i][j]);
        }
    }

    printf("\n");

    printf("The Elements Of Matrix A Are as Follows : \n");
    printf("\n");

    for(int i = 0; i < row1; i++)
    {
        for(int j = 0; j < column1; j++)
        {
            printf("Element (%d,%d) Of Matrix A Is : %d\n", i + 1, j + 1, Matrix_A[i][j]);
        }
    }

    printf("\n");
    printf("The Elements Of Matrix B Are as Follows : \n");
    printf("\n");

    for(int i = 0; i < row2; i++)
    {
        for(int j = 0; j < column2; j++)
        {
            printf("Element (%d,%d) Of Matrix B Is : %d\n", i + 1, j + 1, Matrix_B[i][j]);
        }
    }

    for (int i = 0; i < row1; i++)
    {
        for (int j = 0; j < column2; j++)
        {
            Matrix_C[i][j] = 0;

            for (int k = 0; k < column1; k++)
            {
                Matrix_C[i][j] = Matrix_C[i][j] + (Matrix_A[i][k] * Matrix_B[k][j]); 
            }
        }
    }

    printf("\n");
    printf("The Elements Of Matrix C Are as Follows : \n");
    printf("\n");

    for(int i = 0; i < row1; i++)
    {
        for(int j = 0; j < column2; j++)
        {
            printf("Element (%d,%d) Of Matrix C Is : %d\n", i + 1, j + 1, Matrix_C[i][j]);
        }
    }

    printf("\n");

    return 0;
}