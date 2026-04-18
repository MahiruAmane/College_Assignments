# Write a Python Program To Input Two Values From The User Where The First Line Contains N, The Number Of Test Cases. The Next N Lines Contain The Space Separated Values Of a & b. Perform Integer Division And Print a/b. Handle Exception In Case Of ZeroDivisionError Or ValueError.

try:
    N = int(input("Enter The Number Of Test Cases : "))
    for i in range(N):
        a, b = map(int, input("Enter Two Space Separated Integers (a b) : ").split())
        result = a // b
        print(f"The Result Of {a} Divided By {b} Is : {result}")
except ValueError:
    print("Error : Invalid Input For Number Of Test Cases, Please Enter An Integer.")
except ZeroDivisionError:
    print("Error : Division By Zero Is Not Allowed.")