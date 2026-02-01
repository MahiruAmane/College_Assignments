# Write a Python Program To Find The Greatest Among The Two Numbers.

a = int(input("Please Enter The First Number : "))
b = int(input("Please Enter The Second Number : "))

if a == b:
    print("Both Numbers Are Equal")
elif a > b:
    print(f"{a} Is Greater Than {b}")
else:
    print(f"{b} Is Greater Than {a}")