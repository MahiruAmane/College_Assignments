# Write a Python Program To Input 2 Sets Of Fruits & Perform All The Set Operations.

fruits1 = set(input("Please Enter The First Set Of Fruits : ").split(" "))
fruits2 = set(input("Please Enter The Second Set Of Fruits : ").split(" "))

print("Fruits Present In Either Set : {}".format(fruits1.union(fruits2)))
print("Fruits Only In The First Set But Not In The Second : {}".format(fruits1.difference(fruits2)))
print("Fruits Only In The Second Set But Not In The First : {}".format(fruits2.difference(fruits1)))

print("Fruits Present In Both Sets : {}".format(fruits1.intersection(fruits2)))
print("Fruits Present In Either Set But Not In Both : {}".format(fruits1.symmetric_difference(fruits2)))

print("Total Number Of Fruits In Both Sets Are : {}".format(len(fruits1.union(fruits2))))