# Write a Python Program To Take Different Data Types & Print Values Using Print Function.

integer_value = int(input("Please Enter An Integer Value : "))
float_value = float(input("Please Enter A Float Value : "))
string_value = input("Please Enter A String : ")
boolean_value = input("Please Enter A Boolean Value (True/False) : ")

print("Integer Value : ", integer_value)
print("Float Value : {:.2f} ".format(float_value))
print("String Value : ", string_value)
print("Boolean Value : ", boolean_value)