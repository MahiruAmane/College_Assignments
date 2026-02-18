# Write a Python Function That Takes a Positive Integer & Returns The Sum Of The Cube Of All The Positive Integers Smaller Than The Specified Number.

def sum_of_cubes(n):

    if n <= 0:
        print("A Positive Integer Is Required")
        return None
    
    total = 0
    for i in range(1, n):
        total += i ** 3
    
    return total

n = int(input("Please Enter a Positive Integer : "))
result = sum_of_cubes(n)
print(f"The Sum Of The Cubes Of All Positive Integers Smaller Than {n} Is : {result}")