# Write a Python Program To Check Whether The Given Number Is Divisible By 3 & 5 Both.

num = int(input("Please Enter a Number : "))

if num % 3 == 0 and num % 5 == 0:
    print("{} Is Divisible By Both 3 & 5".format(num))
else:
    print("{} Is Not Divisible By Both 3 & 5".format(num))