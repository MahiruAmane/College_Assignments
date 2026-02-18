# Write a Python Functions To Explain Keywords Arguments, Default Arguments & Variable Length Arguments.

# Keyword Arguments
def greet(name, message):
    print(f"{message}, {name}!")
greet(name = "Alice", message = "Hello")

# Default Arguments
def greet(name, message = "Hello"):
    print(f"{message}, {name}!")
greet("Haruto") 
greet("Anos", "Welcome") 

# Variable Length Arguments
def greet(*names):
    for name in names:
        print(f"Hello, {name}!")
greet("Aishia", "Akari")