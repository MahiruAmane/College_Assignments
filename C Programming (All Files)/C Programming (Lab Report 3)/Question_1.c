// Write a C Program That Uses Functions To Perform The Following Operations (Read, Write, Addition And Subtraction Of Complex Numbers Using a Structure).

#include <stdio.h>

struct Complex 
{
    float real;
    float imag;
};

struct Complex readComplex()
{
    struct Complex c;

    printf("Please Enter The Real Part Of The Complex Number : ");
    scanf("%f", &c.real);

    printf("Enter Enter The Imaginary Part Of The Complex Number : ");
    scanf("%f", &c.imag);

    return c;
}

void writeComplex(struct Complex c)
{
    if (c.imag == 0)
    {
        printf("%.2f\n", c.real);
    }
    else if (c.imag > 0)
    {
        printf("%.2f + %.2fi\n", c.real, c.imag);
    }
    else
    {
        printf("%.2f - %.2fi\n", c.real, -c.imag);
    }    
}   

struct Complex addComplex(struct Complex a, struct Complex b)
{
    struct Complex result;

    result.real = a.real + b.real;
    result.imag = a.imag + b.imag;

    return result;
}

struct Complex subtractComplex(struct Complex a, struct Complex b) 
{
    struct Complex result;

    result.real = a.real - b.real;
    result.imag = a.imag - b.imag;

    return result;
}

int main()
{
    struct Complex c1, c2, sum, diff;

    printf("Please Enter The First Complex Number\n");
    c1 = readComplex();
    printf("\n");

    printf("Please Enter The Second Complex Number\n");
    c2 = readComplex();
    printf("\n");

    sum = addComplex(c1, c2);
    diff = subtractComplex(c1, c2);

    printf("The First Complex Number Is : ");
    writeComplex(c1);

    printf("The Second Complex Number Is : ");
    writeComplex(c2);

    printf("\n");
    printf("The Sum Of Given Complex Numbers Is : ");
    writeComplex(sum);

    printf("The Difference Of Given Complex Numbers Is : ");
    writeComplex(diff);

    return 0;
}