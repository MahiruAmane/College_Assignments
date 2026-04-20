# Advanced Student Data Analyzer - Final Project
# Importing Necessary Libraries

import tkinter as tk
from tkinter import messagebox, filedialog
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import sqlite3

# Function To Clear Login Fields
def clear():
    entry_user.delete(0, tk.END)
    entry_pass.delete(0, tk.END)

# Function To Connect To SQLite Database And Create Users Table If Not Exists
def database_connect():

    conn = sqlite3.connect("user_data.db")
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS users (username TEXT PRIMARY KEY, password TEXT)")
    conn.commit()
    conn.close()

# Function To Handle User Signup With Validations
def signup():

    user = entry_user.get()
    password = entry_pass.get()

    if not user or not password:
        messagebox.showwarning("Warning", "Fields Cannot Be Empty!")
        return
    if len(password) < 6:
        messagebox.showwarning("Warning", "Password Must Be At Least 6 Characters Long!")
        return
    if user[0].isdigit() or user[0] in ['@', '#', '$', '%', '&', '*'] or user[0].isspace():
        messagebox.showwarning("Warning", "Username Cannot Start With A Number Or Special Character!")
        return
        
    conn = sqlite3.connect("user_data.db")
    cursor = conn.cursor()

    try:
        cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", (user, password))
        conn.commit()
        messagebox.showinfo("Success", "Account Created! You Can Now Login.")
    except sqlite3.IntegrityError:
        messagebox.showwarning("Warning", "Username Already Exists!")
    finally:
        conn.close()
        clear()

# Function To Handle User Login With Validations & Transition To Dashboard
def login():

    user = entry_user.get()
    password = entry_pass.get()

    if not user or not password:
        messagebox.showwarning("Warning", "Fields Cannot Be Empty!")
        return

    conn = sqlite3.connect("user_data.db")
    cursor = conn.cursor()
    cursor.execute("SELECT password FROM users WHERE username=?", (user,))
    result = cursor.fetchone()
    conn.close()

    if result and result[0] == password:
        login_frame.pack_forget() 
        dashboard_frame.pack(fill=tk.BOTH, expand=True) 
        root.title("Advanced Student Data Analyzer - Dashboard")
    else:
        messagebox.showerror("Error", "Invalid Credentials!")

# Function To Handle Logout With Confirmation & Transition Back To Login Screen
def logout():
    exit = messagebox.askyesno("Logout Confirmation", "Are You Sure You Want To Logout?")
    if exit:
        dashboard_frame.pack_forget() 
        login_frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER) 
        root.title("Student Analysis System - Login")
        clear()
    else:
        return


global_df = None
global_subject_cols = []
global_canvas = None

# Function To Load CSV File, Identify Subject Columns & Display Initial Info
def load_csv():

    global global_df, global_subject_cols
    # Open File Dialog To Select CSV File With Filter For CSV Files Only
    filepath = filedialog.askopenfilename(filetypes=[("CSV Files", "*.csv")])

    if filepath:
        global_df = pd.read_csv(filepath)

        if "ID" in global_df.columns:
            global_df.set_index("ID", inplace=True)
            
        numeric_cols = global_df.select_dtypes(include='number').columns.tolist()
        global_subject_cols = [c for c in numeric_cols if c not in ['Total Marks', 'Percentage', 'Rank']]
            
        text_out.delete("1.0", tk.END)
        text_out.insert(tk.END, f"Dataset Loaded Successfully! ({len(global_df)} Students Found)\n")
        text_out.insert(tk.END, f"Identified Subjects: {', '.join(global_subject_cols)}\n\n")
        text_out.insert(tk.END, "Click 'Run Deep Analysis' To Process The Marks.")

