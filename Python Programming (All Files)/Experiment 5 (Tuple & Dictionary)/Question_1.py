# Write a Python Program To Scan N Values In Range Of 0 To 3 & Print The Number Of Times Each Value Has Occurred.

n = int(input("Please Enter The Number Of Values : "))
count = {}

for i in range(n):

    num = int(input("Please Enter A Value Between 0 To 3 : "))
    if num < 0 or num > 3:
        print("Invalid Input Please Enter A Value Between 0 To 3")
        continue
    elif num in count:
        count[num] += 1
    else:
        count[num] = 1

for key, value in count.items():
    print("Value {} Has Occurred {} Times".format(key, value))