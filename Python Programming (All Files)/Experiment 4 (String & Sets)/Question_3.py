# Write a Python Program To Input a Sentence & Print Words In Separate Lines.

value = input("Please Enter a String : ")
count = 0

for i in value.split(" ", -1):
    count += 1
    print("{} Word In The Sentence Is : {}".format(count, i))

print("Total Words In The Sentence Are : ", count)