# Write a Python Program To Create a Class To Implement Method Overriding.

class Parent:
    def display(self):
        print("This Is The Parent Class.")

class Child(Parent):
    def display(self):
        print("This Is The Child Class.")

child_instance = Child()
child_instance.display()

parent_instance = Parent()
parent_instance.display()