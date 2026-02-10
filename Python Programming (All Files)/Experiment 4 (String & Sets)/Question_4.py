# Write a Python Program To Input a String And a Sub-String, Print The Number Of Occurrences Of The Sub-String In The String Traversing From Left To Right.

value1 = input("Please Enter a String : ")
value2 = input("Please Enter a Sub-String : ")
count = 0

for i in value1.split(" ", -1):
    if i == value2:
        count += 1

print("Total Occurrences of '{}' Are : {}".format(value2, count))