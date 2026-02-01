# Write a Python Program To Check Whether The Quadratic Equation Has Real Roots Or Imaginary Roots.

import math

a = int(input("Please Enter The Coefficient Of X² : "))
b = int(input("Please Enter The Coefficient Of X : "))
c = int(input("Please Enter The Constant c : "))

discriminant = b**2 - 4*a*c

if discriminant > 0:
    print("The Quadratic Equation Has Two Real And Distinct Roots")
    root1 = (-b + discriminant**0.5) / (2*a)
    root2 = (-b - discriminant**0.5) / (2*a)
    print("The Roots Are : {:.2f} And {:.2f}".format(root1, root2))
elif discriminant == 0:
    print("The Quadratic Equation Has Two Real And Equal Roots")
    root = -b / (2*a)
    print("The Root Is : {:.2f}".format(root))
else:
    print("The Quadratic Equation Has Imaginary Roots")
    real_part = -b / (2*a)
    imaginary_part = (abs(discriminant)**0.5) / (2*a)
    print("The Roots Are : {:.2f} + {:.2f}i And {:.2f} - {:.2f}i".format(real_part, imaginary_part, real_part, imaginary_part))