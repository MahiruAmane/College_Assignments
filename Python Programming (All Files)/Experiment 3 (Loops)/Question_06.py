# Write a Python Program To Print Sum Of Digits.

a = int(input("Please Enter a Number : "))

original = a
sum = 0

while a > 0:
    digit = a % 10
    sum = sum + digit
    a = a // 10

print("Sum Of Digits Of The Number {} Is : ".format(original), sum)