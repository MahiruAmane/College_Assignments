# Write a Python Program To Design a GUI For Student Registration For a Course & Store These Details In a Database. 
# Use Tkinter For UI, SQLite For Database Storage.

import sqlite3
import tkinter as tk
import tkinter.messagebox as messagebox

conn = sqlite3.connect('student_registration.db')
cursor = conn.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS students 
               (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    age INTEGER NOT NULL,
                    course TEXT NOT NULL
                )''')
conn.commit()
conn.close()

def register_student():

    name = entry_name.get()
    age = entry_age.get()
    course = entry_course.get()

    if not name or not age or not course:
        messagebox.showerror("Error", "All Fields Are Required!")
        return
    try:
        age = int(age)
    except ValueError:
        messagebox.showerror("Error", "Age Must Be a Number!")
        return
    if age < 18 or age > 25:
        messagebox.showerror("Error", "Age Must Be Between 18 & 25!")
        return
    conn = sqlite3.connect('student_registration.db')

    cursor = conn.cursor()
    cursor.execute("INSERT INTO students (name, age, course) VALUES (?, ?, ?)", (name, age, course))
    conn.commit()
    conn.close()
    messagebox.showinfo("Success", "Student Registered Successfully!")

def clear_fields():
    entry_name.delete(0, tk.END)
    entry_age.delete(0, tk.END)
    entry_course.delete(0, tk.END)

root = tk.Tk()
root.title("Student Registration")
root.geometry("1280x720")

calc_frame = tk.Frame(root)
calc_frame.place(relx=0.6, rely=0.5, anchor=tk.CENTER)

for i in range(4):
    calc_frame.columnconfigure(i, weight=1, uniform="equal")

label_name = tk.Label(calc_frame, text="Name Of Student", bg="lightgray")
label_name.grid(row=0, column=0, padx=10, pady=10)
entry_name = tk.Entry(calc_frame)
entry_name.grid(row=0, column=1, padx=10, pady=10)

label_age = tk.Label(calc_frame, text="Age Of Student", bg="lightgray")
label_age.grid(row=1, column=0, padx=10, pady=10)
entry_age = tk.Entry(calc_frame)
entry_age.grid(row=1, column=1, padx=10, pady=10)

label_course = tk.Label(calc_frame, text="Course Of Student", bg="lightgray")
label_course.grid(row=2, column=0, padx=10, pady=10)
entry_course = tk.Entry(calc_frame)
entry_course.grid(row=2, column=1, padx=10, pady=10)

register_button = tk.Button(calc_frame, text="Register", command=register_student, fg="green")
register_button.grid(row=3, column=0, padx=10, pady=10)

clear_button = tk.Button(calc_frame, text="Clear", command=clear_fields, fg="red")
clear_button.grid(row=3, column=1, padx=10, pady=10)

root.mainloop()
conn.close()