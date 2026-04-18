# Write a Python Program To Perform Matrix Multiplication Of Any 2 N x N Matrices.

import numpy as np

print("Enter The Size Of The Square Matrices (N x N) : ", end = "")
n = int(input())

print("Enter The Elements Of The First Matrix (Only {} Elements) : ".format(n*n), end = "")
num1 = [int(i) for i in input().split()]

print("Enter The Elements Of The Second Matrix (Only {} Elements) : ".format(n*n), end = "")
num2 = [int(i) for i in input().split()]

matrix1 = np.array(num1).reshape(n, n)
matrix2 = np.array(num2).reshape(n, n)
result = np.dot(matrix1, matrix2)

print("Result Of Matrix Multiplication : ")
print(result)