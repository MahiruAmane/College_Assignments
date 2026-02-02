# Write a Python Program To Print The Sum Of The Following Series (1+ ½ + 1/3 + 1/4 ... N Terms).

n = int(input("Please Enter The Number Of Terms : "))

sum = 0
for i in range(1, n + 1):
    sum = sum + 1 / i
print("The Sum Of The Series Up To {} Terms Is : {:.3f}".format(n, sum))