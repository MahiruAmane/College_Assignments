# Write a Python Program To Swap Two Numbers Without Taking Additional Variable.

a = int(input("Please Enter The First Number : "))
b = int(input("Please Enter The Second Number : "))

a = a + b
b = a - b
a = a - b

print("After Swapping First Number Is : ", a)
print("After Swapping Second Number Is : ", b)