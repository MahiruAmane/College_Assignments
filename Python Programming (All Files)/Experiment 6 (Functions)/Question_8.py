# Write a Python Lambda Function To Check Whether All The Values In a Dictionary Are Same Or Not.

check_values = lambda d : len(set(d.values())) == 1

n = int(input("Please Enter The Number Of Key Value Pairs You Want To Add To The Dictionary : "))
empty = {}

for i in range(n):
    key = input("Please Enter The Key Of The {} Key Value Pair : ".format(i+1))
    value = input("Please Enter The Value Of The {} Key Value Pair : ".format(i+1))
    empty[key] = value

if n > 0 and check_values(empty):
    print("All The Values In The Dictionary Are Same")
elif n == 0:
    print("The Dictionary Is Empty")
else:
    print("All The Values In The Dictionary Are Not Same")