# Write a Python Program To Check Whether a Given Number Is Palindrome Or Not.

a = int(input("Please Enter a Number : "))

orinal = a
rev = 0

while a > 0:
    digit = a % 10
    rev = rev * 10 + digit
    a = a // 10

if orinal == rev:
    print(orinal, "Is A Palindrome Number")
else:
    print(orinal, "Is Not A Palindrome Number")