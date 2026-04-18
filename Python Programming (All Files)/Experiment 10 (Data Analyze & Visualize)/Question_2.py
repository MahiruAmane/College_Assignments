# Write a Python Program To Create NumPy Array Of 3X3 Dimension, 
# Now Find Sum Of All Rows & Columns Individually, Also Find Second Maximum Element In The Array.

import numpy as np

print("Enter The Numbers To Create A 3x3 Array (Only 9 Elements) : ", end="")
num = [int(i) for i in input().split()]

arr = np.array(num).reshape(3, 3)
row_sum = np.sum(arr, axis=1)
col_sum = np.sum(arr, axis=0)

unique_elements = np.unique(arr)
if len(unique_elements) >= 2:
    second_max = unique_elements[-2]
else:
    second_max = None

print("Sum Of All Rows : ", row_sum)
print("Sum Of All Columns : ", col_sum)
print("The Second Maximum Element In The Array Is : ", second_max)