# Write a Python Program To Add Constructor In The Above Class To Initialize Student Details Of N Students & Implement
# a) Display All Student Details
# b) Find Marks Percentages Of Each Student
# c) Display Result Of Each Student (Pass/Fail) Based On Marks (Pass If Marks Are Greater Than 40 In All Subjects)
# d) Write a Function To Find Average Of The Class.

class Student:
    def __init__(self, name, sap_id, marks):
        self.name = name
        self.sap_id = sap_id
        self.marks = marks 

    def display(self):
        print(f"Name : {self.name}")
        print(f"SAP ID : {self.sap_id}")
        print(f"Physics : {self.marks[0]}")
        print(f"Chemistry : {self.marks[1]}")
        print(f"Mathematics : {self.marks[2]}")

    def marks_percentage(self):
        total_marks = sum(self.marks)
        percentage = total_marks / len(self.marks)
        return percentage

    def display_result(self):
        if all(mark > 40 for mark in self.marks):
            print("Result : Pass")
        else:
            print("Result : Fail")


def class_average(student_list):
    if not student_list:
        return 0
    total_class_percentage = sum(student.marks_percentage() for student in student_list)
    return total_class_percentage / len(student_list)


students = []
n = int(input("Enter The Number Of Students : "))

for i in range(n):
    print(f"\nEnter Details For Student {i + 1} :")
    name = input("Enter Student's Name : ")
    sap_id = input("Enter Student's SAP ID : ")
    
    marks = []
    marks.append(float(input("Enter Marks For Physics (Out Of 100) : ")))
    marks.append(float(input("Enter Marks For Chemistry (Out Of 100) : ")))
    marks.append(float(input("Enter Marks For Mathematics (Out Of 100) : ")))
    
    student = Student(name, sap_id, marks)
    students.append(student)

print("\n")
print("Details Of All Students : \n")
for student in students:
    student.display()
    print(f"Percentage : {student.marks_percentage():.2f} %")
    student.display_result()
    print("-" * 30)

avg = class_average(students)
print(f"Overall Average Percentage of the Class : {avg:.2f} %")