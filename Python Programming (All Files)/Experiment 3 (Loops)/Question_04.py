# Write a Python Program To Find If Given Number Is a Prime Number Or Not.

import math

a = int (input("Please Enter a Number : "))

if a > 1:
    for i in range(2, int(math.sqrt(a)) + 1):
        if (a % i) == 0:
            print(f"{a} Is Not a Prime Number")
            break
    else:
        print(f"{a} Is a Prime Number")
else:
    print(f"{a} Is Not a Prime Number")