# Write a Python Program To Store Details Of N Movies In a Dictionary By Taking Input From The User.

n = int(input("Please Enter The Number Of Movies : "))
movies = {}

print()
for i in range(n):
    name = input("Please Enter The {} Movie Name : ".format(i+1))
    year = int(input("Please Enter The Year Of Release : "))
    director = input("Please Enter The Director Name : ")
    cost = float(input("Please Enter The Production Cost (In Crore's) : "))
    profit = float(input("Please Enter The Collection Made (In Crore's) : "))

    movies[name] = {"Year Of Release" : year, "Director's Name" : director, "Production Cost" : cost, "Collection Made" : profit}
    print()

print("All Movie Details Are As Follows : ")

for i in movies:
    print("Movie Name : {}".format(i))
    for key, value in movies[i].items():
        print("{} : {}".format(key, value))
    print()

print("Movies Released Before 2015 Are As Follows : ")

for i in movies:
    if movies[i]["Year Of Release"] < 2015:
        print(i)
print()
print("Movies That Made A Profit Are As Follows : ")

for i in movies:
    if movies[i]["Collection Made"] > movies[i]["Production Cost"]:
        print(i)
print()
director_name = input("Please Enter The Director Name To Find Movies Directed By Him/Her : ")
print("Movies Directed By {} Are As Follows : ".format(director_name))

for i in movies:
    if movies[i]["Director's Name"] == director_name:
        print(i)