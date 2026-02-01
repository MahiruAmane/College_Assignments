# Write a Python Program To Find Sum Of First N Natural Numbers.

n = int(input("Please Enter a Number (To Get Sum Of First N Natural Numbers) : "))

sum = n * (n + 1) // 2
print("Sum of First {} Natural Numbers Is : {}".format(n, sum))