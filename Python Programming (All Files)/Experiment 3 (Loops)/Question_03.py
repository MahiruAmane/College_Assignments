# Write a Python Program To Print Fibonacci Series.

n = int(input("Please Enter The Number Of Terms In Fibonacci Series : "))

a = 0
b = 1

print("Fibonacci Series Upto {} Terms Is : ".format(n))
for i in range(n):
    print(a, end = ' ')
    c = a + b
    a = b
    b = c