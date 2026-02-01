# Write a Python Program To Find The Greatest Among Three Numbers Assuming No Two Values Are Same.

a = int(input("Please Enter The First Number : "))
b = int(input("Please Enter The Second Number : "))
c = int(input("Please Enter The Third Number : "))

if (a > b) and (a > c):
    print(f"The First Number {a} is the Greatest Among The Three Numbers")
elif (b > a) and (b > c):
    print(f"The Second Number {b} is the Greatest Among The Three Numbers")
else:
    print(f"The Third Number {c} is the Greatest Among The Three Numbers")