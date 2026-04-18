# Write a Python Program To Create a GUI Based Task Manager where Users Can Add, Edit & Remove Tasks.
# Use Tkinter, SQLite (Task Storage).

import tkinter as tk
import tkinter.messagebox as messagebox
import sqlite3

command = sqlite3.connect('task_manager.db')
cursor = command.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS tasks
                (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    description TEXT NOT NULL
                )''')
command.commit()
command.close()

def load_tasks():
    conn = sqlite3.connect('task_manager.db')
    cursor = conn.cursor()
    cursor.execute("SELECT id, description FROM tasks")
    tasks = cursor.fetchall()
    conn.close()
    listbox_tasks.delete(0, tk.END)
    for task in tasks:
        listbox_tasks.insert(tk.END, f"{task[0]}: {task[1]}")   

def add_task():
    description = entry_task.get()
    if not description:
        messagebox.showerror("Error", "Task Description Cannot Be Empty!")
        return
    conn = sqlite3.connect('task_manager.db')
    cursor = conn.cursor()
    cursor.execute("INSERT INTO tasks (description) VALUES (?)", (description,))
    conn.commit()
    conn.close()
    messagebox.showinfo("Success", "Task Added Successfully!")
    entry_task.delete(0, tk.END)
    load_tasks()

def edit_task():
    selected_task = listbox_tasks.curselection()
    if not selected_task:
        messagebox.showerror("Error", "No Task Selected!")
        return
    new_description = entry_task.get()
    if not new_description:
        messagebox.showerror("Error", "Task Description Cannot Be Empty!")
        return
    task_id = listbox_tasks.get(selected_task[0]).split(":")[0]
    conn = sqlite3.connect('task_manager.db')
    cursor = conn.cursor()
    cursor.execute("UPDATE tasks SET description = ? WHERE id = ?", (new_description, task_id))
    conn.commit()
    conn.close()
    messagebox.showinfo("Success", "Task Updated Successfully!")
    entry_task.delete(0, tk.END)
    load_tasks()

def remove_task():
    selected_task = listbox_tasks.curselection()
    if not selected_task:
        messagebox.showerror("Error", "No Task Selected!")
        return
    task_id = listbox_tasks.get(selected_task[0]).split(":")[0]
    conn = sqlite3.connect('task_manager.db')
    cursor = conn.cursor()
    cursor.execute("DELETE FROM tasks WHERE id = ?", (task_id,))
    conn.commit()
    conn.close()
    messagebox.showinfo("Success", "Task Removed Successfully!")
    entry_task.delete(0, tk.END)
    load_tasks()

root = tk.Tk()
root.title("Task Manager")
root.geometry("1280x720")

label_task = tk.Label(root, text="Task Description", bg="lightgray")
label_task.pack(pady=10)
entry_task = tk.Entry(root, width=40)
entry_task.pack(pady=5)

button_add = tk.Button(root, text="Add Task", command=add_task, fg="green")
button_add.pack(pady=5)

button_edit = tk.Button(root, text="Edit Task", command=edit_task, fg="blue")
button_edit.pack(pady=5)

button_remove = tk.Button(root, text="Remove Task", command=remove_task, fg="red")
button_remove.pack(pady=5)

listbox_tasks = tk.Listbox(root, width=50)
listbox_tasks.pack(pady=10)

load_tasks()
root.mainloop()