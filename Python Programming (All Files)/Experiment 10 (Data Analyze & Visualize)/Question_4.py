# Write a Python Program To Use Pandas To Get The Powers Of An Array Values Element Wise.

import pandas as pd
import numpy as np


print("Enter The Numbers In The First Array : ", end="")
list1 = [int(i) for i in input().split()]

print("Enter The Numbers In The Second Array : ", end="")       
list2 = [int(i) for i in input().split()]

print("Enter The Numbers In The Third Array : ", end="")
list3 = [int(i) for i in input().split()]

if len(list1) == len(list2) == len(list3):
    lenmax = len(list1)
else:
    print("The Length Of The Arrays Are Not Same.")
    exit()

data = {'X': list1, 
        'Y': list2, 
        'Z': list3}

df = pd.DataFrame(data)

num = [i for i in range(0, lenmax)]
exponents = pd.array(num)

result = df.pow(exponents, axis=0)
print(result)