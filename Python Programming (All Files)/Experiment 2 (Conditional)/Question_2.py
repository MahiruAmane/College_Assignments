# Write a Python Program To Check Whether a Given Number Is Multiple Of Five Or Not.

a = int(input("Please Enter a Number : "))
b = a // 5

if a % 5 == 0:
    print(f"{a} Is The {b} Multiple Of 5")
else:
    print(f"{a} Is Not a Multiple Of 5")