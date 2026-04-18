# Write a Python Program To Design a GUI Based Basic Calculator For Performing Basic Arithmetic Operations.

import tkinter as tk
import tkinter.messagebox as messagebox

def add():
    if not entry1.get() or not entry2.get():
        messagebox.showerror("Error", "All Fields Are Required!")
        return
    num1 = float(entry1.get())
    num2 = float(entry2.get())
    result = num1 + num2
    label_result.config(text="Result - " + str(result))

def subtract():
    if not entry1.get() or not entry2.get():
        messagebox.showerror("Error", "All Fields Are Required!")
        return
    num1 = float(entry1.get())
    num2 = float(entry2.get())
    result = num1 - num2
    label_result.config(text="Result - " + str(result))

def multiply():
    if not entry1.get() or not entry2.get():
        messagebox.showerror("Error", "All Fields Are Required!")
        return
    num1 = float(entry1.get())
    num2 = float(entry2.get())
    result = num1 * num2
    label_result.config(text="Result - " + str(result))

def divide():
    if not entry1.get() or not entry2.get():
        messagebox.showerror("Error", "All Fields Are Required!")
        return
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        result = num1 / num2
        label_result.config(text="Result - " + str(result))
    except ZeroDivisionError:
        label_result.config(text="Error : Division By Zero Is Not Defined")

def clear():
    entry1.delete(0, tk.END)
    entry2.delete(0, tk.END)
    label_result.config(text="Result - ")

root = tk.Tk()
root.title("Basic Calculator")
root.geometry("1280x720")

calc_frame = tk.Frame(root)
calc_frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

for i in range(5):
    calc_frame.columnconfigure(i, weight=1, uniform="equal")

label1 = tk.Label(calc_frame, text="Enter First Number", bg="lightgray")
label1.grid(row=0, column=0, columnspan=2, padx=10, pady=10)
entry1 = tk.Entry(calc_frame)
entry1.grid(row=0, column=2, columnspan=3, padx=10, pady=10)

label2 = tk.Label(calc_frame, text="Enter Second Number", bg="lightgray")
label2.grid(row=1, column=0, columnspan=2, padx=10, pady=10)
entry2 = tk.Entry(calc_frame)
entry2.grid(row=1, column=2, columnspan=3, padx=10, pady=10)

button_add = tk.Button(calc_frame, text="Add", command=add, fg="green")
button_add.grid(row=3, column=0, padx=10, pady=10, sticky="ew")

button_subtract = tk.Button(calc_frame, text="Subtract", command=subtract, fg="green")
button_subtract.grid(row=3, column=1, padx=10, pady=10, sticky="ew")

button_multiply = tk.Button(calc_frame, text="Multiply", command=multiply, fg="green")
button_multiply.grid(row=3, column=2, padx=10, pady=10, sticky="ew")

button_divide = tk.Button(calc_frame, text="Divide", command=divide, fg="green")
button_divide.grid(row=3, column=3, padx=10, pady=10, sticky="ew")

button_clear = tk.Button(calc_frame, text="Clear", command=clear, fg="red")
button_clear.grid(row=3, column=4, padx=10, pady=10, sticky="ew")

label_result = tk.Label(calc_frame, text="Result - ", bg="lightgray")
label_result.grid(row=4, column=0, columnspan=5, padx=10, pady=10)

root.mainloop()