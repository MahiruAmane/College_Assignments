# Write a Python Program To Calculate Simple Interest.

principal = float(input("Please Enter The Principal Amount : "))
rate = float(input("Please Enter The Rate Of Interest : "))
time = float(input("Please Enter The Time (In Years) : "))

simple_interest = (principal * rate * time) / 100
print("The Simple Interest Is : {:.2f} ".format(simple_interest))