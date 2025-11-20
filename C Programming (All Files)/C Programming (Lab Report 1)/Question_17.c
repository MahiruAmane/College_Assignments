// Write a C Program To Print All Ramanujan Numbers Up To a Reasonable Limit. A Ramanujan Number Is The Smallest Number That Can Be Expressed As The Sum Of Two Cubes In Two Different Ways.

#include <stdio.h>
#include <math.h>

int main() {

    int num;
    int sum1;
    int sum2;
    int cube;
    int count = 0;
    int arr[128];

    printf("Please Enter a Number To Search For Possible Ramanujan Numbers : ");
    scanf("%d", &num);

    cube = cbrt(num);

    for (int i = 1; i <= cube; i++)
    {
        for (int j = i; j <= cube; j++) 
        {
            sum1 = (i * i * i) + (j * j * j);

            if (sum1 > num)
            {
                break;
            }

            for (int k = i; k <= cube; k++) 
            {
                for (int l = k; l <= cube; l++) 
                {
                    sum2 = (k * k * k) + (l * l * l);
                    
                    if ((i == k && j == l) || (i == l && j == k))
                    {
                        continue;
                    }

                    if (sum1 == sum2) 
                    {
                        arr[count] = sum1;
                        count = count + 1;
                    }
                }
            }
        }
    }

    for (int i = 0; i < count; i++) 
    {
        for (int j = 0; j < count - 1; j++) 
        {
            if (arr[j] > arr[j + 1]) 
            {
                int temp = arr[j];
                arr[j] = arr[j + 1];
                arr[j + 1] = temp;
            }
        }
    }

    for (int i = 0; i < count; i++)
    {
        printf("%d \n", arr[i]);
    }

    if (count > 0)
    {
        printf("Total Ramanujan Numbers Found Are : %d", count);
    }
    else
    {
        printf("No Ramanujan Number Was Found Within The Specified Range");
    }

    return 0;
}