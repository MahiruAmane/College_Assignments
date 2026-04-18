# Write a Python Program To Create a Class of Student Also Make,
# Objects By Taking Inputs From The User & Display Details Of All Students.

class Student:
    def __init__(self, name, sap_id, marks):
        self.name = name
        self.sap_id = sap_id
        self.marks = marks

    def display_details(self):
        print(f"Name: {self.name}")
        print(f"SAP ID: {self.sap_id}")
        print(f"Physics: {self.marks[0]}")
        print(f"Chemistry: {self.marks[1]}")
        print(f"Mathematics: {self.marks[2]}")

students = []
n = int(input("Enter The Number Of Students : "))

for i in range(n):
    name = input("Enter Student's Name : ")
    sap_id = input("Enter Student's SAP ID : ")
    marks = []
    marks.append(float(input("Enter Marks For Physics : ")))
    marks.append(float(input("Enter Marks For Chemistry : ")))
    marks.append(float(input("Enter Marks For Mathematics : ")))
    
    student = Student(name, sap_id, marks)
    students.append(student)
    print("\n")

print("Details Of All Students :")
for student in students:
    student.display_details()
    print()