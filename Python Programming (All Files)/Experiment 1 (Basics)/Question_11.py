# Write a Python Program To Print Truth Table For Bitwise Operators.

print("Truth Table For 'AND' Operators")
print("{} & {} = ".format(0, 0), 0 & 0)
print("{} & {} = ".format(0, 1), 0 & 1)
print("{} & {} = ".format(1, 0), 1 & 0)
print("{} & {} = ".format(1, 1), 1 & 1)
print()

print("Truth Table For 'OR' Operators")
print("{} | {} = ".format(0, 0), 0 | 0)
print("{} | {} = ".format(0, 1), 0 | 1)
print("{} | {} = ".format(1, 0), 1 | 0)
print("{} | {} = ".format(1, 1), 1 | 1)
print()

print("Truth Table For 'XOR' Operators")
print("{} ^ {} = ".format(0, 0), 0 ^ 0)
print("{} ^ {} = ".format(0, 1), 0 ^ 1)
print("{} ^ {} = ".format(1, 0), 1 ^ 0)
print("{} ^ {} = ".format(1, 1), 1 ^ 1)