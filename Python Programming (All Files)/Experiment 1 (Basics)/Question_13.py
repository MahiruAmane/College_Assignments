# Write a Python Program To Use Membership Operators To Find Whether A Given Number Is Present In A List Or Not.

list = [10, 20, 30, 40, 50]

print("Given List Is : ", list)
num = int(input("Enter A Number To Check It's Presence In The List : "))

print(num in list)
print(num not in list)