# Function To Analyze Data, Calculate Totals, Percentages, Ranks & Generate Comprehensive Report
def analyze_data():

    if global_df is None:
        messagebox.showinfo("No Data", "Please Load a CSV File First.")
        return

    max_marks_per_subject = 100
    num_subjects = len(global_subject_cols)
    
    global_df['Total Marks'] = global_df[global_subject_cols].sum(axis=1)
    global_df['Percentage'] = (global_df['Total Marks'] / (num_subjects * max_marks_per_subject)) * 100
    global_df['Rank'] = global_df['Total Marks'].rank(ascending=False, method='min').astype(int)

    subjects_df = global_df[global_subject_cols]
    class_stats = subjects_df.agg(['mean', 'median', 'max', 'min', 'std', 'var']).round(2)
    class_stats.rename(index={'std': 'Std Dev', 'var': 'Variance'}, inplace=True)
    
    top_student_id = global_df['Percentage'].idxmax()
    top_student_pct = global_df['Percentage'].max()
    overall_class_avg = global_df['Percentage'].mean()
    
    passed = (global_df['Percentage'] >= 40).sum()
    failed = len(global_df) - passed
    distinctions = (global_df['Percentage'] >= 75).sum()
    toppers = global_df[global_df['Percentage'] >= 90].shape[0]

    subject_means = subjects_df.mean()
    easiest_sub = subject_means.idxmax()
    hardest_sub = subject_means.idxmin()

    report = f"====== COMPREHENSIVE CLASS ANALYSIS ======\n\n"
    report += f"Total Students -  {len(global_df)}  |  Passed - {passed}  |  Failed - {failed}  |  Above Average (>=75%) -  {distinctions} |  Toppers (>=90%) - {toppers}\n"
    report += f"Class Average -  {overall_class_avg:.2f}%  |  Top Performer -  {top_student_id} ({top_student_pct:.2f}%)\n"
    report += f"Easiest Subject (Highest Avg) -  {easiest_sub}  |  Hardest Subject (Lowest Avg) - {hardest_sub}\n"
    report += "-" * 75 + "\n\n"
    report += "----- SUBJECT-WISE STATISTICS (Subjects Only) -----\n"
    report += class_stats.to_string() + "\n\n"
    report += "----- TOP 10 STUDENTS (Leaderboard) -----\n"
    leaderboard = global_df[['Total Marks', 'Percentage', 'Rank']].sort_values(by='Rank', ascending=True).head(10)
    report += leaderboard.to_string()

    text_out.delete("1.0", tk.END)
    text_out.insert(tk.END, report)

# Function To Generate Graphs Based On User Selection With Dynamic Layout Adjustments
def plot_graphs():

    global global_canvas

    if global_df is None: 
        messagebox.showinfo("No Data", "Please Load a CSV File First.")
        return
    
    if 'Percentage' not in global_df.columns:
        messagebox.showinfo("Error", "Please Click 'Run Deep Analysis' First To Calculate Percentages.")
        return

    if global_canvas:
        global_canvas.get_tk_widget().destroy()

    subjects_df = global_df[global_subject_cols]
    
    selected_plots = []
    if var_bar.get(): selected_plots.append('bar')
    if var_box.get(): selected_plots.append('box')
    if var_line.get(): selected_plots.append('line')
    if var_pie.get(): selected_plots.append('pie')
    
    plots = len(selected_plots)
    if plots == 0: 
        return

    fig = plt.Figure(figsize=(10, 6.5), dpi=100)
    
    # Dynamically Create Subplots Based On Number Of Selected Graphs With Improved Layout Logic
    for i, ptype in enumerate(selected_plots):
        if plots == 1:
            ax = fig.add_subplot(1, 1, 1)
        elif plots == 2:
            ax = fig.add_subplot(1, 2, i + 1)
        elif plots == 3:
            if i < 2:
                ax = fig.add_subplot(2, 2, i + 1)
            else:
                ax = fig.add_subplot(2, 2, (3, 4))
        else:
            ax = fig.add_subplot(2, 2, i + 1)

        if ptype == 'bar':
            subjects_df.mean().plot(kind='bar', ax=ax, color=['#4C72B0', '#55A868', '#C44E52', '#8172B2', '#CCB974'])
            ax.set_title("Average Marks (Subjects Only)", fontsize=10)
            ax.tick_params(axis='x', rotation=0, labelsize=8)
        elif ptype == 'box':
            subjects_df.plot(kind='box', ax=ax, patch_artist=True)
            ax.set_title("Mark Spread & Outliers (Subjects Only)", fontsize=10)
            ax.tick_params(axis='x', labelsize=8)
        elif ptype == 'line':
            subjects_df.head(10).plot(kind='line', marker='o', ax=ax)
            ax.set_title("Performance Trends (First 10 Students)", fontsize=10)
            ax.tick_params(axis='x', labelsize=8)
            ax.legend(fontsize=7, loc='upper right')
        elif ptype == 'pie':
            passed = (global_df['Percentage'] >= 40).sum()
            failed = len(global_df) - passed
            ax.pie([passed, failed], labels=['Passed', 'Failed'], autopct='%1.1f%%', 
                   colors=['#55A868', '#C44E52'], startangle=140, explode=(0.05, 0), shadow=True)
            ax.set_title("Class Pass/Fail Ratio", fontsize=10)
    
    fig.tight_layout(pad=2.0)
    global_canvas = FigureCanvasTkAgg(fig, master=canvas_frame)
    global_canvas.draw()
    global_canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)

