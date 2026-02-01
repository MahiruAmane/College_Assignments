# Write a Python Program To Find Left Shift & Right Shift Values Of a Given Number.

a = int(input("Please Enter a Number : "))
x = int(input("Please Enter The Number Of Bits You Want To Shift : "))

left_shift = a << x
right_shift = a >> x

print("Left Shifted Value Of {} Is : ".format(a), left_shift)
print("Right Shifted Value Of {} Is : ".format(a), right_shift)