# Write a Python Program To Print The Multiplication Table Of A Given Number Using Loop.

a = int(input("Please Enter a Number To Print It's Multiplication Table : "))
n = int(input("Please Enter The Range Upto Which You Want The Multiplication Table : "))

for i in range(1, n + 1):
    print(f"{a} x {i} = {a * i}")