# Initialize Database And Start The Application
database_connect()

# Setting Up The Main Application Window And Layout
root = tk.Tk()
root.title("Student Analysis System - Login")
root.geometry("1280x720")

login_frame = tk.Frame(root)
login_frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

# Login Screen UI Elements With Improved Styling And Layout
tk.Label(login_frame, text="Student Analysis System - Login Screen", font=("Arial", 16, "bold")).grid(row=0, column=0, pady=10)
tk.Label(login_frame, text="Username").grid(row=1, column=0, pady=5)

entry_user = tk.Entry(login_frame)
entry_user.grid(row=2, column=0, pady=5)

tk.Label(login_frame, text="Password").grid(row=3, column=0, pady=5)
entry_pass = tk.Entry(login_frame, show="*")
entry_pass.grid(row=4, column=0, pady=5)

tk.Button(login_frame, text="Login", bg="lightblue", width=15, command=login).grid(row=5, column=0, pady=10)
tk.Button(login_frame, text="Sign Up", width=15, command=signup).grid(row=6, column=0, pady=10)
tk.Button(login_frame, text="Clear", width=15, command=clear, fg="red").grid(row=7, column=0, pady=5)

dashboard_frame = tk.Frame(root)

control_frame = tk.Frame(dashboard_frame, bg="#e0e0e0", pady=10)
control_frame.pack(fill=tk.X)

# Dashboard Control Buttons With Improved Styling
tk.Button(control_frame, text="(1) Load CSV File", command=load_csv, bg="lightgreen", font=("Arial", 10, "bold")).pack(side=tk.LEFT, padx=10)
tk.Button(control_frame, text="(2) Run Deep Analysis", command=analyze_data, bg="lightblue", font=("Arial", 10, "bold")).pack(side=tk.LEFT, padx=10)
tk.Button(control_frame, text="(3) Logout", command=logout, bg="red", font=("Arial", 10, "bold")).pack(side=tk.RIGHT, padx=10)

text_out = tk.Text(dashboard_frame, height=16, bg="#f4f6f9", font=("Courier", 10))
text_out.pack(fill=tk.X, padx=10, pady=10)

graph_controls = tk.LabelFrame(dashboard_frame, text="Visualization Options")
graph_controls.pack(fill=tk.X, padx=10)

var_bar = tk.BooleanVar(value=True)
var_box = tk.BooleanVar()
var_line = tk.BooleanVar()
var_pie = tk.BooleanVar()

# Graph Selection Checkbuttons With Improved Layout And Default Selection
tk.Checkbutton(graph_controls, text="Subject Averages (Bar)", variable=var_bar).pack(side=tk.LEFT, padx=10)
tk.Checkbutton(graph_controls, text="Mark Distribution (Box)", variable=var_box).pack(side=tk.LEFT, padx=10)
tk.Checkbutton(graph_controls, text="Top 10 Trend (Line)", variable=var_line).pack(side=tk.LEFT, padx=10)
tk.Checkbutton(graph_controls, text="Pass/Fail Ratio (Pie)", variable=var_pie).pack(side=tk.LEFT, padx=10)

tk.Button(graph_controls, text="(4) Generate Graphs", command=plot_graphs, bg="lightyellow", font=("Arial", 10, "bold")).pack(side=tk.RIGHT, padx=10, pady=5)

# Canvas Frame For Graphical Output With Dynamic Resizing
canvas_frame = tk.Frame(dashboard_frame)
canvas_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=5)

# Start The Main Event Loop
root.mainloop()