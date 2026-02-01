# Write a Python Program To Find Area Of Triangle When Length Of Sides Are Given.

side1 = float(input("Please Enter Length Of The First Side : "))
side2 = float(input("Please Enter Length Of The Second Side : "))
side3 = float(input("Please Enter Length Of The Third Side : "))

s = (side1 + side2 + side3) / 2

area = (s * (s - side1) * (s - side2) * (s - side3)) ** 0.5

print("The Area Of The Triangle Is : {:.2f}".format(area))