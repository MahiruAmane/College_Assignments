# Write a Python Program To Input 2 Sets Of Fruits & Perform Basic Set Operations.

fruits1 = set(input("Please Enter The First Set Of Fruits : ").split(" "))
fruits2 = set(input("Please Enter The Second Set Of Fruits : ").split(" "))

print("Fruits Present In Either Set : {}".format(fruits1.union(fruits2)))
print("Fruits Only In The First Set But Not In The Second : {}".format(fruits1.difference(fruits2)))

print("Total Number Of Fruits In Both Sets Are : {}".format(len(fruits1.union(fruits2))))