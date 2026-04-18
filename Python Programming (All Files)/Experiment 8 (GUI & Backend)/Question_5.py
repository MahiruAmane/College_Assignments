# Write a Python Program To Design a Login & Signup Authentication System.

import tkinter as tk
import tkinter.messagebox as messagebox

users = {}

def signup():
    username = entry_username.get()
    password = entry_password.get()

    if not username or not password:
        messagebox.showerror("Error", "Username & Password Cannot Be Empty!")
        return
    if len(password) < 6:
        messagebox.showerror("Error", "Password Must Be At Least 6 Characters Long!")
        return
    if username in users:
        messagebox.showerror("Error", "Username Already Exists!")
        return
    users[username] = password
    messagebox.showinfo("Success", "Signup Successful!")

def login():
    username = entry_username.get()
    password = entry_password.get()
    
    if not username or not password:
        messagebox.showerror("Error", "Username & Password Cannot Be Empty!")
        return
    if len(password) < 6:
        messagebox.showerror("Error", "Password Must Be At Least 6 Characters Long!")
        return
    if username in users and users[username] == password:
        messagebox.showinfo("Success", "Login Successful!")
    else:
        messagebox.showerror("Error", "Invalid Username Or Password!")

root = tk.Tk()
root.title("Login & Signup Authentication System")
root.geometry("1280x720")

calc_frame = tk.Frame(root)
calc_frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

for i in range(3):
    calc_frame.columnconfigure(i, weight=1, uniform="equal")

label_username = tk.Label(calc_frame, text="Username", bg="lightgray")
label_username.grid(row=0, column=0, pady=10)
entry_username = tk.Entry(calc_frame, width=30)
entry_username.grid(row=0, column=1, pady=10)

label_password = tk.Label(calc_frame, text="Password", bg="lightgray")
label_password.grid(row=1, column=0, padx=10, pady=10)
entry_password = tk.Entry(calc_frame, show="*", width=30)
entry_password.grid(row=1, column=1, padx=10, pady=10)

button_signup = tk.Button(calc_frame, text="Signup", command=signup, fg = "blue")
button_signup.grid(row=2, column=0, columnspan=2, padx=10, pady=10)
button_login = tk.Button(calc_frame, text="Login", command=login, fg = "green")
button_login.grid(row=2, column=1, columnspan=1, padx=10, pady=10)

root.mainloop()