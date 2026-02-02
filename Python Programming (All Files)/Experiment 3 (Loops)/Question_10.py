# Write a Python Program To Print The Following Pattern.

n = int(input("Please Enter The Number Of Rows : "))

for i in range(n, 0, -1):

    for j in range(1, i + 1):
        print(j, end = "")

    for k in range(n - i - 1):
        print(" ", end = "")

    for k in range(n - i):
        print(" *", end = "")

    for k in range(n - i - 1):
        print(" ", end = "")
    if i == n:
        for l in range(i - 1, 0, -1):
            print(l, end = "")
    else:
        for l in range(i, 0, -1):
            print(l, end = "")
    
    print()