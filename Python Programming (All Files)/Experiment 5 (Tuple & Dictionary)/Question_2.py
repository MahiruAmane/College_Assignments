# Write a Python Program To Create a Tuple & Store N Numeric Values & Find Average Of All Values.

tup = ()
n = int(input("Please Enter The Number Of Values To Be Stored In Tuple : "))

for i in range(n):
    val = int(input("Please Enter The {} Number : ".format(i+1)))
    tup += (val,)

print("The Given Tuple Is : ", tup)
sum_val = sum(tup)
avg = sum_val / len(tup)
print("The Average Of All Values In The Tuple Is : {:.2f}".format(avg))