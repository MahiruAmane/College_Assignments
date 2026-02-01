# Write a Python Program To Print The Grade Sheet Of a Student For The Given Range Of CGPA.

name = input("Please Enter The Student Name : ")
print()

physics = float(input("Please Enter The Marks Obtained In Physics : "))
chemistry = float(input("Please Enter The Marks Obtained In Chemistry : "))
maths = float(input("Please Enter The Marks Obtained In Mathematics : "))
python = float(input("Please Enter The Marks Obtained In Python : "))
english = float(input("Please Enter The Marks Obtained In English : "))
total_marks = physics + chemistry + maths + python + english
percentage = (total_marks / 500) * 100
cgpa = percentage / 9.5

if cgpa >= 9.0 and cgpa <= 10.0:
    grade = 'O'
elif cgpa >= 8.0 and cgpa < 9.0:
    grade = 'A+'
elif cgpa >= 7.0 and cgpa < 8.0:
    grade = 'A'
elif cgpa >= 6.0 and cgpa < 7.0:
    grade = 'B+'
elif cgpa >= 5.0 and cgpa < 6.0:
    grade = 'B'
elif cgpa >= 4.0 and cgpa < 5.0:
    grade = 'C'
else:
    grade = 'F'

print()
print("Student Name : ", name)
print("Total Marks : ", total_marks, "/ 500")
print("Percentage : {:.2f} %".format(percentage))
print("CGPA : {:.2f}".format(cgpa))
print("Grade Obtained :", grade)