# Write a Python Lambda Function To Find Volume Of Cone.

import math

cone_volume = lambda r, h : (1/3) * math.pi * r**2 * h

radius = float(input("Please Enter The Radius Of The Cone : "))
height = float(input("Please Enter The Height Of The Cone : "))
volume = cone_volume(radius, height)
print("The Volume Of The Cone Is : {:.2f}".format(volume))