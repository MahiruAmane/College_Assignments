# Write a Python Program To Take Any Date As Input & Display Next Date Of The Calendar.

day = int(input("Please Enter a Day : "))
month = int(input("Please Enter a Month : "))
year = int(input("Please Enter a Year : "))
print(f"You Entered The Date As : {day}/{month}/{year}")

is_leap = (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

month_days = [31, 29 if is_leap else 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]    

if day < month_days[month - 1]:
    day += 1
else:
    day = 1
    if month == 12:
        month = 1
        year += 1
    else:
        month += 1
print(f"The Next Date Is : {day}/{month}/{year}")