# Write a Python Program To Create a NumPy Array To Find Sum Of All Elements In An Array.

import numpy as np

print("Enter The Numbers To Create An Array : ", end="")
num = [int(i) for i in input().split()]

arr = np.array(num)
total_sum = np.sum(arr)
print("The Sum Of All Elements In The Array Is :", total_sum)