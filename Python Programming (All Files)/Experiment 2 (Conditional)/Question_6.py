# Write a Python Program To Find Whether a Given Year Is a Leap Year Or Not.

year = int(input("Please Enter a Year : "))

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(f"{year} Is a Leap Year")
else:
    print(f"{year} Is Not a Leap Year")