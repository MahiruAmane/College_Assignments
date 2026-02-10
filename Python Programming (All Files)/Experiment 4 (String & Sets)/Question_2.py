# Write a Python Program To Count The Number Of Vowels In A String.

value = input("Please Enter a String : ")
count = 0

for i in value:
    if i in "AEIOUaeiou":
        count += 1
        print("{} Vowel Found : {}".format(count, i))
        
print("The Number Of Vowels In The String Are : ", count)