# Write a Python Program To Create a Dictionary Of N Persons Where Key Is Name & Value Is City.

value = {}
n = int(input("Please Enter The Number Of Persons : "))

for i in range(n):
    name = input("Please Enter The {} Student Name : ".format(i+1))
    city = input("Please Enter The {} Student City : ".format(i+1))
    value[name] = city

print("Names Of All Students : ", list(value.keys()))
print("City Of All Students : ", list(value.values()))
print("Name & City Of All Students : ", value)

city_count = {}

for city in value.values():
    if city in city_count:
        city_count[city] += 1
    else:
        city_count[city] = 1
print("Number Of Students In Each City : ", city_count)