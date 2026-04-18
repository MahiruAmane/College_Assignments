# Write a Python Program To Create Programs To Implement Different Types Of Inheritances.

class Parent:
    def parent_method(self):
        print("This Is The Parent Method.")

class Child(Parent):
    def child_method(self):
        print("This Is The Child Method.")



class Grandparent:
    def grandparent_method(self):
        print("This Is The Grandparent Method.")

class Parent(Grandparent):
    def parent_method(self):
        print("This Is The Parent Method.")

class Child(Parent):
    def child_method(self):
        print("This Is The Child Method.")



class Parent:
    def parent_method(self):
        print("This Is The Parent Method.")

class Child1(Parent):
    def child1_method(self):
        print("This Is The First Child Method.")

class Child2(Parent):
    def child2_method(self):
        print("This Is The Second Child Method.")



class Father:
    def father_method(self):
        print("This Is The Father Method.")

class Mother:
    def mother_method(self):
        print("This Is The Mother Method.")

class Child(Father, Mother):
    def child_method(self):
        print("This Is The Child Method.")



class Animal:
    def animal_method(self):
        print("This Is The Animal Method (Base Class).")

class Mammal(Animal):
    def mammal_method(self):
        print("This Is The Mammal Method.")

class Bird(Animal):
    def bird_method(self):
        print("This Is The Bird Method.")

class Bat(Mammal, Bird):
    def bat_method(self):
        print("This Is The Bat Method.")