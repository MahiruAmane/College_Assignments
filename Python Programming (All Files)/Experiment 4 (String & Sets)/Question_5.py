# Write a Python Program To Count The Number Of Occurrences Of Each Alphabet In A Given String.

value = input("Please Enter a String : ")
count_lower = {}
count_upper = {}
spaces = 0

for i in value:
    if i.islower():
        if i in count_lower:
            count_lower[i] += 1
        else:
            count_lower[i] = 1
    elif i.isupper():
        if i in count_upper:
            count_upper[i] += 1
        else:
            count_upper[i] = 1
    elif i.isspace():
        spaces += 1

for key, value in count_lower.items():
    print("Total Occurrences of '{}' Are : {}".format(key, value))

for key, value in count_upper.items():
    print("Total Occurrences of '{}' Are : {}".format(key, value))

print("Total Occurrences of Space Are : {}".format(spaces))