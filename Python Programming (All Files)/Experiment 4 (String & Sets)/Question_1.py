# Write a Python Program To Count & Display The Number Of Capital Letters In a String.

value = input("Please Enter a String : ")
count = 0

for i in value:
    if i.isupper():
        count += 1
        print("{} Capital Letter Found : {}".format(count, i))

print("The Number Of Capital Letters In The String Are : ", count)