# Write a Python Program To Input Two Values From The User Where The First Line Contains N, The Number Of Test Cases. 
# The Next N Lines Contain The Space Separated Values Of a & b. Perform Integer Division And Print The Result. 
# Handle Exception In Case Of Zero Division Error Or Value Error.

try:
    n = int(input("Enter The Number Of Test Cases : "))
    for i in range(n):
        a, b = map(int, input("Enter Two Space Separated Integers (a b) : ").split())
        result = a // b
        print(f"The Result Of {a} Divided By {b} Is : {result}")
except ValueError:
    print("Error : Invalid Input For Number Of Test Cases, Please Enter An Integer.")
except ZeroDivisionError:
    print("Error : Division By Zero Is Not Allowed.")