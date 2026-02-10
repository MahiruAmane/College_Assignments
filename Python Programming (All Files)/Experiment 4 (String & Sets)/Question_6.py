# Write a Python Program To Count Number Of Unique Words In a Given Sentence Using Sets.

value = input("Please Enter a String : ")
unique_words = set(value.split(" ", -1))
print("Total Number Of Unique Words In The Given String Are : {}".format(len(unique_words)))