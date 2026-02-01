# Write a Python Program To Compute The Length Of The Hypotenuse Of a Right Triangle Using Pythagora's Theorem.

import math

side1 = float(input("Please Enter Length Of The First Side : "))
side2 = float(input("Please Enter Length Of The Second Side : "))

hypotenuse = math.sqrt(side1**2 + side2**2)
print("The Length Of The Hypotenuse Is : {:.2f}".format(hypotenuse))