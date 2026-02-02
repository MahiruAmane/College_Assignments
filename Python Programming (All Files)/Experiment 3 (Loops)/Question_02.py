# Write a Python Program To Check Whether The Given Number Is An Armstrong Number Or Not.

a = int(input("Please Enter a Number : "))

count = len(str(a))
sum = 0 
orinal = a

while a > 0:
    digit = a % 10
    sum += digit ** count
    a = a // 10

if orinal == sum:
    print(orinal, "Is An Armstrong Number")
else:
    print(orinal, "Is Not An Armstrong Number")