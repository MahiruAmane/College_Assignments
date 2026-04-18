# Write a Python Program To Create a Counter To Show That How Many Times The Program Is Executed.

counter = 0
try:
    with open("counter.txt", "r") as file:
        counter = int(file.read())
except FileNotFoundError:
    pass
counter += 1

with open("counter.txt", "w") as file:
    file.write(str(counter))

print(f"This Program Has Been Executed {counter} Times.")