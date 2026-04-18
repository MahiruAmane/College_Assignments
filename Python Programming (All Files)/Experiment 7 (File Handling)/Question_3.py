# Write a Python Program To Input City Name, Population & Area For 5 Cities And Store The Data In A File. Display Details Of All The Cities, Display City Names With More Than 1 Million Population & Display Sum Of Area Of All The Cities.

n = int(input("Please Enter The Number Of Tasks You Want To Add : "))
info = []

for i in range(n):
    city_name = input("Please Enter The City Name : ")
    population = int(input("Please Enter The Population : "))
    area = float(input("Please Enter The Area : "))
    info.append((city_name, population, area))

with open("cities.txt", "w") as file:
    for city in info:
        file.write(f"{city[0]},{city[1]},{city[2]}\n")

with open("cities.txt", "r") as file:
    print("Details Of All The Cities :")
    for line in file:
        city_data = line.strip().split(",")
        print(f"City Name : {city_data[0]}, Population : {city_data[1]}, Area : {city_data[2]}")

with open("cities.txt", "r") as file:
    print("City Names With More Than 1 Million Population : ")
    for line in file:
        city_data = line.strip().split(",")
        if int(city_data[1]) > 1000000:
            print(city_data[0])

with open("cities.txt", "r") as file:
    total_area = 0
    for line in file:
        city_data = line.strip().split(",")
        total_area += float(city_data[2])
    print(f"Sum Of Area Of All The Cities : {total_area}")