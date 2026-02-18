# Write a Python Function To Print Fibonacci Series Using Recursion.

def fibonacci(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    else:
        fib_series = fibonacci(n - 1)
        fib_series.append(fib_series[-1] + fib_series[-2])
        return fib_series
    
n = int(input("Please Enter The Number Of Terms In Fibonacci Series : "))
print("Fibonacci Series : {}".format(fibonacci(n)))