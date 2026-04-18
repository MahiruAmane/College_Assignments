# Write a Python Program To Input Integers In A File & Find The Maximum Number, Average Of All Numbers & Count All Numbers Greater Than 100.

print("Please Enter The Integers (Separate By Space) : ", end = "")
numbers = [int(i) for i in input().split()]

with open("numbers.txt", "w") as file:
    for number in numbers:
        file.write(str(number) + "\n")

with open("numbers.txt", "r") as file:
    
    num = file.read().splitlines()
    num = [int(i) for i in num]
    max_num = max(num)
    avg_num = sum(num) / len(num)
    count_greater_100 = len([i for i in num if i > 100])

print(f"Maximum Number : {max_num}")
print(f"Average Of All Numbers : {avg_num}")
print(f"Count Of All Numbers Greater Than 100 : {count_greater_100}")