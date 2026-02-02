# Write a Python Program To Count & Print All Numbers Divisible By 5 Or 7 Between 1 To 100.

n = int(input("Please Enter The Upper Limit For Counting Divisible Numbers : "))
count = 0

for i in range(1, n + 1):
    if i % 5 == 0:
        print("{} Is Divisible By 5".format(i))
        count += 1
    elif i % 7 == 0:
        print("{} Is Divisible By 7".format(i))
        count += 1
        
print("Total Count Of Numbers Divisible By 5 Or 7 Between 1 To {} Is : {}".format(n, count))