# Write a Python Program To Find Factorial Of a Given Number.

n = int(input("Please Enter a Number To Find It's Factorial : "))

factorial = 1

for i in range(1, n + 1, 1):
    factorial = factorial * i

print("Factorial Of Given Number {} Is : {}".format(n, factorial))