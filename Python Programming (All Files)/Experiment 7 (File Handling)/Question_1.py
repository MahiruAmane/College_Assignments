# Write a Python Program To Add a Few Names To a File & Count All The Names In That File, Names Starting With Vowel & Find The Longest Name In That File.

n = int(input("How Many Names Do You Want To Add To The File : "))
print("Please Enter The Names To Be Added To The File (Enter For Next Name ): ")
names = [input() for i in range(n)]
print(names)

with open("Names.txt", "w") as file:
    for name in names:
        file.write(name + "\n")

with open("Names.txt", "r") as file:
    names = file.read().splitlines()

    total_names = len(names)
    vowel_names = [name for name in names if name[0].upper() in "AEIOU"]
    longest_name = max(names, key=len)

print(f"Total Names : {total_names}")
print(f"Names Starting With Vowel : {len(vowel_names)}")
print(f"Longest Name : {longest_name}")