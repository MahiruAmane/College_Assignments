# Write a Python Function To Print 1 To N Using Recursion (Note - Do Not Use Loop).

def print_numbers(n):
    
    if n == 0:
        return
    print_numbers(n - 1)
    print(n)

n = int(input("Please Enter a Number To Display From 1 To N : "))
if n < 1:
    print("Please Enter a Positive Integer")
else:
    print_numbers(n)